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
                        help='image file(s)')
    parser.add_argument('DEST',
                        help='destination folder for sorted images')

    # Add optional arguments
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='get all images from subsequent directories')

    # Get all the arguments
    args = parser.parse_args()


    lst: List[str] = []

    # get all subsequent files depending on 'recursive' options
    lst = sort_images.list_img(args.recursive, args.SRC)

    print(lst)


# execute main() function
if __name__ == '__main__':
    main()
