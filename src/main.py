#!/usr/bin/env python
"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""
import sys
import argparse
import sort_images
from image_info import ImageInfo
from os import EX_OK
from pathlib import Path
import errno


def main():
    """main CLI Entry"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    # Add positional arguments
    parser.add_argument(
        "PATH",
        nargs="+",
        help="""Provides Source Directory(s) and Destination
            Directory for image sorting.  If --summary is
            given, only needed Source Directory(s).""",
    )

    # Add optional arguments
    parser.add_argument(
        "-c", "--copy", action="store_true", help="Copy instead of move image files."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Print detail information."
    )
    parser.add_argument(
        "-s",
        "--summary",
        action="store_true",
        help="Simulate the run, no file will be moved/copied.",
    )
    parser.add_argument(
        "-i",
        "--include",
        action="store",
        type=str,
        help="Sorting only certain size indicated by this option.",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        action="store",
        type=str,
        help="Exclude certain image size indicated by this option.",
    )
    parser.add_argument(
        "-m",
        "--more",
        action="store",
        type=int,
        help="Sort only if image of said size is more than X number.",
    )

    args: argparse.Namespace = parser.parse_args()

    lst: list[ImageInfo] = []

    if args.summary:
        lst = sort_images.sort_info(args.PATH[:], [])
    else:
        lst = sort_images.sort_info(args.PATH[:-1], [])
        # Create directory, throw error if file with same name exists
        try:
            Path(args.PATH[-1]).mkdir(parents=True, exist_ok=True)
        except FileExistsError as error:
            sys.exit(error)


    # First by first, then second element
    lst.sort(key=lambda index: (index.get_width(), index.get_height()))

    if args.include and args.exclude:
        print("error: either use -i/--include or -e/--exclude", file=sys.stderr)
        sys.exit(errno.EINVAL)  # Invalid argument error
    elif args.include or args.exclude:
        size_opts: str = args.include if args.include else args.exclude
        sort_images.filter_size(lst, bool(args.include), size_opts)

    # DEBUG
    if args.summary:
        for node in lst:
            print(node)

    sys.exit(EX_OK)


if __name__ == "__main__":
    main()
