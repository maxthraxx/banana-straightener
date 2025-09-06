# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.8] - 2025-01-09

### 🖼️ Image Format Improvements
- **Fixed WebP images in web UI**: All images now display as PNG format in browsers
- **Consistent PNG output**: Images from Gemini API are immediately converted to RGB/PNG format
- **Better browser compatibility**: Right-click → Save Image now saves as PNG files instead of WebP
- **Optimized PNG compression**: Removed unnecessary quality parameters from PNG saves (PNG is lossless)

### 🔧 Technical Changes
- Added `format="png"` parameter to all Gradio Image components
- Enhanced image pipeline to convert WebP to PNG immediately after receiving from Gemini API
- Improved image consistency throughout the entire application flow
- Fixed PyPI trusted publishing configuration to match repository settings

### 🚀 Deployment & Release
- **Fixed automated PyPI publishing**: Resolved "invalid-publisher" errors with trusted publishing
- **Streamlined release workflow**: Renamed workflow from `release.yml` to `publish.yml` 
- **Environment configuration**: Added proper `pypi` environment for secure publishing
- **Reliable CI/CD**: Automated releases now work correctly with GitHub → PyPI publishing

## [0.1.4] - 2025-01-09

### 🎨 Web UI Enhancements
- **Added comparison view**: Side-by-side before/after comparison when using input images
- **Download all iterations**: New ZIP download button to get all iterations + session data
- **Mobile-responsive design**: Improved layout and touch-friendly interface for mobile devices
- **Better gallery display**: Responsive columns that adapt to screen size

### 🔧 Technical Improvements
- Enhanced session data storage for better UI integration
- Added ZIP utility for packaging session artifacts with metadata
- Improved CSS with mobile breakpoints and touch-optimized buttons
- Updated UI architecture to support new comparison and download features

### 🛠 Workflow Improvements
- Simplified GitHub Actions from 4 to 2 workflows for better maintainability
- Consolidated release process into single streamlined workflow
- Updated testing to focus on Python 3.12 & 3.13 only
- Enhanced mobile responsiveness across all UI components

## [0.1.3] - 2025-01-09

### ✨ New Features
- **Added `--version` flag**: Users can now check their installed version with `straighten --version`

### 🧪 Developer Experience
- Fixed CI test failures by handling missing API keys gracefully in GitHub Actions
- Tests now skip API-dependent operations when running in CI without API keys
- Improved pytest configuration to suppress warnings

### 📦 Technical Changes
- Version command properly imports and displays package version
- Better error handling for test environments without API credentials

## [0.1.2] - 2025-01-09

### 🚀 Major Improvements
- **Fixed Repetitive Iteration Problem**: Enhanced prompt engineering to avoid identical iterations
- **Smarter Evaluation System**: Improved evaluator to provide specific, actionable feedback instead of generic responses
- **Iteration-Aware Strategies**: Different approaches for early (1-3), mid (4-6), and late (7+) iterations
- **Alternative Approach Detection**: Automatically switches strategies when stuck in repetitive loops

### ✨ New Features
- **Feedback Diversity Check**: Detects when feedback is >80% similar to previous iterations
- **Progressive Enhancement**: Builds on previous attempts instead of starting fresh each time
- **Better Debug Logging**: Shows parsed improvements and fallback warnings
- **Multi-line Evaluation Parsing**: Properly handles bullet-point feedback from evaluator

### 🎨 UI Improvements  
- **Dark Theme Compatibility**: Fixed white text on yellow background visibility issues
- **Cleaner Layout**: Removed duplicate "Tips & Examples" sections and reduced visual clutter
- **Better Spacing**: Less crowded interface with improved margins and organization

### 🔧 Technical Changes
- Enhanced `enhance_prompt_with_feedback()` function with history tracking
- Improved evaluation prompt with specific examples of good vs bad feedback
- Better parsing of multi-line evaluator responses
- Added repetition detection algorithms

### 📦 Developer Experience
- Added GitHub Actions workflow for automated PyPI publishing
- Set up CI/CD pipeline with testing across Python 3.10-3.12
- Created comprehensive CHANGELOG for version tracking

## [0.1.1] - 2025-01-08

### 🐛 Bug Fixes
- Fixed Gradio 5.0+ Progress API compatibility issue
- Resolved "Progress.tqdm() missing 1 required positional argument" error
- Updated progress call syntax for newer Gradio versions

### 🔧 Technical Changes
- Removed problematic `progress.tqdm()` call from UI
- Updated progress syntax: `progress(value, description)` format
- Added missing `create_interface()` function for testing

## [0.1.0] - 2025-01-07

### 🎉 Initial Release
- **Core Features**: Self-correcting image generation using Gemini 2.5 Flash Image Preview
- **CLI Interface**: Command-line tool with rich formatting and progress bars
- **Web UI**: Beautiful Gradio interface with real-time iteration updates
- **Image Editing**: Support for modifying existing images or generating from scratch
- **Configurable Parameters**: Adjustable iteration limits, success thresholds, and model settings
- **Session Management**: Automatic saving of iterations, evaluations, and final results
- **Multiple Output Formats**: Gallery view, detailed evaluations, and session reports

### 📦 Package Features
- **Easy Installation**: `pip install banana-straightener`
- **Environment Configuration**: Support for `.env` files and environment variables
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Python 3.10+ Support**: Modern Python compatibility

### 🛠 Technical Architecture
- Modular design with separate generator and evaluator models
- Extensible configuration system
- Comprehensive error handling and retry logic
- Rich CLI output with emojis and progress indicators