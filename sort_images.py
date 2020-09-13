"""
This module will only contain functions that manipulates class ImageInfo
in linked list.
"""
import os
import sys
import shutil
from typing import List, Tuple
from PIL import Image
from image_info import ImageInfo
from bool_collection import BoolCollection
from util import create_dir


def sort_img(files: List[str], destination: str, bool_value: BoolCollection,
             limit_size: List[int]) -> bool:
    """
    sort all images to the destination directory
    will recursively calling itself if -r option is true
    """

    for _file in files:
        # get the image width and size
        size: Tuple[int, int] = _is_image(_file)
        # sort to destination if it's image
        if _limit_img(size, bool_value.include, limit_size):
            # Create new directory if not exist
            # directory name is all image with the same size
            new_directory: str = os.path.join(destination,
                                              str(size[0]) + 'x' +
                                              str(size[1]))
            create_dir(new_directory)
            _try_sort(_file, new_directory, bool_value)

        # If file is directory and recursive is True
        elif bool_value.recursive and os.path.isdir(_file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            sort_img(lst_files, destination, bool_value, limit_size)
        # if file is non-directory or image, and bool_value.unknown is true
        elif bool_value.unknown and not os.path.isdir(_file):
            # create a new directory if not exist
            # directory name is always 'unknown' for all unreadable
            # and unknown images
            new_directory: str = os.path.join(destination, 'unknown')
            _try_sort(_file, new_directory, bool_value)

    return True


def summary(linked_list: List[ImageInfo], files: List[str],
            bool_value: BoolCollection,
            limit_size: List[int]) -> List[ImageInfo]:
    """
    summaries the number of images and image size that's moved/copied
    Return: lst: List[ImageInfo]
    """

    # Cycle through each file
    for _file in files:
        # get the image width and height
        size: Tuple[int, int] = _is_image(_file)
        # do the following if it's image and its size is included
        if _limit_img(size, bool_value.include, limit_size):
            _add_linked_list(linked_list, size, _file)
        # if it's directory and recursive is on:
        elif bool_value.recursive and os.path.isdir(_file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            linked_list = summary(linked_list, lst_files, bool_value,
                                  limit_size)
        # do the following if it's non-image and --unknown option is flaged
        elif size == (0, 0) and bool_value.unknown:
            _add_linked_list(linked_list, size, _file)

    return linked_list


def unknown_only(result: ImageInfo, src: List[str], dest: str, _summary: bool,
                 bool_value: BoolCollection) -> List[int]:
    """ Sort unknown images only.
        Depends on whether --recursive, --verbose, --summary is active or not.
        All path is treat as source if --summary is active.
        Exclude directory.

        Args result: [0] is total number of non-image files,
                  [1] is total file size.
        return List: [0] is total number of non-image files,
                      [1] is total file size.
        If the return Tuple is [0, 0], it means no non-image files, or
        --summary is off.
    """
    # cycle through each source
    for _file in src:
        # if it's directory and recursive is on
        if os.path.isdir(_file) and bool_value.recursive:
            # recrusively calling itself with complete file path
            # and content of directory
            lst_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            result = unknown_only(result, lst_files, dest, _summary, bool_value)
        # if file is not image or directory
        elif _is_image(_file) == (0, 0) and not os.path.isdir(_file):
            # Add all file size together and number of non-image file
            # if summary option is on.
            if _summary:
                result.increment(_file)
            else:
                _try_sort(_file, dest, bool_value)

    return result


# private function
def _is_image(_file: str) -> Tuple[int, int]:
    """
    verify whether it's image or not

    Return Tuple (img.width, img.height) if yes
    Return emtpy Tuple if no
    """
    try:
        with Image.open(_file) as img:
            return img.size
    except IOError:
        return (0, 0)


def _limit_img(img_size: Tuple[int, int], include: bool,
               limit_size: List[int]) -> bool:
    """
    Return False if img_size is (0, 0)
    Return True if img_size is in included size
    Return False if it's excluded size
    Othersie return True
    """
    # Return False if img_size is (0, 0)
    if img_size == (0, 0):
        return False
    # if limit_size is not empty, it means either include args or exclude
    # args is true
    if limit_size:
        # Return True if include is True and img_size is in included size
        if include:
            for i, j in zip(limit_size[0::2], limit_size[1::2]):
                if img_size[0] == i and img_size[1] == j:
                    return True
            # return false if it's not included size
            return False

        # Return False if it's excluded size
        for i, j in zip(limit_size[0::2], limit_size[1::2]):
            if img_size[0] == i and img_size[1] == j:
                return False
        # return True if it's not excluded size
        return True

    # Otherwise return True
    return True


def _try_sort(_file: str, new_directory: str, bool_value: BoolCollection):
    """
    attempt to either copy or move file(s) to new directory(s)
    output error if file with same name exists
    """
    try:
        if bool_value.copy:
            shutil.copy(_file, new_directory)
            if bool_value.verbose:
                print('COPY: "{}"\nTO:   "{}"'.format(_file, new_directory))
        else:
            shutil.move(_file, new_directory)
            if bool_value.verbose:
                print('MOVE: "{}"\nTO:   "{}"'.format(_file, new_directory))
    except shutil.Error as error:
        # output error only if unknown sorting option is false
        if not bool_value.unknown:
            print('{0}'.format(error), file=sys.stderr)


def _add_linked_list(linked_list: List[ImageInfo], size: Tuple[int],
                     _file: str) -> List[ImageInfo]:
    added: bool = False
    for node in linked_list:  # Cycle through each node in list
        if node.is_same(size):  # Add img path into node if same size
            node.increment(_file)
            added = True

    # Create new node if it's not added to the current nodes
    if not added:
        linked_list.append(ImageInfo(size[0], size[1], _file))

    return linked_list
