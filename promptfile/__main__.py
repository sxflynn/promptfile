import argparse
import os
import sys
import fnmatch
from typing import List

# Editable list of glob patterns to ignore.
# Any file or directory whose name matches one of these patterns will be skipped.
IGNORE_PATTERNS: List[str] = [
    '*test*',              # Skip files/directories containing "test"
    '.*',                  # Skip hidden files/directories (those starting with a dot)
    'node_modules',        # Skip node_modules directory (non-Python, but common in JS hybrid repos)
    'package-lock.json',   # Skip JS lock files
    'coverage',            # Ignore coverage output folders
    'lcov-report',         # Ignore lcov HTML report folders
    'build',               # Skip build directories (e.g. for wheels, setuptools)
    'dist',                # Skip dist directories
    'target',              # Skip compiled output (used in some hybrid setups)
    '__pycache__',         # Skip Python bytecode cache directories
    '*.pyc',               # Skip compiled Python files
    '*.pyo',               # Skip optimized bytecode files
    '*.egg-info',          # Skip metadata from setuptools
    '*.egg',               # Skip built egg files
    '*.svg',               # Skip SVGs
    '*.log',               # Skip logs
    '*.sqlite3',           # Skip SQLite database files
    '*.db',                # Skip generic database files
    'env',                 # Skip virtual environments
    '.env',                # Skip dotenv config files
    '.venv',               # Skip virtualenv dirs
    'venv',                # Common venv dir name
    'LICENSE',             # LICENSE
    'LICENSE.*',           # Match LICENSE.md, LICENSE.txt, etc.
    '*bruno*',             # Project-specific skip
    'poetry.lock',         # Skip Poetry lockfile
    '*.png',
    '*.svg',
    '*.jpeg',
    '*.jpg',
    '*.cmd',
    'HELP.md',
    'mvnw',
    'prompt.txt'
]

def should_ignore(name: str) -> bool:
    """Return True if the given name matches any of the ignore patterns."""
    for pattern in IGNORE_PATTERNS:
        if fnmatch.fnmatch(name, pattern):
            return True
    return False


def process_directory(base_dir: str, output_to_file: bool) -> None:
    output_path: str = "prompt.txt"

    if output_to_file:
        with open(output_path, "w", encoding="utf-8"):
            pass

    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not should_ignore(d)]

        for file in files:
            if should_ignore(file):
                continue

            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, base_dir)
            file_output: List[str] = [f"File: {rel_path}"]

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    file_output.append(content)
            except Exception as e:
                file_output.append(f"Error reading file: {e}")

            file_output.append("")

            if output_to_file:
                with open(output_path, "a", encoding="utf-8") as out_file:
                    out_file.write("\n".join(file_output) + "\n")
            else:
                print("\n" + "\n".join(file_output))


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="List and print non-ignored files in a directory."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Path to the directory (relative or absolute). Defaults to current directory."
    )
    parser.add_argument(
        "--out", "-O",
        action="store_true",
        help="Write output to stdout instead of a file (default is prompt.txt)"
    )

    args: argparse.Namespace = parser.parse_args()

    base_dir: str = os.path.abspath(args.directory)

    if not os.path.isdir(base_dir):
        print(f"Provided path is not a directory: {base_dir}")
        sys.exit(1)

    output_to_file: bool = not args.out
    process_directory(base_dir, output_to_file=output_to_file)


if __name__ == '__main__':  # pragma: no cover
    main()
