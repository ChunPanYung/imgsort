"""
This module is mainly used for handling command line arguments,
and decided which function to call based on arguments.
"""
import sys
import argparse
import re
from typing import List, Tuple
import sort_images
from image_info import ImageInfo
from bool_collection import BoolCollection
import util


def main():
    """ main CLI Entry """
    parser = argparse.ArgumentParser()
    # Add positional arguments
    parser.add_argument('PATH', nargs='+',
                        help='''Provides Source Directory(s) and Destination
                                Directory for image sorting.  If --summary is
                                given, only needed Source Directory(s).''')

    # Add optional arguments
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='Get all images from subsequent directories.')
    parser.add_argument('-c', '--copy', action='store_true',
                        help='Copy instead of move image files.')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print detail information.')
    parser.add_argument('-s', '--summary', action='store_true',
                        help='Simulate the run, no file will be moved/copied.')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help='Same as --summary option.')
    parser.add_argument('-i', '--include', action='store', type=str,
                        help='''Sorting only certain size indicated by
                                this option.''')
    parser.add_argument('-e', '--exclude', action='store', type=str,
                        help='''Exclude certain image size indicated by
                                this option.''')
    parser.add_argument('-m', '--more', action='store', type=int,
                        help='''Sort only if image of said size is more than
                                X number.''')
    parser.add_argument('--unknown', action='store_true',
                        help='Sort all unknown/unreadable images into folder.')
    parser.add_argument('--unknownonly', action='store_true',
                        help='Sort only unknown/unreadable images only.')

    args = parser.parse_args()


    # Putting all boolean args into one bundle
    bool_value: BoolCollection = BoolCollection(args.recursive, args.copy,
                                                args.verbose, args.unknown,
                                                args.more, bool(args.include))


    # check error on arguments
    _check_error(len(args.PATH), args.summary, (args.include, args.exclude),
                 (args.unknown, args.unknownonly))

    # flag --summary if --dry-run is flaged
    if args.dry_run:
        args.summary = args.dry_run

    # Create destination directory if not exists
    if not args.summary:
        util.create_dir(args.PATH[-1])


    # get the args.include or args.exclude value
    limit_size: List[int] = [int(num) for num in
                             re.split('[x,]', str(args.include or '') +
                                      str(args.exclude or ''))]


    # process image sorting functionality separately if --unknownonly option
    # is on.
    # it will process whethere --summary option is on or off
    if args.unknownonly:
        # src and dest will change depends on flag args.summary
        src: str = args.PATH[:-1] if not args.summary else args.PATH
        dest: str = args.PATH[-1] if not args.summary else ''
        result: List[int] = sort_images.unknown_only([0, 0], src, dest,
                                                     args.summary,
                                                     bool_value)
        # print out info if --summary is flaged
        if args.summary:
            # if --more option is flaged
            if not args.more:
                print('-Total numbers: {}'.format(result[0]))
                print('-Total size: {}\n'.format(util.sizeof_fmt(result[1])))
            elif args.more < result[0]:
                print('-Total numbers: {}'.format(result[0]))
                print('-Total size: {}\n'.format(util.sizeof_fmt(result[1])))
    # If summary arguments is true, no actual images is sorted
    elif args.summary:
        lst: List[ImageInfo] = []
        lst = sort_images.summary(lst, args.PATH, bool_value, limit_size)
        if not lst:
            print('''No image files found!  Maybe using it with --recursive
                     option?''')
        else:
            print('\n===SUMMARY===')
            for node in lst:
                # if --more option is not on
                if not args.more:
                    node.to_string()
                # otherwise print on-screen only if image total is more than
                # the said flag
                elif args.more < node.get_num():
                    node.to_string()
    else:
        sort_images.sort_img(args.PATH[:-1], args.PATH[-1], bool_value,
                             limit_size)

    # end of main()


def  _check_error(length: int, summary: bool, size_limit: Tuple,
                  unknown_tup: Tuple) -> bool:
    """
    Check whether there's enough argument passed for processing image sort
    also check if there's conflicting argument being passed
    """
    # Require at least 2 position arguments if -d is False
    if not summary and length < 2:
        sys.exit('Please indicates both SRC and DEST directories')
    # Either args.include or args.exclude, can't have both
    if size_limit[0] and size_limit[1]:
        sys.exit('Either --include or --exclude option, cannot have both.')
    # Either args.unknown or args.unknownonly
    if unknown_tup[0] and unknown_tup[1]:
        sys.exit('Either --unknown or --unknownonly option, cannot have both.')


    return True


if __name__ == '__main__':
    main()
