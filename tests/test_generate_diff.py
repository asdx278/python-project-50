import os

from gendiff.modules.generate_diff import generate_diff
'tests/test_data/result.txt'

def test_generate_diff_basic():
    expected = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""
    path1 = 'tests/test_data/file1.json'
    path2 = 'tests/test_data/file2.json'
    actual = generate_diff(path1, path2)
    assert actual.strip() == expected.strip()