import json
import os


def normalized_path(path):
    """Функция принимает путь и нормализует его до абсолютного"""
    normalized_file_path = os.path.normpath(path)
    return normalized_file_path


def read_file(file_path):
    """Функция читает файл по переданному абсолютному пути"""

    if os.path.isabs(file_path):
        abs_path = file_path
    else:
        abs_path = os.path.abspath(normalized_path(file_path))

    with open(abs_path, "r", encoding="utf-8") as file:
        file_data = json.load(file)
    sorted_file_data = {
        key: file_data[key] for key in sorted(file_data)
        }

    return sorted_file_data
