# svn-mcp

A minimal Python helper package for interacting with Subversion (SVN). It
provides a thin wrapper around the `svn` command line so scripts and tools can
perform common operations programmatically.

## Installation

Clone the repository and install it in editable mode:

```bash
pip install -e .
```

## Usage

The package exposes a simple command line interface. For example, to checkout a
repository and commit changes:

```bash
python -m svn_mcp checkout http://example.com/repo path/to/dest
# make changes
python -m svn_mcp commit "My commit message"
# later update the working copy
python -m svn_mcp update path/to/dest
```

## Development

Unit tests are located in the `tests/` directory and can be run with:

```bash
python -m unittest
```
