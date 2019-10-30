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
import sort_images


def main():
    """
    Parse all command line options
    """
    parser = argparse.ArgumentParser()
    # Add positional arguments
    parser.add_argument('SRC', nargs='+',
                        help='Directory that contains unsorted images')
    # Optional positional arguments

    # Add optional arguments
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Output all sorted images and error')

    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='Simulate the image sorting without actual action.',)
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Get all images from subsequent directories')

    # Get all the arguments
    args = parser.parse_args()

    # Early exit if there's no SRC
    if not args.SRC:
        print("Please indicate both SRC directory.")
        sys.exit()

    lst: List[str] = []

    # get all subsequent files depending on 'recursive' options
    lst = sort_images.list_img(args.recursive, args.SRC)



    # process according to optional arguments
    #lst = list_img(args.recursive, args.SRC)



    #lst: List = dry_run(SRC)


# execute main() function
if __name__ == '__main__':
    main()
