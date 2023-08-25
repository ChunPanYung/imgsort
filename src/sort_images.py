"""
This module will only contain functions that manipulates class ImageInfo
in linked list.
"""
import os
from PIL import Image
from image_info import ImageInfo


def sort_info(file_paths: list[str], current_info: list[ImageInfo]) -> list[ImageInfo]:
    """
    Get images info such as path and size, then sort them into list.
    Return: lst: list[ImageInfo]
    """
    # current_info: list[ImageInfo] = current_info  # reference pointer
    # Cycle through each file
    for _file in file_paths:
        print(_file)
        # get the image width and height
        size: tuple[int, int] = _is_image(_file)
        # do the following if it's image and its size is included
        if os.path.isdir(_file):
            # Get all file paths within a directory
            sub_files: list[str] = [
                os.path.join(_file, file_name) for file_name in os.listdir(_file)
            ]
            sort_info(sub_files, current_info)
        elif size != (0, 0):
            _to_list(current_info, size, _file)

    return current_info


# private function
def _is_image(_file: str) -> tuple[int, int]:
    """
    verify whether it's image or not

    Return tuple (img.width, img.height) if yes
    Return emtpy tuple if no
    """
    try:
        with Image.open(_file) as img:
            return img.size
    except IOError:
        print(f"{_file} is not a image file.")
        return (0, 0)


def _to_list(
    lst: list[ImageInfo], size: tuple[int, int], _file: str
) -> list[ImageInfo]:
    """
    Cycle through list[ImageInfo].  If the image size is already existed in the
    node, increment the node by 1 and add file info into node.
    Otherwise create a new node with image size & path
    """
    # lst: list[ImageInfo] = linked_list  # reference pointer
    added: bool = False
    for node in lst:  # Cycle through each node in list
        if node.is_same(size):  # Add img path into node if same size
            node.increment(_file)
            added = True

    # Create new node if it's not added to the current nodes
    if not added:
        lst.append(ImageInfo(size[0], size[1], _file))

    return lst
