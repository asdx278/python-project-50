import json
import os

import yaml


def normalized_path(path):
    """Нормализует путь к файлу.

    Функция преобразует переданный путь к стандартизированному виду,
    устраняя избыточные разделители, символы '..' и '.',
    приводя его к каноническому формату для текущей операционной системы.

    Args:
        path (str): Путь к файлу (может быть относительным или абсолютным)

    Returns:
        str: Нормализованный путь к файлу
    """
    normalized_file_path = os.path.normpath(path)
    return normalized_file_path


def read_file(file_path):
    """Читает и парсит конфигурационный файл.

    Функция автоматически определяет формат файла (JSON или YAML),
    считывает его содержимое, парсит данные и возвращает словарь
    с отсортированными по алфавиту ключами.

    Args:
        file_path (str): Путь к файлу конфигурации (JSON или YAML).
                         Может быть относительным или абсолютным

    Returns:
        dict: Словарь с данными из файла, отсортированный по ключам

    Raises:
        FileNotFoundError: Если файл не найден по указанному пути
        json.JSONDecodeError: Если JSON некорректен
        yaml.YAMLError: Если YAML некорректен
    """

    if os.path.isabs(file_path):
        abs_path = file_path
    else:
        abs_path = os.path.abspath(normalized_path(file_path))

    if abs_path[-4:] == 'json':
        with open(abs_path, "r", encoding="utf-8") as file:
            file_data = json.load(file)
    else:
        with open(abs_path, "r", encoding="utf-8") as file:
            file_data = yaml.safe_load(file)

    sorted_file_data = {
        key: file_data[key] for key in sorted(file_data)
        }

    return sorted_file_data
