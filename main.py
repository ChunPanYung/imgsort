#!/usr/bin/python3

"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""

import os
import argparse
from typing import List
import sort_images
from image_ptr import ImagePtr

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
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print detail information')
    parser.add_argument('-d', '--dry_run', action='store_true',
                        help='simulate the execution, no file will be moved/copied')

    # Get all the arguments
    args = parser.parse_args()

    # Create destination directory if not exists and dry_run is False
    if not args.dry_run:
        sort_images.create_dir(args.DEST)
        if args.verbose:
            print('{}: is created.\n'.format(args.DEST))
    elif os.path.exists(args.DEST) and not os.path.isdir(args.DEST):
        print('{}: cannot be created!\n'.format(args.DEST))
    else:
        print('{}: can be create!\n'.format(args.DEST))


    if args.dry_run:
        linked_list: List[ImagePtr] = []
        sort_images.dry_run(linked_list, args.SRC, args.recursive)
    else:
        sort_images.sort_img(args.SRC, args.DEST, args.recursive, args.copy,
                             args.verbose)


# execute main() function
if __name__ == '__main__':
    main()
