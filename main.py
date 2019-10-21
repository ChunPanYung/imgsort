#!/usr/bin/python3

"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""

import sys
import os
import argparse
from typing import List
from PIL import Image
from sorted_images import dry_run


def main():
    """
    Parse all command line options
    """
    parser = argparse.ArgumentParser()
    # Add positional arguments
    parser.add_argument('SRC', help='Directory that contains unsorted images')
    # Optional positional arguments
    parser.add_argument('DEST', nargs='?', default=os.getcwd(),
                        help='''Destination directory that will contain sorted images.
                                If not provided, use current directory.''')
    # Add optional arguments
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Output all sorted images and error')

    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='Simulate the image sorting without actual action.',)

    # Get all the arguments
    args = parser.parse_args()

    # Early exit if there's no SRC
    if not args.SRC:
        print("Please indicate both SRC directory.")
        sys.exit()

    # Get absolute path for following variables
    SRC = os.path.abspath(args.SRC)
    DEST = os.path.abspath(args.DEST)

    lst: List = dry_run(SRC)


# execute main() function
if __name__ == '__main__':
    main()
