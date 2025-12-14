import json

from gendiff.formatters.plane import format_plane
from gendiff.formatters.stylish import format_stylish


def choice_formatters(diff, format_name):
    if format_name == 'stylish':
        return format_stylish(diff)
    elif format_name == 'plain':
        return format_plane(diff)
    elif format_name == 'json':
        return json.dumps(diff)
    raise ValueError(f"Unknown format: {format_name}")