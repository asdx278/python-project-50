import json

def generate_diff(first_file_path, second_file_path):

    with open(first_file_path, "r", encoding="utf-8") as first_file:
        first_file_data = json.load(first_file)

    with open(second_file_path, "r", encoding="utf-8") as second_file:
        second_file_data = json.load(second_file)

