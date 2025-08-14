from gendiff.modules.read_file import read_file


def generate_diff(first_file_path, second_file_path):
    """Функция сравнения двух плоских файлов в формате json"""

    first_second_diff = ''

    first_file = read_file(first_file_path)
    second_file = read_file(second_file_path)

    for key, value in first_file.items():
        if key in second_file and value != second_file[key]:
            first_second_diff += f'  - {key}: {value}\n'
            first_second_diff += f'  + {key}: {second_file[key]}\n'
        if key not in second_file:
            first_second_diff += f'  - {key}: {value}\n'
        if key in second_file and value == second_file[key]:
            first_second_diff += f'    {key}: {value}\n'

    for key, value in second_file.items():
        if key not in first_file:
            first_second_diff += f'  + {key}: {value}\n'

    return f'{{\n{first_second_diff.lower()}}}'

