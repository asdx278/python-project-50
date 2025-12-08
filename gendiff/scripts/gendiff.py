import argparse

from gendiff.modules.generate_diff import generate_diff
from gendiff.modules.read_file import read_file


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

    diff = generate_diff(read_file(args.first_file), read_file(args.second_file), args.format)
    print(diff)


if __name__ == "__main__":
    main()