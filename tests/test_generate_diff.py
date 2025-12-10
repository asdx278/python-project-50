from pathlib import Path

import pytest

from gendiff.modules.generate_diff import generate_diff


@pytest.fixture
def plain_text():
    result_diff_plane_path = Path('tests/test_data/result_diff_plane.txt')
    result_diff_plane = result_diff_plane_path.read_text()
    return result_diff_plane


def test_generate_diff_plane_json(plain_text):
    path1 = 'tests/test_data/file1.json'
    path2 = 'tests/test_data/file2.json'
    actual = generate_diff(path1, path2, 'plane')
    assert actual.strip() == plain_text


def test_generate_diff_plane_yaml(plain_text):
    path1 = 'tests/test_data/file1.yml'
    path2 = 'tests/test_data/file2.yml'
    actual = generate_diff(path1, path2, 'plane')
    assert actual.strip() == plain_text


