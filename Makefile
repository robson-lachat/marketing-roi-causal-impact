# Variables to simplify maintenance
PYTHON = poetry run python
RUFF = poetry run ruff

.PHONY: install load analyze lint format check clean help

# Default target when you run 'make' without arguments
help:
	@echo "Available commands:"
	@echo "  make install  - Installs dependencies via Poetry"
	@echo "  make load     - Runs the data load pipeline (SQL -> DuckDB)"
	@echo "  make analyze  - Runs LTV and Causal Impact analysis"
	@echo "  make lint     - Runs Ruff to check style and errors"
	@echo "  make format   - Automatically formats code with Ruff"
	@echo "  make check    - Runs FORMAT, LOAD and ANALYZE in sequence"
	@echo "  make clean    - Removes the database and temporary files"

install:
	poetry install

load:
	$(PYTHON) src/load_data.py

analyze:
	$(PYTHON) src/analysis.py

lint:
	$(RUFF) check .

format:
	$(RUFF) check --fix .
	$(RUFF) format .

check: format load analyze

clean:
	rm -f database.duckdb
	rm -rf outputs/*.png
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "🧹 Environment cleaned successfully."