# MCP Server Demo

A demonstration MCP (Model Context Protocol) server that provides tools for project analysis and README generation.

## Features

- **Project Structure Analysis**: Scan and analyze project directories
- **File Reading**: Read contents of specific files
- **README Generation**: Automatically generate comprehensive README files
- **Project Information**: Get detailed project insights and statistics

## Installation

1. Clone the repository
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the MCP server:
```bash
python github_readme.py
```

The server provides the following tools:
- `scan_project(project_path)` - Analyze project structure
- `read_file(file_path)` - Read file contents
- `generate_readme(project_path, project_name, description)` - Generate README
- `save_readme(project_path, readme_content)` - Save README to file

## Project Structure

```
├── github_readme.py    # Main MCP server implementation
├── pyproject.toml      # Project configuration
└── uv.lock            # Lock file
```

## Requirements

- Python 3.13+
- MCP (Model Context Protocol) framework (Like Claude Desktop..)

