#!/usr/bin/env python
"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""
import sys
import argparse
import sort_images
from image_info import ImageInfo
import os
from pathlib import Path
import errno

def main():
    """
    main CLI Entry

    After collecting all images info, it will store it as a list.
    It will run through each function one by one.
    Each function corresponds to one or more argument options,
    it will change list depends on function and what command options is enabled.
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version='%(prog)s 1.2.0'
    )

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
        "--minimum",
        action="store",
        type=int,
        help="Sort only if same size images are at least minimal number given.",
    )

    args: argparse.Namespace = parser.parse_args()

    lst: list[ImageInfo] = []

    if args.summary:
        lst = sort_images.sort_info(args.PATH[:], [])
    elif len(args.PATH[:]) < 2:
        raise argparse.ArgumentTypeError(
            "Need to have 2 paths: Source and destination."
        )
    else:
        lst = sort_images.sort_info(args.PATH[:-1], [])
        # Create directory, throw error if file with same name exists
        try:
            Path(args.PATH[-1]).mkdir(parents=True, exist_ok=True)
        except FileExistsError as error:
            sys.exit(error)

    if args.include and args.exclude:
        print("error: either use -i/--include or -e/--exclude", file=sys.stderr)
        sys.exit(errno.EINVAL)  # Invalid argument error
    elif args.include or args.exclude:
        size_opts: str = args.include if args.include else args.exclude
        lst = sort_images.filter_size(lst, bool(args.include), size_opts)

    if args.minimum:
        lst = sort_images.filter_minimum(lst, args.minimum)

    if args.summary:
        for node in lst:
            print(node)
    else:
        sort_images.sort_execute(lst, args.PATH[-1], args.copy)

    sys.exit(os.EX_OK)


if __name__ == "__main__":
    main()
