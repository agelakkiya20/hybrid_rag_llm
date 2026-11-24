.PHONY: install test lint format check clean

install:
	pip install -r requirements-lock.txt

test:
	python -m pytest -v

lint:
	ruff check .

format:
	ruff format .

check: lint test

clean:
	rm -rf .pytest_cache __pycache__