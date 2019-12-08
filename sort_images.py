"""
This module will only contain functions that manipulates class ImagePtr
in linked list.
"""
import os
import shutil
from typing import List, Tuple
from pathlib import Path
from PIL import Image

def move_img(files: List[str], destination: str, recursive: bool) -> bool:
    """
    sort all images to the destination directory
    """
    # Create destination directory if not exists
    Path(destination).mkdir(parents=True, exist_ok=True)

    for file in files:
        # get the image width and size
        size: Tuple[int, int] = _is_image(file)
        # sort to destination if it's image
        if size != (0, 0):
            # Create new directory if not exist
            # directory name is all image with the same size
            new_directory: str = os.path.join(destination,
                                              str(size[0]) + 'x' + str(size[1]))
            Path(new_directory).mkdir(parents=True, exist_ok=True)
            # Move images to new directory
            shutil.move(file, new_directory)
        # If file is directory and recursive is True
        elif recursive and os.path.isdir(file):
            # recursively calling its own function with complete file path
            lst_files: List[str] = [os.path.join(file, file_name)
                                    for file_name in os.listdir(file)]
            move_img(lst_files, destination, recursive)
        else:
            print('{}: is not image'.format(file))


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
