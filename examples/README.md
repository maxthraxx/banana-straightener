# 📚 Banana Straightener Examples

This directory contains example scripts and resources to help you get started with Banana Straightener.

## 🚀 Getting Started

### For Local Development

If you're working with the source code locally:

```bash
# From the project root directory
cd banana-straightener

# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install in editable mode
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .

# Set your API key (choose one method)

# Method 1: Create .env file (recommended)
echo 'GEMINI_API_KEY=your-api-key-here' > .env

# Method 2: Environment variable  
export GEMINI_API_KEY="your-api-key-here"

# Run examples from project root
uv run python examples/basic_usage.py
uv run python examples/advanced_usage.py
```

### For Production Use

If you have the published package:

```bash
# Install uv and Banana Straightener
curl -LsSf https://astral.sh/uv/install.sh | sh
uv pip install banana-straightener

# Set your API key (choose one method)

# Method 1: Create .env file (recommended)
echo 'GEMINI_API_KEY=your-api-key-here' > .env

# Method 2: Environment variable
export GEMINI_API_KEY="your-api-key-here"
```

Get your key from: https://aistudio.google.com/app/apikey

## 📁 Available Examples

### 🌟 basic_usage.py

**Perfect for beginners!**

- Simple example showing core functionality
- Default settings and straightforward usage
- Clear output and result handling

```bash
uv run python examples/basic_usage.py
```

### 🎯 advanced_usage.py

**For power users**

- Custom configuration options
- Real-time iteration monitoring
- Input image modification
- Error handling patterns
- Custom callback functions

```bash
uv run python examples/advanced_usage.py
```

### ⚡ batch_processing.py

**Process multiple prompts efficiently**

- Batch processing workflow
- Progress tracking and statistics
- Results summary and reporting
- Performance optimization

```bash
uv run python examples/batch_processing.py
```

### ⚙️ custom_config.py

**Configuration deep dive**

- Multiple configuration strategies
- Environment-based setup
- Domain-specific configurations
- Quality vs speed trade-offs

```bash
uv run python examples/custom_config.py
```

### 📝 example_prompts.txt

**Curated prompt collection**

- 100+ tested prompts organized by category
- Creative, realistic, technical examples
- Pro tips for writing great prompts
- Style and composition guidance

Open with any text editor to browse prompts.

## 🎨 Quick Test

Want to quickly test if everything is working?

```bash
# Simple test
uv run python -c "
from banana_straightener import BananaStraightener
agent = BananaStraightener()
result = agent.straighten('a simple red circle on white background')
print('Success!' if result['success'] else 'Partial success')
"
```

## 💡 Usage Tips

### Running Examples

- All examples check for API key automatically
- Examples create their own output directories
- You can modify prompts directly in the scripts
- Check output directories for generated images

### Customization

- Copy any example as a starting point for your own scripts
- Adjust iteration counts and thresholds based on your needs
- Experiment with different prompt styles from `example_prompts.txt`

### Performance

- Start with fewer iterations (3-5) for faster experimentation
- Use higher thresholds (0.9+) only for final production runs
- Enable `save_intermediates` to see the improvement process

## 🔧 Troubleshooting

### Common Issues

**"API key not found"**

```bash
# Method 1: Create .env file (recommended)
echo 'GEMINI_API_KEY=your-key-here' > .env

# Method 2: Environment variable
export GEMINI_API_KEY="your-key-here"
```

**"Permission denied" errors**

```bash
# Make sure output directories are writable
chmod 755 ./outputs
```

**Import errors**

```bash
# Reinstall banana-straightener
uv pip install --upgrade banana-straightener
```

**Rate limit errors**

- Add delays between requests
- Reduce batch sizes
- Check your API quota

### Getting Help

- 📖 Full documentation: [README.md](../README.md)
- 🐛 Report issues: [GitHub Issues](https://github.com/velvet-shark/banana-straightener/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/velvet-shark/banana-straightener/discussions)

## 📊 Expected Outputs

When you run the examples, you'll see:

- **Console output**: Real-time progress and results
- **Image files**: Generated images in PNG format
- **Session reports**: JSON files with detailed iteration data
- **Summary statistics**: Success rates and performance metrics

All outputs are saved to clearly named directories like:

- `./outputs/` (basic usage)
- `./advanced_outputs/` (advanced usage)
- `./batch_outputs/` (batch processing)
- etc.

## 🎯 Next Steps

After trying these examples:

1. **Experiment** with different prompts from `example_prompts.txt`
2. **Customize** configurations for your specific use case
3. **Integrate** Banana Straightener into your own projects
4. **Share** your results and improvements with the community!

Happy banana straightening! 🍌✨
