install:
	uv sync

gendiff-plane-files:
	uv run gendiff gendiff/file1.json gendiff/file2.json

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl

lint:
	uv run ruff check gendiff