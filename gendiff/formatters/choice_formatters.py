from gendiff.formatters.plane import format_plane
from gendiff.formatters.stylish import format_stylish


def choice_formatters(diff, format_name):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plane':
        return format_plane(diff)
    # Additional formatters can be added here
    raise ValueError(f"Unknown format: {format_name}")