import argparse

from gendiff.formatters import format_stylish
from gendiff.modules import generate_diff, read_file


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration "
    "files and shows a difference.")

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="stylish"
    )
    args = parser.parse_args()

    diff = generate_diff(read_file(args.first_file),
                          read_file(args.second_file), args.format)
    formatting = format_stylish(diff)
    print(formatting)


if __name__ == "__main__":
    main()