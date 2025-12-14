def generate_diff(first_file, second_file, format='stylish'):
    """Генерирует различия между двумя файлами конфигурации.

    Функция принимает пути к файлам, читает и парсит их,
    затем рекурсивно сравнивает структуры данных и формирует
    список различий с указанием статуса каждого ключа.
    Поддерживает вложенные структуры и различные типы изменений.

    Args:
        first_file (str): Путь к первому файлу конфигурации
        second_file (str): Путь к второму файлу конфигурации
        format (str): Формат вывода результата сравнения
                      (например, 'stylish', 'plain', 'json')

    Returns:
        list: Список словарей с результатами сравнения,
              где каждый элемент содержит ключ, статус
              (added/removed/changed/unchanged/nested)
              и соответствующие значения
    """
    from gendiff.modules.read_file import read_file

    # Читаем и парсим файлы
    first_data = read_file(first_file)
    second_data = read_file(second_file)

    return build_diff(first_data, second_data)


def build_diff(first_data, second_data):
    """Строит дерево различий между двумя структурами данных.

    Args:
        first_data (dict): Первая структура данных
        second_data (dict): Вторая структура данных

    Returns:
        list: Список различий
    """
    # получаем уникальные ключи из обоих файлов и сортируем их
    UNIQUE_KEYS = sorted(first_data.keys() | second_data.keys())

    def processed_diff(key):
        first_is_dict = isinstance(first_data.get(key), dict)
        second_is_dict = isinstance(second_data.get(key), dict)
        if first_is_dict and second_is_dict:
            return {
                "key": key,
                "status": "nested",
                "children": build_diff(
                    first_data.get(key),
                    second_data.get(key)
                )
            }
        if key not in second_data:
            return {
                "key": key,
                "status": "removed",
                "value": first_data.get(key)
            }
        if key not in first_data:
            return {
                "key": key,
                "status": "added",
                "value": second_data.get(key)
            }
        if first_data.get(key) != second_data.get(key):
            return {
                "key": key,
                "status": "changed",
                "old_value": first_data.get(key),
                "new_value": second_data.get(key)
            }
        return {
            "key": key,
            "status": "unchanged",
            "value": first_data.get(key)
        }

    result_diff = list(map(processed_diff, UNIQUE_KEYS))

    return result_diff
