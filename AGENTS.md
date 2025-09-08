# Repository Guidelines

## Project Structure & Module Organization
- `src/banana_straightener/` — core package: `agent.py` (iteration logic), `models.py` (Gemini interface), `cli.py` (entry points), `ui.py` (Gradio UI), `utils.py` (helpers), `__init__.py` (exports/version).
- `tests/` — pytest suite (`test_*.py`); quick, integration, and image-generation tests.
- `examples/` — prompts and sample flows; `outputs/` — run artifacts; `scripts/` — release/version helpers.
- Config: `pyproject.toml`, `pytest.ini`, `.env(.example)`; packaging via PEP 621.

## Build, Test, and Development Commands
- Create env + editable install: `uv venv && source .venv/bin/activate && uv pip install -e .[dev]`
- Run CLI locally: `straighten --help`, `straighten generate "a perfectly straight banana"`, `straighten ui`.
- Multi-image CLI example: `straighten generate "blend styles" -i style1.png -i style2.jpg`.
- Tests (fast → full):
  - `uv run pytest tests/test_quick.py -v`
  - `uv run pytest` (requires `GEMINI_API_KEY`)
  - Coverage: `uv run pytest --cov=banana_straightener --cov-report=term-missing`
- Build distribution: `uv run python -m build` (or `python -m build`).

## Coding Style & Naming Conventions
- Python 3.12+ preferred (project supports 3.10+). Use 4‑space indents and type hints for public APIs.
- Formatting: Black (line length 88): `uv run black src/ tests/`.
- Linting: Flake8: `uv run flake8 src/ tests/`.
- Types: Mypy on package: `uv run mypy src/banana_straightener/`.
- Naming: modules/functions/vars `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE_CASE`.

## Testing Guidelines
- Framework: pytest with `pytest.ini` defaults (`python_files = test_*.py`).
- Place new tests under `tests/` and name `test_<feature>.py`.
- Mark or skip slow/API-dependent tests when possible; keep fast unit tests deterministic.
- Provide assertions around confidence/iteration behavior; include minimal fixtures/assets.

## Commit & Pull Request Guidelines
- Commits: short imperative subject (e.g., "Fix image format handling"); group related changes.
- PRs: clear description, rationale, and scope; link issues; include before/after or screenshots for UI.
- Required: passing tests, formatted code, no linter/type errors; update `README.md`/`examples/` if behavior changes.

## Security & Configuration Tips
- Secrets: set `GEMINI_API_KEY` via `.env` or environment; never commit keys.
- Example `.env`: `GEMINI_API_KEY=your-key` (see `README.md` for more options).
- Local artifacts go to `outputs/`; keep large or generated files out of version control.

## Multi-Image Support
- CLI: pass multiple `--image/-i` flags to condition on several images (e.g., `-i img1.png -i img2.jpg`).
- Python API: `agent.straighten(prompt, input_images=[img1, img2])` (legacy `input_image` still supported).
- UI: use the “Starting Images (optional)” uploader; previews show selected images. Recommended max 3 images for best performance.
