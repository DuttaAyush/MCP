# MCP Server Demo

A comprehensive Model Context Protocol (MCP) server implementation featuring GitHub repository analysis, documentation generation, and basic mathematical operations. This project demonstrates the power of MCP servers for automating development workflows and repository management tasks.

## Features

### 🧮 Basic Mathematical Operations
- Simple addition tool for mathematical computations
- Personalized greeting resources with dynamic parameters

### 📁 Repository Analysis
- **Project Structure Scanning**: Automatically analyze directory structures and file organization
- **Language Detection**: Identify primary programming languages used in projects
- **Dependency Analysis**: Extract and analyze dependencies from various package managers
- **Smart File Classification**: Categorize files into entry points, tests, documentation, and configuration

### 📝 Documentation Generation
- **Automated README Creation**: Generate comprehensive README.md files with proper structure
- **Requirements File Generation**: Create requirements.txt for Python projects
- **Package.json Scripts**: Generate useful npm scripts for JavaScript projects
- **Project Structure Visualization**: Create ASCII tree representations of project hierarchies

### 🔧 GitHub Integration
- **Repository Documentation**: Comprehensive analysis and documentation generation for GitHub repositories
- **Multi-language Support**: Python, JavaScript, Java, and more
- **Dependency Mapping**: Smart mapping of import names to package names
- **Test Detection**: Automatic identification of test files and testing frameworks

## Technologies Used

- **Python**: Core implementation language
- **FastMCP**: High-performance MCP server framework
- **AST Parsing**: Advanced Python code analysis
- **Multi-format Support**: TOML, JSON, XML parsing capabilities

## Installation

### Prerequisites
- Python 3.13 or higher
- uv package manager (recommended) or pip

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd mcp-server-demo

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies (if any are added to pyproject.toml)
uv sync
# or with pip:
pip install -e .
```

## Usage

### Basic MCP Server
The main server provides simple demonstration tools:

```python
from mcp.server.fastmcp import FastMCP

# Start the basic demo server
python main.py
```

Available tools:
- `add(a: int, b: int)`: Add two numbers
- `greeting://{name}`: Get personalized greetings

### GitHub Repository Analyzer
For comprehensive repository analysis and documentation:

```bash
# Analyze a repository
python githubrepo.py /path/to/repository

# Analyze and generate documentation
python githubrepo.py /path/to/repository --output /output/directory

# Only analyze without generating files
python githubrepo.py /path/to/repository --analyze-only
```

### README Generator Server
Run the dedicated README generation server:

```python
python github_readme.py
```

Available MCP tools:
- `scan_project(project_path)`: Analyze project structure
- `read_file(file_path)`: Read file contents
- `generate_readme(project_path, project_name, description)`: Generate README content
- `save_readme(project_path, readme_content)`: Save README to file

## Project Structure

```
mcp-server-demo/
├── main.py                 # Basic MCP server with demo tools
├── github_readme.py        # README generation MCP server
├── githubrepo.py          # Comprehensive repository analyzer
├── pyproject.toml         # Project configuration
├── README.md              # This file
├── uv.lock               # Dependency lock file
└── .venv/                # Virtual environment
    ├── Scripts/          # Windows activation scripts
    └── Lib/              # Python libraries
```

## Key Features Deep Dive

### Repository Analysis Engine
The `githubrepo.py` module provides enterprise-grade repository analysis:

- **Language Detection**: Automatic identification of primary programming languages
- **Dependency Extraction**: Support for pip, npm, Maven, Gradle dependency files
- **Code Structure Analysis**: AST-based analysis for Python projects
- **Test Discovery**: Automatic detection of test files across different frameworks
- **Documentation Mining**: Extraction of existing documentation and README files

### Intelligent README Generation
- **Template-based Generation**: Professional README templates with proper sections
- **Technology-specific Instructions**: Tailored installation and usage instructions
- **Dependency Documentation**: Automatic listing of project dependencies
- **Structure Visualization**: ASCII tree representation of project layout
- **Contributing Guidelines**: Standard open-source contribution guidelines

### MCP Integration
- **FastMCP Framework**: High-performance server implementation
- **Tool Registration**: Automatic tool discovery and registration
- **Resource Management**: Dynamic resource handling with parameterized URLs
- **Error Handling**: Robust error handling and reporting

## Advanced Usage

### Custom Analysis Patterns
Extend the language patterns for new programming languages:

```python
language_patterns = {
    'rust': {
        'extensions': ['.rs'],
        'dep_files': ['Cargo.toml', 'Cargo.lock'],
        'config_files': ['rust-toolchain.toml'],
        'test_patterns': ['**/tests/*.rs'],
        'entry_points': ['main.rs', 'lib.rs']
    }
}
```

### Integration with IDEs
The MCP server can be integrated with various development environments:
- Visual Studio Code (via MCP extension)
- JetBrains IDEs (via MCP plugin)
- Command-line tools and scripts

## API Reference

### Core Tools

#### `add(a: int, b: int) -> int`
Simple mathematical addition.

#### `scan_project(project_path: str) -> Dict[str, Any]`
Comprehensive project structure analysis returning:
- File listings with metadata
- Language detection results
- Key file identification
- Directory structure mapping

#### `generate_readme(project_path: str, project_name?: str, description?: str) -> str`
Generate README content with:
- Automatic project name detection
- Technology-specific installation instructions
- Project structure visualization
- Professional formatting and sections

## Contributing

We welcome contributions to improve the MCP Server Demo! Here's how you can help:

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Set up development environment:
   ```bash
   uv sync --dev
   pre-commit install  # If pre-commit hooks are configured
   ```

### Code Style
- Follow PEP 8 for Python code
- Use type hints where appropriate
- Add docstrings for public functions
- Write tests for new features

### Testing
```bash
# Run tests (when test suite is added)
pytest

# Run with coverage
pytest --cov=. --cov-report=html
```

### Pull Request Process
1. Ensure all tests pass
2. Update documentation as needed
3. Add your changes to the changelog
4. Submit a pull request with a clear description

## Roadmap

- [ ] **Enhanced Language Support**: Add support for Go, Rust, C++, and more
- [ ] **CI/CD Integration**: Generate GitHub Actions, GitLab CI, and other CI/CD configurations
- [ ] **Documentation Templates**: Multiple README templates for different project types
- [ ] **Dependency Analysis**: Security vulnerability scanning and update recommendations
- [ ] **Code Quality Metrics**: Integration with code quality tools and reporting
- [ ] **Interactive Mode**: CLI interface for interactive project analysis
- [ ] **Web Interface**: Browser-based interface for repository analysis
- [ ] **Plugin System**: Extensible plugin architecture for custom analyzers

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [FastMCP](https://github.com/jlowin/fastmcp) framework
- Inspired by modern development automation tools
- Thanks to the Model Context Protocol community

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/your-repo/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

**Made with ❤️ for the developer community**