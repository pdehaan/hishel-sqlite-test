main:
		uv run main.py

format:
		uvx ruff check --fix
		uvx ruff format