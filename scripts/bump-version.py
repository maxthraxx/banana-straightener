#!/usr/bin/env python3
"""
Script to bump version and optionally create a release.

Usage:
    python scripts/bump-version.py 0.1.4
    python scripts/bump-version.py 0.1.4 --release
    python scripts/bump-version.py --patch  # auto-increment patch version
    python scripts/bump-version.py --minor  # auto-increment minor version
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

def get_current_version():
    """Get current version from pyproject.toml."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")
    
    content = pyproject_path.read_text()
    match = re.search(r'version = "([^"]+)"', content)
    if not match:
        raise ValueError("Version not found in pyproject.toml")
    
    return match.group(1)

def parse_version(version_str):
    """Parse version string into components."""
    parts = version_str.split('.')
    if len(parts) != 3:
        raise ValueError("Version must be in format x.y.z")
    
    try:
        return [int(x) for x in parts]
    except ValueError:
        raise ValueError("Version parts must be integers")

def increment_version(current_version, increment_type):
    """Increment version based on type."""
    major, minor, patch = parse_version(current_version)
    
    if increment_type == "patch":
        patch += 1
    elif increment_type == "minor":
        minor += 1
        patch = 0
    elif increment_type == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        raise ValueError("Invalid increment type")
    
    return f"{major}.{minor}.{patch}"

def update_version_files(new_version):
    """Update version in pyproject.toml and __init__.py."""
    # Update pyproject.toml
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    updated_content = re.sub(
        r'version = "[^"]+"',
        f'version = "{new_version}"',
        content
    )
    pyproject_path.write_text(updated_content)
    print(f"✅ Updated pyproject.toml to {new_version}")
    
    # Update __init__.py
    init_path = Path("src/banana_straightener/__init__.py")
    if init_path.exists():
        content = init_path.read_text()
        updated_content = re.sub(
            r'__version__ = "[^"]+"',
            f'__version__ = "{new_version}"',
            content
        )
        init_path.write_text(updated_content)
        print(f"✅ Updated __init__.py to {new_version}")

def commit_and_push(new_version, create_release=False):
    """Commit version changes and optionally trigger release."""
    try:
        # Add files
        subprocess.run(["git", "add", "pyproject.toml", "src/banana_straightener/__init__.py"], check=True)
        
        # Commit
        commit_message = f"Bump version to {new_version}"
        if create_release:
            commit_message += "\n\nThis commit will trigger an automated release."
        
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"✅ Committed version bump to {new_version}")
        
        # Push
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("✅ Pushed to main branch")
        
        if create_release:
            print(f"🚀 Automated release will be created for v{new_version}")
        else:
            print(f"💡 To create a release manually, run: gh release create v{new_version}")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Bump version and optionally create release")
    
    # Version specification (mutually exclusive)
    version_group = parser.add_mutually_exclusive_group(required=True)
    version_group.add_argument("version", nargs="?", help="Explicit version (e.g., 0.1.4)")
    version_group.add_argument("--patch", action="store_true", help="Increment patch version")
    version_group.add_argument("--minor", action="store_true", help="Increment minor version") 
    version_group.add_argument("--major", action="store_true", help="Increment major version")
    
    # Options
    parser.add_argument("--release", action="store_true", help="Create GitHub release after version bump")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    
    args = parser.parse_args()
    
    # Get current version
    try:
        current_version = get_current_version()
        print(f"Current version: {current_version}")
    except Exception as e:
        print(f"❌ Error getting current version: {e}")
        sys.exit(1)
    
    # Determine new version
    if args.version:
        new_version = args.version
        try:
            parse_version(new_version)  # Validate format
        except ValueError as e:
            print(f"❌ Invalid version format: {e}")
            sys.exit(1)
    elif args.patch:
        new_version = increment_version(current_version, "patch")
    elif args.minor:
        new_version = increment_version(current_version, "minor")
    elif args.major:
        new_version = increment_version(current_version, "major")
    
    print(f"New version: {new_version}")
    
    if new_version == current_version:
        print("⚠️ Version unchanged")
        sys.exit(0)
    
    if args.dry_run:
        print("🔍 Dry run mode - no changes will be made")
        print(f"Would update version from {current_version} to {new_version}")
        if args.release:
            print("Would create GitHub release")
        return
    
    # Confirm
    confirm = input(f"Update version from {current_version} to {new_version}? (y/N): ")
    if confirm.lower() != 'y':
        print("Cancelled")
        sys.exit(0)
    
    # Update files
    try:
        update_version_files(new_version)
        commit_and_push(new_version, args.release)
        print(f"🎉 Successfully bumped version to {new_version}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()