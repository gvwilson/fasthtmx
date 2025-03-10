# FastHTMX Project Guidelines

## Commands
- Run app: `uvicorn app:app --reload`
- Run app (dev): `python app.py`
- Lint: `ruff check .`
- Format: `ruff format .`

## Code Style
- **Imports**: Standard library first, then third-party, then local
- **Type annotations**: Use for all function parameters and return values
- **Naming**: snake_case for variables/functions, PascalCase for classes
- **Docstrings**: Use triple double quotes with concise descriptions
- **HTML/Templates**: Use double quotes for attributes, indent by 2 spaces
- **Error handling**: Use try/except blocks with specific exceptions
- **Max line length**: 88 characters (Black compatible)
- **Async**: Prefer async functions for API endpoints

## Best Practices
- Mount static files explicitly using app.mount()
- Use HTMLResponse for HTML-returning endpoints
- Validate form inputs before processing
- Keep HTML templates semantic and clean