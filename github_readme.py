# server.py
import os
import fnmatch
from pathlib import Path
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Github_Docs")

# Configuration
IGNORE_PATTERNS = [
    "*.pyc", "__pycache__", ".git", ".gitignore", "node_modules", 
    ".env", "*.log", ".DS_Store", "*.tmp", "*.temp", ".vscode",
    ".idea", "*.sqlite", "*.db", "dist", "build", ".pytest_cache"
]

def should_ignore(path: str) -> bool:
    """Check if a file/folder should be ignored based on common patterns"""
    name = os.path.basename(path)
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return True
    return False

def get_file_info(file_path: Path) -> Dict[str, Any]:
    """Get information about a file"""
    try:
        stat = file_path.stat()
        return {
            "name": file_path.name,
            "path": str(file_path),
            "size": stat.st_size,
            "is_file": file_path.is_file(),
            "extension": file_path.suffix
        }
    except (OSError, PermissionError):
        return {"name": file_path.name, "path": str(file_path), "error": "Access denied"}

def analyze_project_structure(project_path: str, max_depth: int = 3) -> Dict[str, Any]:
    """Analyze project structure and identify key files"""
    project_root = Path(project_path)
    
    if not project_root.exists():
        return {"error": f"Project path '{project_path}' does not exist"}
    
    structure = {
        "root": str(project_root),
        "files": [],
        "directories": [],
        "key_files": {},
        "languages": set(),
        "framework_indicators": []
    }
    
    # Key files to look for
    key_files_patterns = {
        "readme": ["README.md", "README.txt", "README.rst", "readme.md"],
        "license": ["LICENSE", "LICENSE.txt", "LICENSE.md", "license"],
        "config": ["package.json", "requirements.txt", "setup.py", "Cargo.toml", 
                  "composer.json", "pom.xml", "build.gradle", "Gemfile"],
        "docker": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
        "ci": [".github/workflows", ".gitlab-ci.yml", ".travis.yml"],
        "env": [".env.example", ".env.sample"]
    }
    
    # Walk through directory structure
    for root, dirs, files in os.walk(project_root):
        current_depth = len(Path(root).relative_to(project_root).parts)
        if current_depth > max_depth:
            continue
            
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d))]
        
        for file in files:
            file_path = Path(root) / file
            if should_ignore(str(file_path)):
                continue
                
            file_info = get_file_info(file_path)
            structure["files"].append(file_info)
            
            # Detect programming languages
            ext = file_path.suffix.lower()
            if ext in ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.go', '.rs', '.rb', '.php']:
                structure["languages"].add(ext[1:])
            
            # Check for key files
            for category, patterns in key_files_patterns.items():
                for pattern in patterns:
                    if file.lower() == pattern.lower() or file == pattern:
                        structure["key_files"][category] = str(file_path)
    
    structure["languages"] = list(structure["languages"])
    return structure

@mcp.tool()
def scan_project(project_path: str) -> Dict[str, Any]:
    """Scan a project directory and analyze its structure"""
    return analyze_project_structure(project_path)

@mcp.tool()
def read_file(file_path: str) -> str:
    """Read the contents of a specific file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except UnicodeDecodeError:
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
            return f"[File read with latin-1 encoding]\n{content}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
def generate_readme(project_path: str, project_name: str = None, description: str = None) -> str:
    """Generate a comprehensive README.md for a project"""
    
    # Analyze project structure
    analysis = analyze_project_structure(project_path)
    
    if "error" in analysis:
        return f"Error: {analysis['error']}"
    
    # Auto-detect project name if not provided
    if not project_name:
        project_name = Path(project_path).name
    
    # Start building README content
    readme_content = f"# {project_name}\n\n"
    
    # Add description
    if description:
        readme_content += f"{description}\n\n"
    else:
        readme_content += "A brief description of your project.\n\n"
    
    # Add languages/technologies section
    if analysis["languages"]:
        readme_content += "## Technologies Used\n\n"
        for lang in sorted(analysis["languages"]):
            readme_content += f"- {lang.upper()}\n"
        readme_content += "\n"
    
    # Add installation section
    readme_content += "## Installation\n\n"
    
    # Provide installation instructions based on detected files
    if "package.json" in str(analysis.get("key_files", {})):
        readme_content += "```bash\nnpm install\n```\n\n"
    elif "requirements.txt" in str(analysis.get("key_files", {})):
        readme_content += "```bash\npip install -r requirements.txt\n```\n\n"
    elif "Cargo.toml" in str(analysis.get("key_files", {})):
        readme_content += "```bash\ncargo build\n```\n\n"
    else:
        readme_content += "Add installation instructions here.\n\n"
    
    # Add usage section
    readme_content += "## Usage\n\n"
    readme_content += "Describe how to use your project here.\n\n"
    
    # Add project structure if it's not too complex
    if len(analysis["files"]) <= 20:
        readme_content += "## Project Structure\n\n"
        readme_content += "```\n"
        for file_info in sorted(analysis["files"], key=lambda x: x["path"]):
            if file_info.get("is_file", True):
                rel_path = Path(file_info["path"]).relative_to(analysis["root"])
                readme_content += f"{rel_path}\n"
        readme_content += "```\n\n"
    
    # Add contributing section
    readme_content += "## Contributing\n\n"
    readme_content += "1. Fork the repository\n"
    readme_content += "2. Create your feature branch (`git checkout -b feature/AmazingFeature`)\n"
    readme_content += "3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)\n"
    readme_content += "4. Push to the branch (`git push origin feature/AmazingFeature`)\n"
    readme_content += "5. Open a Pull Request\n\n"
    
    # Add license section if license file exists
    if "license" in analysis.get("key_files", {}):
        readme_content += "## License\n\n"
        readme_content += "This project is licensed under the terms found in the LICENSE file.\n\n"
    
    return readme_content

@mcp.tool()
def save_readme(project_path: str, readme_content: str) -> str:
    """Save README content to README.md file in the project directory"""
    try:
        readme_path = Path(project_path) / "README.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        return f"README.md saved successfully to {readme_path}"
    except Exception as e:
        return f"Error saving README.md: {str(e)}"

# Add a resource to get project information
@mcp.resource("project://{project_path}")
def get_project_info(project_path: str) -> str:
    """Get comprehensive project information"""
    analysis = analyze_project_structure(project_path)
    
    if "error" in analysis:
        return f"Error analyzing project: {analysis['error']}"
    
    info = f"Project Analysis for: {analysis['root']}\n"
    info += f"Total files: {len(analysis['files'])}\n"
    info += f"Languages detected: {', '.join(analysis['languages'])}\n"
    info += f"Key files found: {', '.join(analysis['key_files'].keys())}\n"
    
    return info

if __name__ == "__main__":
    # Run the MCP server
    mcp.run()