"""
This module will only contain functions that manipulates class ImagePtr
in linked list.
"""
import os
import sys
import shutil
from typing import List, Tuple
from pathlib import Path
from PIL import Image
from image_ptr import ImagePtr
from bool_collection import BoolCollection

def sort_img(files: List[str], destination: str, bool_value: BoolCollection,
             limit_size: List[int]) -> bool:
    """
    sort all images to the destination directory
    """

    for file in files:
        # get the image width and size
        size: Tuple[int, int] = _is_image(file)
        # sort to destination if it's image
        if _limit_img(size, BoolCollection.include, limit_size):
            # Create new directory if not exist
            # directory name is all image with the same size
            new_directory: str = os.path.join(destination,
                                              str(size[0]) + 'x' + str(size[1]))
            create_dir(new_directory)
            # Move or copy images to new directory
            # output error if file with same name exists
            try:
                if bool_value.copy:
                    shutil.copy(file, new_directory)
                    if bool_value.verbose:
                        print('COPY: "{}"\nTO:   "{}"'.format(file, new_directory))
                else:
                    shutil.move(file, new_directory)
                    if bool_value.verbose:
                        print('MOVE: "{}"\nTO:   "{}"'.format(file, new_directory))
            except shutil.Error as error:
                print('{0}'.format(error), file=sys.stderr)

        # If file is directory and recursive is True
        elif bool_value.recursive and os.path.isdir(file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(file, file_name)
                                    for file_name in os.listdir(file)]
            sort_img(lst_files, destination, bool_value, limit_size)

    return True


def dry_run(linked_list: List[ImagePtr], files: List[str],
            recursive: bool, limit_size: List[int]) -> List[ImagePtr]:
    """

    summaries the number of images and image size that's moved/copied

    Return: lst: List[ImagePtr]
    """

    # Cycle through each file
    for file in files:
        # get the image width and height
        img_size: Tuple[int, int] = _is_image(file)
        # do the following if it's image
        if img_size != (0, 0):
            added: bool = False
            for node in linked_list: # Cycle through each node in list
                if node.is_same(img_size): # Add img path into node if same size
                    node.increment(os.path.getsize(file))
                    added = True

            # Create new node if it's not added to the current nodes
            if not added:
                linked_list.append(ImagePtr(img_size[0], img_size[1], file))
        # if it's directory and recursive is on:
        elif recursive and os.path.isdir(file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(file, file_name)
                                    for file_name in os.listdir(file)]
            linked_list = dry_run(linked_list, lst_files, recursive, limit_size)

    return linked_list


def create_dir(directory: str) -> bool:
    """
        Create from directory:str
        It will create parent directory if it doesn't exist.
        It won't throw Exception if directory already exists.
    """
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
    except FileExistsError as error:
        sys.exit(error)

    return True


# private function
def _is_image(file: str) -> Tuple[int, int]:
    """
    verify whether it's image or not

    Return Tuple (img.width, img.height) if yes
    Return emtpy Tuple if no
    """
    try:
        with Image.open(file) as img:
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
    elif limit_size:
        # Return True if include is True and img_size is in included size
        if include:
            for i, j in zip(limit_size[0::2], limit_size[1::2]):
                if img_size[0] == i and img_size[1] == j:
                    return True
            # return false if it's not included size
            return False
        # Return False if it's excluded size
        else:
            for i, j in zip(limit_size[0::2], limit_size[1::2]):
                if img_size[0] == i and img_size[1] == j:
                    return False
            # return True if it's not excluded size
            return True
        
    # Otherwise return True
    return True
