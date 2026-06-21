# Repository Guidelines

## Project Structure & Module Organization

`web.py` is the FastAPI entry point. Core code lives in `src/`, with API routes in `src/api/`, compatibility routers in `src/router/`, converters in `src/converter/`, storage backends in `src/storage/`, and control-panel routes in `src/panel/`. Static assets are in `front/`, localized docs are in `docs/`, and deployment files are at the root. Keep defaults in `config.py` and document new environment variables in `.env.example`.

## Build, Test, and Development Commands

- `python -m venv .venv`: create a local environment; activate it with `.venv\Scripts\activate` or `source .venv/bin/activate`.
- `pip install -e ".[dev]"`: install runtime and development tooling from `pyproject.toml`.
- `pip install -r requirements.txt`: install only runtime dependencies.
- `python web.py`: run the local API and panel using `HOST`, `PORT`, and password variables.
- `docker compose up -d`: run the published container with the root Compose file.
- `python -m pytest`: run the pytest suite.
- `python -m black .`, `python -m flake8 .`, and `python -m mypy src config.py web.py log.py`: format, lint, and type-check changes.

## Coding Style & Naming Conventions

Target Python 3.12+ and follow PEP 8 with Black at 100 columns. Use four-space indentation, `snake_case` for modules, functions, and variables, and `PascalCase` for classes. Prefer async FastAPI handlers and Pydantic models where surrounding code already uses them. Keep route-specific logic in the matching router or panel module.

## Testing Guidelines

Pytest is configured in `pyproject.toml` to discover `test_*.py` files, `Test*` classes, and `test_*` functions from the repository root. Add focused tests for new features and converter changes, especially API compatibility and storage behavior. Use `pytest-asyncio` for async code. Check shared-path coverage with `python -m pytest --cov=src`.

## Commit & Pull Request Guidelines

Recent history uses short imperative or descriptive subjects, sometimes with scopes such as `chore:` and `[skip ci]`. Keep the first line concise, for example `Handle empty Claude tool schema`. Pull requests should target `master`, describe behavior changes, list test results, link issues, and update docs when APIs or configuration change.

## Security & Configuration Tips

Never commit real credentials, tokens, OAuth files, or populated `data/creds` content. Start from `.env.example`, keep local secrets in `.env`, and use separate `API_PASSWORD` and `PANEL_PASSWORD` when exposing the service.

## Agent-Specific Instructions

Use UTF-8 by default for text files and command output assumptions. Use Simplified Chinese for contributor-facing explanations, comments, and agent responses unless the surrounding file or user request requires another language.
