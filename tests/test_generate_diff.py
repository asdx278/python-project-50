from pathlib import Path

import pytest

from gendiff.formatters.choice_formatters import choice_formatters
from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.read_file import read_file


@pytest.fixture
def plain_text():
    result_diff_plane_path = Path('tests/test_data/result_diff_plane.txt')
    result_diff_plane = result_diff_plane_path.read_text()
    return result_diff_plane


def test_generate_diff_plane_json(plain_text):
    path1 = 'tests/test_data/file1.json'
    path2 = 'tests/test_data/file2.json'
    data1 = read_file(path1)
    data2 = read_file(path2)
    diff = generate_diff(data1, data2, 'plane')
    actual = choice_formatters(diff, 'plane')
    assert actual.strip() == plain_text


def test_generate_diff_plane_yaml(plain_text):
    path1 = 'tests/test_data/file1.yml'
    path2 = 'tests/test_data/file2.yml'
    data1 = read_file(path1)
    data2 = read_file(path2)
    diff = generate_diff(data1, data2, 'plane')
    actual = choice_formatters(diff, 'plane')
    assert actual.strip() == plain_text


