from setuptools import setup, find_packages


LIBRARY_NAME = "path_tree_graph"
PACKAGE_DIR = 'lib'

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name=LIBRARY_NAME,
    version="0.1.0",
    packages=[PACKAGE_DIR],
    package_dir={LIBRARY_NAME: PACKAGE_DIR},
    install_requires=install_requires,
    author="kenyo3026",
    author_email="kenyo3026@gmail.com",
    description="🔄 Path-Tree-Graph – Transform file paths into hierarchical tree structures with graph-style visualization for clear directory representation and path analysis",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kenyo3026/path-tree-graph",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.10",
    keywords="path, tree, visualization, directory, file-system",
    project_urls={
        "Bug Reports": "https://github.com/kenyo3026/path-tree-graph/issues",
        "Source": "https://github.com/kenyo3026/path-tree-graph",
    },
)
