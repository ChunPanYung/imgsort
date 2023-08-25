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


def main():
    """main CLI Entry"""
    parser = argparse.ArgumentParser()
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

    args = parser.parse_args()

    # check error on arguments
    _check_args(len(args.PATH), args.summary, (args.include, args.exclude))

    if args.summary:
        # If args.summary is on, sort images on the DESTINATION directory
        lst: list[ImageInfo] = sort_images.sort_info(args.PATH[:], list())
        for node in lst:
            # if int(args.more) < node.get_num():
            print(node)
        sys.exit(EX_OK)

    lst: list[ImageInfo] = sort_images.sort_info(args.PATH[:-1], list())

def _check_args(length: int, summary: bool, size_limit: tuple) -> bool:
    """
    Check whether there's enough argument passed for processing image sort
    also check if there's conflicting argument being passed
    """
    # Require at least 2 position arguments if -d is False
    if not summary and length < 2:
        sys.exit("Please indicates both SRC and DEST directories")
    # Either args.include or args.exclude, can't have both
    if size_limit[0] and size_limit[1]:
        sys.exit("Either --include or --exclude option, cannot have both.")
    return True


if __name__ == "__main__":
    main()
