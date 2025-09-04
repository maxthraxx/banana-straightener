# 🧪 Testing Guide

This directory contains all tests for the Banana Straightener project.

## 📁 Test Structure

```
tests/
├── README.md              # This file
├── __init__.py            # Package init
├── test_quick.py          # Fast tests, no API calls
├── test_image_generation.py # Core functionality tests (requires API key)
├── test_integration.py    # End-to-end workflow tests (requires API key)  
├── test_local.py          # Comprehensive local development script
└── test_quick_manual.py   # Simple manual image generation test
```

## 🚀 Quick Start

### Prerequisites

Most tests require a valid Gemini API key:

```bash
# Get API key from: https://aistudio.google.com/app/apikey
export GEMINI_API_KEY='your-key-here'

# Or create .env file in project root:
echo 'GEMINI_API_KEY=your-key-here' > .env
```

### Running Tests

```bash
# Quick smoke tests (no API key required)
uv run pytest tests/test_quick.py -v

# Local development validation (comprehensive)
uv run python tests/test_local.py

# Simple image generation test (requires API key)
uv run python tests/test_quick_manual.py

# All tests (requires API key)
uv run pytest -v

# Exclude slow tests
uv run pytest -m "not slow" -v
```

## 📋 Test Categories

### 🟢 `test_quick.py` - Fast Tests
- **Purpose**: Basic functionality without API calls
- **Speed**: Very fast (~1 second)
- **Requirements**: None
- **What it tests**: 
  - Imports work correctly
  - Classes can be instantiated
  - Configuration works
  - Placeholder functionality

### 🟡 `test_image_generation.py` - Core Functionality
- **Purpose**: Test image generation and evaluation
- **Speed**: Slow (requires API calls)
- **Requirements**: Valid `GEMINI_API_KEY`
- **What it tests**:
  - Actual image generation
  - Image evaluation
  - Model creation
  - API integration

### 🟠 `test_integration.py` - End-to-End Tests  
- **Purpose**: Complete workflow testing
- **Speed**: Slow (requires API calls)
- **Requirements**: Valid `GEMINI_API_KEY`
- **What it tests**:
  - Full BananaStraightener workflow
  - CLI integration
  - Configuration loading
  - File output

### 🔧 `test_local.py` - Development Script
- **Purpose**: Comprehensive local validation
- **Speed**: Fast
- **Requirements**: None (API key optional)
- **What it tests**:
  - Package structure
  - CLI commands
  - Import functionality
  - Basic smoke tests

### 🎯 `test_quick_manual.py` - Manual Test
- **Purpose**: Simple image generation validation
- **Speed**: Medium (one API call)
- **Requirements**: Valid `GEMINI_API_KEY`
- **What it tests**:
  - Single image generation
  - End-to-end functionality
  - Quick validation

## 🏷️ Test Markers

Tests use pytest markers for organization:

- `@pytest.mark.slow` - Tests that make API calls
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.quick` - Fast tests without API calls

Run specific categories:
```bash
# Only fast tests
uv run pytest -m "not slow"

# Only slow tests (requires API key)
uv run pytest -m "slow"

# Only integration tests
uv run pytest -m "integration"
```

## 🎛️ Configuration

Tests are configured via `pytest.ini` in the project root:

```ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --verbose --tb=short -ra
markers =
    slow: marks tests as slow (requiring API calls)
    integration: marks tests as integration tests  
    quick: marks tests as quick (no API calls required)
```

## ❗ Common Issues

### `ModuleNotFoundError: No module named 'banana_straightener'`

The package isn't installed in development mode:

```bash
uv pip install -e .
```

### `API key not valid`

You need a real API key from Google:

1. Get one at: https://aistudio.google.com/app/apikey
2. Set it: `export GEMINI_API_KEY='your-key-here'`
3. Or create `.env` file in project root

### `ImportError` for Google libraries

Dependencies aren't installed:

```bash
uv sync  # Reinstall all dependencies
```

## 🎯 Recommended Testing Workflow

For **development**:
```bash
# 1. Quick smoke test
uv run pytest tests/test_quick.py -v

# 2. Local validation  
uv run python tests/test_local.py

# 3. Test image generation (if you have API key)
uv run python tests/test_quick_manual.py
```

For **CI/CD**:
```bash
# Fast tests only (no API key required)
uv run pytest tests/test_quick.py

# Or all tests if API key is available
uv run pytest -v
```

For **comprehensive testing**:
```bash
# Everything (requires API key)
uv run pytest -v --cov=banana_straightener
```