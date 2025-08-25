# Path-Tree-Graph 🔄

🔄 Path-Tree-Graph – Transform file paths into hierarchical tree structures with graph-style visualization for clear directory representation and path analysis

A lightweight Python utility that converts file path lists into hierarchical tree structures with beautiful graph-style visualization, enabling clear understanding of directory hierarchies and file organization patterns.

> **Note**: This project provides an intuitive way to visualize complex file system structures, making it easier to understand project organization and directory relationships.

## ✨ Key Features

- **🔄 Path Transformation**: Automatically convert file paths to hierarchical tree structures
- **🌳 Tree Visualization**: Generate beautiful tree-style representations with proper indentation
- **📊 Graph-Style Output**: Display directory relationships with clear visual connections
- **🔧 Path Concentration**: Automatically merge single-child paths for cleaner visualization
- **📝 Flexible Input**: Support for various path formats and string representations
- **🤖 AI Agent Integration**: Perfect for RAG systems and AI agents to understand codebase structure
- **🧠 Context-Aware**: Provides intelligent path filtering and organization for AI-powered tools
- **⚡ Lightweight**: Minimal dependencies, focused on core tree building and visualization

## 🚀 Quick Start

### Installation

#### From Source
```bash
# Clone the repository
git clone https://github.com/kenyo3026/path-tree-graph.git
cd path-tree-graph

# Install dependencies
pip install -r requirements.txt

# Or install in development mode
pip install -e .
```

#### Install directly from GitHub
```bash
# Install the latest version
pip install git+https://github.com/kenyo3026/path-tree-graph.git

# Or install a specific branch/tag
pip install git+https://github.com/kenyo3026/path-tree-graph.git@main
```

**Dependencies:**
- Python 3.10+
- pathlib (built-in)
- os (built-in)
- typing (built-in)

### Basic Usage

#### **1. Simple Tree Creation**
```python
from lib.tree_graph import TreeGraph

# Define your file paths
paths = [
    '/home/user/project/src/main.py',
    '/home/user/project/src/utils/helper.py',
    '/home/user/project/tests/test_main.py',
    '/home/user/project/README.md'
]

# Create tree visualization
tree = TreeGraph.from_paths(paths, concentrate=False)
tree.display()

# With path concentration (merge single-child paths)
tree_concentrated = TreeGraph.from_paths(paths, concentrate=True)
tree_concentrated.display()
```

#### **2. API Endpoint Organization**
```python
# Analyze and organize API endpoint patterns
api_paths = [
    '/api/v1/users/profile',
    '/api/v1/users/settings',
    '/api/v2/auth/login',
    '/api/v2/auth/logout'
]
tree = TreeGraph.from_paths(api_paths)
tree.display()
```

#### **3. AI Agent Path RAG Reference** 🧠
```python
# Use as a reference system for AI agents to understand codebase structure
# Perfect for RAG (Retrieval-Augmented Generation) systems that need to
# understand project organization and file relationships

def create_codebase_reference(project_root):
    """Create a tree reference for AI agents to understand project structure"""
    import os
    from pathlib import Path
    
    # Get all relevant files (exclude common ignore patterns)
    ignore_patterns = {'.git', '__pycache__', '.pytest_cache', 'node_modules'}
    
    paths = []
    for root, dirs, files in os.walk(project_root):
        # Filter out ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_patterns]
        
        for file in files:
            if not file.startswith('.'):
                rel_path = os.path.relpath(os.path.join(root, file), project_root)
                paths.append(rel_path)
    
    # Create tree reference
    tree = TreeGraph.from_paths(paths, concentrate=True)
    
    # This tree can be used by AI agents to:
    # - Understand project structure
    # - Navigate codebase efficiently
    # - Make informed decisions about file locations
    # - Provide context-aware code suggestions
    
    return tree

# Example usage for AI agent
codebase_tree = create_codebase_reference('/path/to/your/project')
codebase_tree.display()

# AI agent can now use this tree to:
# "Where should I create a new utility function?"
# "What's the typical structure for test files?"
# "How is this project organized?"
```

## 📖 Configuration

The tree builder supports various configuration options:

```python
# Basic tree creation
tree = TreeGraph.from_paths(paths)

# With path concentration enabled
tree = TreeGraph.from_paths(paths, concentrate=True)

# Custom tree formatting
formatted_output = tree.format()
print(formatted_output)

# Traverse tree nodes
all_nodes = tree.traverse()
```

## 🧪 Testing

```bash
# Run the example directly
python lib/tree_graph.py

# This will process sample paths and display both concentrated and non-concentrated trees
```

## 📚 API Reference

### TreeGraph Class

```python
class TreeGraph:
    @classmethod
    def from_paths(
        cls,
        paths: List[str],
        concentrate: bool = True,
    ) -> PathTree
```

**Parameters:**
- `paths`: List of file paths to convert into tree structure
- `concentrate`: Whether to merge single-child paths for cleaner visualization

**Returns:**
- `PathTree` object with hierarchical structure

### PathTree Class

```python
class PathTree:
    def add_path(self, path_parts: List[str])
    def traverse(self, node=None) -> List[str]
    def format(self, node=None, prefix="") -> str
    def display(self, **kwargs)
```

**Key Methods:**
- `add_path()`: Add a new path to the tree
- `traverse()`: Get all node names in traversal order
- `format()`: Generate formatted string representation
- `display()`: Print formatted tree to console

### PathTreeNode Class

```python
class PathTreeNode:
    def __init__(self, name: str, is_leaf: bool = False)
    def add_child(self, child_name: str, is_leaf: bool = False) -> PathTreeNode
    def concentrate(self)
```

**Properties:**
- `name`: Node name/path
- `is_leaf`: Whether node represents a file (leaf) or directory
- `children`: Dictionary of child nodes


## 🔧 Advanced Features

### Path Concentration
The `concentrate` feature automatically merges single-child paths for cleaner visualization:

```python
# Without concentration
tree = TreeGraph.from_paths(paths, concentrate=False)
# Shows: /home/user/project/src/main.py

# With concentration
tree = TreeGraph.from_paths(paths, concentrate=True)
# Shows: /home/user/project/src/main.py (merged single-child paths)
```

### Custom Formatting
```python
# Get formatted string without printing
formatted = tree.format()
print(formatted)

# Custom prefix for different display styles
custom_format = tree.format(prefix="  ")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Built with Python's built-in libraries for maximum compatibility
- Designed for clear and intuitive path visualization
- Thanks to the Python community for excellent path handling tools

---

Made with ❤️ for the path visualization community
