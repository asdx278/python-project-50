def generate_diff(first_file, second_file, format):
    """Генерирует различия между двумя структурами данных.

    Функция рекурсивно сравнивает две структуры данных (словари)
    и формирует список различий с указанием статуса каждого ключа.
    Поддерживает вложенные структуры и различные типы изменений.

    Args:
        first_file (dict): Первая структура данных для сравнения
        second_file (dict): Вторая структура данных для сравнения
        format (str): Формат вывода результата сравнения
                      (например, 'stylish', 'plain', 'json')

    Returns:
        list: Список словарей с результатами сравнения,
              где каждый элемент содержит ключ, статус
              (added/removed/changed/unchanged/nested)
              и соответствующие значения
    """

    # получаем уникальные ключи из обоих файлов и сортируем их
    UNIQUE_KEYS = sorted(first_file.keys() | second_file.keys())

    def processed_diff(key):
        first_is_dict = isinstance(first_file.get(key), dict)
        second_is_dict = isinstance(second_file.get(key), dict)
        if first_is_dict and second_is_dict:
            return {
                "key": key,
                "status": "nested",
                "children": generate_diff(
                    first_file.get(key),
                    second_file.get(key),
                    format
                )
            }
        if key not in second_file:
            return {
                "key": key,
                "status": "removed",
                "value": first_file.get(key)
            }
        if key not in first_file:
            return {
                "key": key,
                "status": "added",
                "value": second_file.get(key)
            }
        if first_file.get(key) != second_file.get(key):
            return {
                "key": key,
                "status": "changed",
                "old_value": first_file.get(key),
                "new_value": second_file.get(key)
            }
        return {
            "key": key,
            "status": "unchanged",
            "value": first_file.get(key)
        }

    result_diff = list(map(processed_diff, UNIQUE_KEYS))

    return result_diff