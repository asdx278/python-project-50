def to_str(value, depth):
    """Преобразует значение в строку с учетом типа."""
    if isinstance(value, dict):
        lines = []
        indent = ' ' * (depth * 4)
        lines.append('{')
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {to_str(v, depth + 1)}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    return str(value).lower() if isinstance(value, bool) else str(value)


def iter_(current_tree, depth):
    """Рекурсивно обходит дерево различий и формирует строки."""
    indent = ' ' * (depth * 4 - 2)
    lines = []

    for node in current_tree:
        key = node["key"]
        status = node["status"]

        if status == "nested":
            lines.append(f"{indent}  {key}: {{")
            lines.append(iter_(node["children"], depth + 1))
            lines.append(f"{indent}  }}")
        elif status == "added":
            value = to_str(node["value"], depth)
            lines.append(f"{indent}+ {key}: {value}")
        elif status == "removed":
            value = to_str(node["value"], depth)
            lines.append(f"{indent}- {key}: {value}")
        elif status == "changed":
            old_value = to_str(node["old_value"], depth)
            new_value = to_str(node["new_value"], depth)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")
        elif status == "unchanged":
            value = to_str(node["value"], depth)
            lines.append(f"{indent}  {key}: {value}")

    return '\n'.join(lines)


def format_stylish(tree):
    """Форматирует различия в стиле "stylish".

    Функция принимает древовидную структуру различий и
    преобразует её в строковое представление с отступами
    и символами, обозначающими тип изменений.

    Args:
        tree (list): Древовидная структура различий,
                     полученная из функции generate_diff
    Returns:
        str: Отформатированная строка с различиями
    """
    result = iter_(tree, 1)
    return f"{{\n{result}\n}}"
