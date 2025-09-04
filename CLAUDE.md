# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Banana Straightener is a self-correcting image generation agent that uses Gemini 2.5 Flash to iteratively improve images until they match the user's prompt. The system generates an image, evaluates it against the original prompt, provides feedback, and regenerates until success or max iterations are reached.

## Development Commands

This project uses `uv` for fast Python package management. All Python operations should use `uv pip` instead of regular `pip`.

**Requirements**: Python 3.9+ (required by google-generativeai dependency)

### Setup
```bash
# Install uv if not already installed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Optional: Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with dev dependencies
uv pip install -e .[dev]

# Set required API key (choose one method)
# Method 1: Create .env file (recommended for development)
echo 'GEMINI_API_KEY=your-api-key-here' > .env

# Method 2: Environment variable (for deployment)
export GEMINI_API_KEY="your-api-key-here"
```

### Testing
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=banana_straightener

# Run specific test file
uv run pytest tests/test_agent.py -v

# Run single test
uv run pytest tests/test_agent.py::TestBananaStraightener::test_basic_straightening -v
```

### Code Quality
```bash
# Format code
uv run black src/ tests/

# Check style
uv run flake8 src/ tests/

# Type checking  
uv run mypy src/banana_straightener/

# Run all quality checks
uv run black src/ tests/ && uv run flake8 src/ tests/ && uv run mypy src/banana_straightener/
```

### Local Testing & Development

For local development before publishing the package:

```bash
# Install in editable mode
uv pip install -e .

# Test basic functionality
uv run python -c "from banana_straightener import BananaStraightener; print('✅ Import successful!')"

# Test CLI using module syntax
uv run python -m banana_straightener.cli --help
uv run python -m banana_straightener.cli generate "test prompt" --iterations 2

# Test CLI using entry points (after editable install)
straighten --help
straighten generate "test prompt" --iterations 2

# Test web UI
uv run python -m banana_straightener.cli ui --port 7860

# Run examples from project root
uv run python examples/basic_usage.py
uv run python examples/advanced_usage.py
uv run python examples/batch_processing.py
```

### Running Published Package
```bash
# CLI commands (after published installation)
straighten generate "your prompt"
straighten ui
straighten config
straighten examples
```

### Quick Development Workflow

Complete workflow for testing changes locally:

```bash
# 1. Make code changes to src/banana_straightener/

# 2. Run quality checks
uv run black src/ tests/
uv run flake8 src/ tests/

# 3. Test import and basic functionality
uv run python -c "from banana_straightener import BananaStraightener; print('✅ Works')"

# 4. Test CLI help (should not require API key)
uv run python -m banana_straightener.cli --help
uv run python -m banana_straightener.cli config

# 5. Test with API key (if you have one)
export GEMINI_API_KEY="your-key"
uv run python examples/basic_usage.py

# 6. Test entry points work
straighten examples

# 7. Run any existing tests
uv run pytest

# 8. Or run the comprehensive test script
uv run python test_local.py
```

## Architecture Overview

### Core Components

**BananaStraightener (agent.py)**: The main orchestrator class that manages the iterative improvement loop. Holds a generator model, evaluator model (can be the same), and configuration. The `straighten()` method is the primary entry point that runs the full cycle, while `straighten_iterative()` provides a generator for real-time updates.

**GeminiModel (models.py)**: Wraps the Google Generative AI API for both image generation and evaluation. Uses Imagen 3 for generation and Gemini 2.5 Flash for evaluation. Implements retry logic with tenacity and structured evaluation response parsing.

**Config (config.py)**: Centralized configuration management using dataclasses. Supports environment variables via python-dotenv, with sensible defaults. Key settings include model names, iteration limits, success thresholds, and output directories.

### Interface Layer

**CLI (cli.py)**: Click-based command line interface with rich formatting. Main commands: `generate`, `ui`, `examples`, `config`. Uses callbacks for progress tracking and provides comprehensive output formatting.

**Web UI (ui.py)**: Gradio-based web interface with real-time progress updates. Uses the `straighten_iterative()` generator to provide live feedback during processing.

### Core Loop Architecture

The iterative improvement follows this pattern:
1. **Generation**: Create/improve image using current prompt
2. **Evaluation**: Gemini analyzes image against original target prompt  
3. **Feedback Processing**: Parse structured evaluation response
4. **Prompt Enhancement**: Use feedback to create more specific prompt for next iteration
5. **Success Check**: Compare confidence score against threshold
6. **Session Tracking**: Save images and metadata for each iteration

The system maintains session state including iteration history, confidence scores, and intermediate results. Each session gets a unique timestamp-based ID and output directory.

## Key Implementation Details

### Model Integration
- Single GeminiModel class handles both generation (Imagen 3) and evaluation (Gemini 2.5 Flash)
- Can use same or different models for generation vs evaluation
- Implements structured evaluation prompt with specific response format parsing
- Retry logic handles API failures gracefully

### Configuration Strategy  
- Environment variables take precedence over defaults
- Configuration is immutable once created (dataclass)
- Supports both programmatic config and env-based config
- Session directories created automatically under configured output path

### Error Handling Patterns
- API failures fall back to placeholder images when needed
- Invalid images are validated before processing continues
- Configuration errors fail fast with clear messages
- Session state is preserved even when individual iterations fail

### Session Management
- Each run gets unique session ID (timestamp-based)
- All iterations saved if `save_intermediates=True`
- Session reports saved as JSON with full metadata
- Images saved with descriptive filenames based on prompts

## Testing Strategy

The codebase is structured for testability:
- Core logic separated from API calls (models.py)
- Configuration externalized and injectable
- Agent accepts custom models for testing
- CLI separated from business logic

Key areas for testing:
- Agent iteration loop logic
- Configuration loading and validation  
- Model response parsing
- CLI command execution
- Session state management

## Working with Examples

The `examples/` directory contains comprehensive usage patterns:
- `basic_usage.py`: Simple API usage
- `advanced_usage.py`: Custom configs, callbacks, real-time monitoring
- `batch_processing.py`: Processing multiple prompts efficiently
- `custom_config.py`: Different configuration strategies
- `example_prompts.txt`: Curated prompt collection

When adding new features, update relevant examples to demonstrate usage patterns.

## API Key Management

The system requires a Gemini API key from Google AI Studio. It's loaded in this priority order:
1. Explicit `api_key` parameter in Config
2. `.env` file in current or parent directories (GEMINI_API_KEY or GOOGLE_API_KEY)
3. `GEMINI_API_KEY` environment variable  
4. `GOOGLE_API_KEY` environment variable

**Recommended approach**: Create a `.env` file in your project root:
```bash
echo 'GEMINI_API_KEY=your-api-key-here' > .env
```

Never commit API keys to version control. The `.env.example` file shows the expected format, and `.env` files are already in `.gitignore`.