"""
This module will only contain functions that manipulates class ImageInfo
in linked list.
"""
import os
from typing import List, Tuple
from PIL import Image
from image_info import ImageInfo
from bool_collection import BoolCollection
from util import create_dir, move_file

def sort_info(file_paths: list[str], current_info: list[ImageInfo]) -> list[ImageInfo]:
    """
    Get images info such as path and size, then sort them into list.
    Return: lst: List[ImageInfo]
    """

    # Cycle through each file
    for _file in file_paths:
        # get the image width and height
        size: Tuple[int, int] = _is_image(_file)
        # do the following if it's image and its size is included
        if size != (0, 0):
            _add_linked_list(current_info, size, _file)
        elif os.path.isdir(_file):
            # Get all file paths within a directory
            sub_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            current_info.append(sort_info(sub_files, current_info))
        # do the following if it's non-image or it cannot read the size
        elif size == (0, 0):
            print(f"{_file} is not a image file.")

    return current_info

# TODO: add --more function here
def sort_img(files: List[str], destination: str, bool_value: BoolCollection,
             limit_size: List[int]) -> bool:
    """
    sort all images to the destination directory
    will recursively calling itself
    """

    for _file in files:
        # get the image width and size
        size: Tuple[int, int] = _is_image(_file)
        # sort to destination if it's image
        if _limit_img(size, bool_value.include, limit_size):
            # Create new directory if not exist
            # directory name is all image with the same size
            new_directory: str = os.path.join(destination, str(size[0]) + 'x' +
                                              str(size[1]))
            create_dir(new_directory)
            move_file(_file, new_directory, bool_value)

        # If file is directory
        elif os.path.isdir(_file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            sort_img(lst_files, destination, bool_value, limit_size)
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
        # if it's directory
        elif os.path.isdir(_file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(_file, file_name)
                                    for file_name in os.listdir(_file)]
            linked_list = summary(linked_list, lst_files, bool_value,
                                  limit_size)
        # do the following if it's non-image or it cannot read the size
        elif size == (0, 0):
            _add_linked_list(linked_list, size, _file)

    return linked_list

def sort_with_more(linked_list: List[ImageInfo], destination: str,
                   bool_value: BoolCollection, limit_size: List[int]) -> bool:
    for node in linked_list:
        if node.num > bool_value.more:
            sort_img(node.paths, destination, bool_value, limit_size)
    return True

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

def _add_linked_list(linked_list: List[ImageInfo], size: Tuple[int, int],
                     _file: str) -> List[ImageInfo]:
    """
    Cycle through List[ImageInfo].  If the image size is already existed in the
    node, increment the node by 1 and add file info into node.
    Otherwise create a new node with image size & path
    """
    added: bool = False
    for node in linked_list:  # Cycle through each node in list
        if node.is_same(size):  # Add img path into node if same size
            node.increment(_file)
            added = True

    # Create new node if it's not added to the current nodes
    if not added:
        linked_list.append(ImageInfo(size[0], size[1], _file))

    return linked_list
