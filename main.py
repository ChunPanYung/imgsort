#!/usr/bin/python3

"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""

import argparse
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
    parser.add_argument('-c', '--copy', action='store_true',
                        help='copy instead of move image files')

    # Get all the arguments
    args = parser.parse_args()


    # get all subsequent files depending on 'recursive' options
    sort_images.sort_img(args.SRC, args.DEST, args.recursive, args.copy)


# execute main() function
if __name__ == '__main__':
    main()
