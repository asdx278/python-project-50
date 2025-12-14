import argparse

from gendiff.formatters import choice_formatters
from gendiff.modules import generate_diff


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

    diff = generate_diff(args.first_file, args.second_file, args.format)
    current_diff = choice_formatters(diff, args.format)
    print(current_diff)


if __name__ == "__main__":
    main()