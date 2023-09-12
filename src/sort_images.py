"""
This module will only contain functions that manipulates class ImageInfo
in linked list.
"""
import os
import sys
from PIL import Image
from image_info import ImageInfo
import re
import errno


def sort_info(file_paths: list[str], image_info: list[ImageInfo]) -> list[ImageInfo]:
    """
    Get images info such as path and size, then sort them into list.

    This function will modfiy file_paths: list[str] itself.
    Return: lst: list[ImageInfo]
    """
    # Cycle through each file
    for file in file_paths:
        # get the image width and height
        size: tuple[int, int] = _is_image(file)
        # do the following if it's image and its size is included
        if os.path.isdir(file):
            # Get all file paths within a directory
            sub_files: list[str] = [
                os.path.join(file, file_name) for file_name in os.listdir(file)
            ]
            sort_info(sub_files, image_info)
        elif size != (0, 0):
            _to_list(image_info, size, file)
        else:
            print(f"{file} is not a image file.", file=sys.stderr)

    return image_info


def filter_size(
    image_info: list[ImageInfo], is_include: bool, size_opts: str
) -> list[ImageInfo]:
    """
    Filter images size depending on is_include and size_opts argument.

    If is_include is true, it will only include images that has the same
    width and height as in size_opts.
    If is_include is false, it exclude images that has the same
    width and height as in size_opts.
    """
    try:
        options: list[int] = [int(element) for element in re.split(",|x", size_opts)]
        pair: list[tuple[int, int]] = list(
            zip(options[::2], options[1::2], strict=True)
        )
        # Sort by first, then second element
        pair.sort(key=lambda index: (index[0], index[1]))
        image_info.sort(key=lambda index: (index.width, index.height))

        new_lst: list[ImageInfo] = []  # Create a new list for filtered node

        # Cycle through each element
        # if is_include is true, append the element from current list to new_lst
        # if is_include is false, remove the element from current list
        for node in image_info:
            if is_include:
                if (node.width, node.height) in pair:
                    new_lst.append(node)
            elif (node.width, node.height) not in pair:
                new_lst.append(node)

        # Return new_lst if it is not empty, otherwise return image_info
        return new_lst
    except TypeError as error:
        sys.exit(error)
    except ValueError:
        msg: str = (
            "Check argument string for either --include/-i or --exclude/-e.\n"
            + "It should be in the format of: 10x20,30x40,50x60 etc,\n"
            + "which is [wdith]x[height],[width]x[height],[width]x[height] etc."
        )
        print(msg, file=sys.stderr)
        sys.exit(errno.EINVAL)  # Invalid argument error


def filter_minimum(image_info: list[ImageInfo], minimum: int):
    """
    Compare ImageInfo.num  to minimum:int on each node
    If it is less than minimum, remove from list
    """
    for node in image_info:
        if node.num < minimum:
            image_info.remove(node)

    return image_info


def sort_execute(lst: list[ImageInfo], copy: bool):
    pass


# private function
def _is_image(file: str) -> tuple[int, int]:
    """
    verify whether it's image or not

    Return tuple (img.width, img.height) if yes
    Return emtpy tuple if no
    """
    try:
        with Image.open(file) as img:
            return img.size
    except IOError:
        return (0, 0)


def _to_list(lst: list[ImageInfo], size: tuple[int, int], file: str) -> list[ImageInfo]:
    """
    Cycle through list[ImageInfo].  If the image size is already existed in the
    node, increment the node by 1 and add file info into node.
    Otherwise create a new node with image size & path
    """
    # lst: list[ImageInfo] = linked_list  # reference pointer
    added: bool = False
    for node in lst:  # Cycle through each node in list
        if node.is_same(size):  # Add img path into node if same size
            node.increment(file)
            added = True

    # Create new node if it's not added to the current nodes
    if not added:
        lst.append(ImageInfo(size[0], size[1], file))

    return lst
