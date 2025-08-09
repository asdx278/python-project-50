install:
	uv sync

gendiff-plane-files:
	uv run gendiff tests/test_data/file1.json tests/test_data/file2.json

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml