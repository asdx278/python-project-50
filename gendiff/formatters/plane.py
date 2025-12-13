def to_str(value):
    """Преобразует значение в строковое представление для булевых значений,
    чисел и NULL"""
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return str(value)
    if isinstance(value, dict):
        return "[complex value]"
    # Строковые значения оборачиваем в одинарные кавычки
    return f"'{value}'"


def iter_(tree, path=""):
    lines = []
    for node in tree:
        key = node["key"]
        status = node["status"]
        current_path = f"{path}.{key}" if path else key

        if status == "added":
            value = to_str(node["value"])
            lines.append(
                f"Property '{current_path}' was added with value: {value}"
            )
        elif status == "removed":
            lines.append(f"Property '{current_path}' was removed")
        elif status == "changed":
            old_value = to_str(node["old_value"])
            new_value = to_str(node["new_value"])
            lines.append(
                f"Property '{current_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif status == "nested":
            child_lines = iter_(node["children"], current_path)
            lines.append(child_lines)
    return "\n".join(lines)


def format_plane(tree):
    """Форматирует различия в стиле "plain".

    Функция принимает древовидную структуру различий и
    преобразует её в строковое представление, подходящее
    для простого текстового вывода.

    Args:
        tree (list): Древовидная структура различий,
                     полученная из функции generate_diff
    Returns:
        str: Отформатированная строка с различиями
    """
    result = iter_(tree)
    return result
