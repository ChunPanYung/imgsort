#!/usr/bin/python3

"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""

import sys
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
    parser.add_argument('PATH', nargs='+',
                        help='''Provides Source Directory(s) and Destination
                                Directory for image sorting.  If --dry_run is
                                given, only needed Source Directory(s).''')

    # Add optional arguments
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='get all images from subsequent directories')
    parser.add_argument('-c', '--copy', action='store_true',
                        help='copy instead of move image files')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='print detail information')
    parser.add_argument('-d', '--dry_run', action='store_true',
                        help='simulate the execution, no file will be moved/copied')
    parser.add_argument('-i', '--include', action='store', type=str,
                        help='sorting only certain size indicated by this argument')
    parser.add_argument('-e', '--exclude', action='store', type=str,
                        help='exclude certain image sizes indicated by this argument')

    # Get all the arguments
    args = parser.parse_args()

    # Requier at least 2 position arguments if -d is False
    if not args.dry_run and len(args.PATH) < 2:
        sys.exit('Please indicates both SRC and DEST directories')

    # Create destination directory if not exists and dry_run is False
    if not args.dry_run:
        sort_images.create_dir(args.PATH[-1])
        if args.verbose:
            print('{}: is created.\n'.format(args.PATH[-1]))

    # If dry_run arguments is true, no actual images is sorted
    if args.dry_run:
        lst: List[ImagePtr] = []
        lst = sort_images.dry_run(lst, args.PATH, args.recursive)
        for node in lst:
            node.to_string()
    else:
        sort_images.sort_img(args.PATH[:-1], args.PATH[-1], args.recursive,
                             args.copy, args.verbose)


# execute main() function
if __name__ == '__main__':
    main()
