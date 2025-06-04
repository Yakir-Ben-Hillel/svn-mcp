import subprocess
from typing import List


def _run_command(cmd: List[str]) -> subprocess.CompletedProcess:
    """Internal helper to run a command using subprocess."""
    return subprocess.run(cmd, check=True, capture_output=True, text=True)


def checkout(url: str, dest: str) -> subprocess.CompletedProcess:
    """Checkout an SVN repository to a destination directory."""
    return _run_command(["svn", "checkout", url, dest])


def commit(message: str) -> subprocess.CompletedProcess:
    """Commit local changes with a commit message."""
    return _run_command(["svn", "commit", "-m", message])
