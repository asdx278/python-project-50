from gendiff.formatters.stylish import format_stylish


def choice_formatters(diff, format_name):
    if format_name == 'stylish':
        return format_stylish(diff)
    # Additional formatters can be added here
    raise ValueError(f"Unknown format: {format_name}")