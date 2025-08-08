import json

def generate_diff(first_file_path, second_file_path):
    first_second_diff = ''

    with open(first_file_path, "r", encoding="utf-8") as first_file:
        first_file_data = json.load(first_file)
    sorted_first_file_data = {
        key: first_file_data[key] for key in sorted(first_file_data)
        }

    with open(second_file_path, "r", encoding="utf-8") as second_file:
        second_file_data = json.load(second_file)
    sorted_second_file_data = {
        key: second_file_data[key] for key in sorted(second_file_data)
        }

    for key, value in sorted_first_file_data.items():
        if key in second_file_data and value != second_file_data[key]:
            first_second_diff += f'  - {key}: {value}\n'
            first_second_diff += f'  + {key}: {second_file_data[key]}\n'
        if key not in second_file_data:
            first_second_diff += f'  - {key}: {value}\n'
        if key in second_file_data and value == second_file_data[key]:
            first_second_diff += f'    {key}: {value}\n'

    for key, value in sorted_second_file_data.items():
        if key not in first_file_data:
            first_second_diff += f'  + {key}: {value}\n'

    print(f'{{\n{first_second_diff.lower()}}}')

