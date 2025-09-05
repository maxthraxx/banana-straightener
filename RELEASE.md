# Release Process

This document describes how to create releases for the Banana Straightener project.

## 🤖 Automated Release (Recommended)

### Method 1: Automatic on Version Change

Simply update the version in both files and push to main:

1. **Update version in `pyproject.toml`**:
   ```toml
   version = "0.1.4"
   ```

2. **Update version in `src/banana_straightener/__init__.py`**:
   ```python
   __version__ = "0.1.4"
   ```

3. **Commit and push**:
   ```bash
   git add pyproject.toml src/banana_straightener/__init__.py
   git commit -m "Bump version to 0.1.4"
   git push origin main
   ```

4. **Automated workflow will**:
   - ✅ Detect version change
   - ✅ Extract release notes from CHANGELOG.md
   - ✅ Create GitHub release
   - ✅ Trigger PyPI publishing

### Method 2: Using the Bump Script (Easiest)

```bash
# Increment patch version (0.1.3 → 0.1.4)
python scripts/bump-version.py --patch --release

# Increment minor version (0.1.3 → 0.2.0)  
python scripts/bump-version.py --minor --release

# Set specific version
python scripts/bump-version.py 0.1.4 --release

# Dry run to see what would happen
python scripts/bump-version.py --patch --dry-run
```

The script will:
- ✅ Update version files
- ✅ Commit changes
- ✅ Push to main
- ✅ Trigger automated release creation

### Method 3: Manual Release with Script

For manual releases without pushing version changes:

```bash
# Use the bump script without --release flag
python scripts/bump-version.py 0.1.4

# Then create release manually if needed
gh release create v0.1.4 --title "v0.1.4" --generate-notes
```

## 📝 Updating CHANGELOG.md

For best release notes, update `CHANGELOG.md` before bumping version:

```markdown
## [0.1.4] - 2025-01-09

### ✨ New Features
- Added automated release workflows
- Created version bump script

### 🐛 Bug Fixes  
- Fixed workflow duplication issues

### 📦 Technical Changes
- Improved CI/CD pipeline separation
```

The automated release will extract the section matching your version.

## 🚀 What Happens Automatically

When you push a version change, the `release.yml` workflow:

1. **Detects version change** in pyproject.toml and __init__.py
2. **Runs tests** to ensure quality
3. **Creates GitHub release** with changelog extraction
4. **Builds package** (wheel + source distribution)  
5. **Publishes to PyPI** using trusted publishing
6. **Creates attestations** for security

All in one workflow - no chaining or multiple triggers needed!

## 📋 Manual Release (Not Recommended)

If you prefer manual control:

1. **Update versions** (as above)
2. **Create release manually**:
   ```bash
   gh release create v0.1.4 \
     --title "v0.1.4: Description" \
     --notes-file RELEASE_NOTES.md \
     --latest
   ```

## 🔍 Verification

After release:

1. **Check GitHub**: https://github.com/velvet-shark/banana-straightener/releases
2. **Check PyPI**: https://pypi.org/project/banana-straightener/
3. **Test installation**:
   ```bash
   pip install --upgrade banana-straightener==0.1.4
   straighten --version  # Should show new version
   ```

## 🛠 Troubleshooting

### Release Not Created
- Check that version actually changed in both files
- Look at [Release workflow](https://github.com/velvet-shark/banana-straightener/actions/workflows/release.yml) logs
- Ensure you pushed the version changes to main branch

### PyPI Publishing Failed
- Check [Release workflow](https://github.com/velvet-shark/banana-straightener/actions/workflows/release.yml) logs (same workflow handles everything)
- Ensure PyPI trusted publishing is configured
- Verify version doesn't already exist on PyPI

### Version Script Issues
```bash
# Make sure you're in project root
cd /path/to/banana-straightener

# Check current version
python scripts/bump-version.py --dry-run --patch

# Run with explicit version
python scripts/bump-version.py 0.1.4 --dry-run
```

## 🎯 Best Practices

1. **Always update CHANGELOG.md** before releasing
2. **Test locally** before version bump
3. **Use semantic versioning**: 
   - Patch (0.1.3 → 0.1.4): Bug fixes
   - Minor (0.1.4 → 0.2.0): New features
   - Major (0.2.0 → 1.0.0): Breaking changes
4. **Let automation handle** the release process
5. **Verify** the release worked on PyPI