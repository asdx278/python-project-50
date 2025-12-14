from pathlib import Path

import pytest

from gendiff.formatters.choice_formatters import choice_formatters
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.read_file import read_file


# Fixtures для ожидаемых результатов
@pytest.fixture
def expected_stylish_simple():
    """Ожидаемый результат в формате stylish для простых файлов."""
    result_path = Path('tests/test_data/result_diff_simple_file.txt')
    return result_path.read_text().strip()


@pytest.fixture
def expected_stylish_nested():
    """Ожидаемый результат в формате stylish для вложенных файлов."""
    result_path = Path('tests/test_data/result_diff_nested_stylish.txt')
    return result_path.read_text().strip()


@pytest.fixture
def expected_plane_simple():
    """Ожидаемый результат в формате plane для простых файлов."""
    result_path = Path('tests/test_data/result_diff_simple_plane.txt')
    return result_path.read_text().strip()


@pytest.fixture
def expected_plane_nested():
    """Ожидаемый результат в формате plane для вложенных файлов."""
    result_path = Path('tests/test_data/result_diff_nested_plane.txt')
    return result_path.read_text().strip()


# Тесты для формата stylish
class TestStylishFormatter:
    """Тесты для форматтера stylish."""

    def test_format_stylish_simple_json(self, expected_stylish_simple):
        """Тест форматирования простых JSON файлов в формате stylish."""
        path1 = 'tests/test_data/file1_simple.json'
        path2 = 'tests/test_data/file2_simple.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'stylish')
        actual = choice_formatters(diff, 'stylish')
        assert actual.strip() == expected_stylish_simple

    def test_format_stylish_simple_yaml(self, expected_stylish_simple):
        """Тест форматирования простых YAML файлов в формате stylish."""
        path1 = 'tests/test_data/file1_simple.yml'
        path2 = 'tests/test_data/file2_simple.yml'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'stylish')
        actual = choice_formatters(diff, 'stylish')
        assert actual.strip() == expected_stylish_simple

    def test_format_stylish_nested_json(self, expected_stylish_nested):
        """Тест форматирования вложенных JSON файлов в формате stylish."""
        path1 = 'tests/test_data/file1_nested.json'
        path2 = 'tests/test_data/file2_nested.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'stylish')
        actual = choice_formatters(diff, 'stylish')
        assert actual.strip() == expected_stylish_nested


# Тесты для формата plane
class TestPlaneFormatter:
    """Тесты для форматтера plane."""

    def test_format_plane_simple_json(self, expected_plane_simple):
        """Тест форматирования простых JSON файлов в формате plane."""
        path1 = 'tests/test_data/file1_simple.json'
        path2 = 'tests/test_data/file2_simple.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'plane')
        actual = choice_formatters(diff, 'plane')
        assert actual.strip() == expected_plane_simple

    def test_format_plane_simple_yaml(self, expected_plane_simple):
        """Тест форматирования простых YAML файлов в формате plane."""
        path1 = 'tests/test_data/file1_simple.yml'
        path2 = 'tests/test_data/file2_simple.yml'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'plane')
        actual = choice_formatters(diff, 'plane')
        assert actual.strip() == expected_plane_simple

    def test_format_plane_nested_json(self, expected_plane_nested):
        """Тест форматирования вложенных JSON файлов в формате plane."""
        path1 = 'tests/test_data/file1_nested.json'
        path2 = 'tests/test_data/file2_nested.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'plane')
        actual = choice_formatters(diff, 'plane')
        assert actual.strip() == expected_plane_nested


# Тесты для формата json
class TestJsonFormatter:
    """Тесты для форматтера json."""

    def test_format_json_simple_json(self):
        """Тест форматирования простых JSON файлов в формате json."""
        path1 = 'tests/test_data/file1_simple.json'
        path2 = 'tests/test_data/file2_simple.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'json')
        actual = choice_formatters(diff, 'json')
        assert isinstance(actual, list)
        assert all(isinstance(item, dict) for item in actual)
        assert all('key' in item and 'status' in item for item in actual)

    def test_format_json_nested_json(self):
        """Тест форматирования вложенных JSON файлов в формате json."""
        path1 = 'tests/test_data/file1_nested.json'
        path2 = 'tests/test_data/file2_nested.json'
        data1 = read_file(path1)
        data2 = read_file(path2)
        diff = generate_diff(data1, data2, 'json')
        actual = choice_formatters(diff, 'json')
        assert isinstance(actual, list)
        assert all(isinstance(item, dict) for item in actual)
        # Проверка структуры вложенных элементов
        nested_items = [
            item for item in actual if item.get('status') == 'nested'
        ]
        for item in nested_items:
            assert 'children' in item
            assert isinstance(item['children'], list)
