"""
This module will only contain functions that manipulates class ImagePtr
in linked list.
"""
import os
from typing import List, Tuple
from PIL import Image
from image_ptr import ImagePtr

def list_img(recursive: bool, files: List[str]) -> List[str]:
    """
    Return a list of all images file
    """
    lst: List[str] = []
    # list all files in directory, get its absolute path
    for file in files:
        if _is_image(file): # add into lst if it's image
            lst[:0] = [file]
        elif recursive and os.path.isdir(file):
            # join the directory path with file name, then put it in list
            lst_files: List[str] = [os.path.join(file, file_name)
                                    for file_name in os.listdir(file)]
            lst[:0] = list_img(recursive, lst_files)

    return lst




def dry_run(directory) -> List[ImagePtr]:
    """
    sort images by height and width

    Return: lst: List[ImagePtr]
    """

    # Contains list of object ImagePtr, with each object contains images
    # who has the same width and height
    lst: List[ImagePtr] = []

    # list all files in directory, get its absolute path
    files: List[str] = [f for f in os.listdir(directory)
                        if os.path.isfile(os.path.join(directory, f))]

    # Cycle through each file
    for file in files:
        file = os.path.join(directory, file) # get the full path
        # Check to see whether it can grab img width and height
        img_size: Tuple = _is_image(file)

        if img_size: # If it can, do the following:
            added: bool = False
            for node in lst: # Cycle through each node in list
                if node.is_same(img_size): # Add img path into node if same size
                    node.add_to_path(file)
                    added = True
            # Create new node if it's not added to the current nodes
            if not added:
                lst.append(ImagePtr(img_size[0], img_size[1], file))

    print_all(lst)
    return lst

def print_all(lst: List[ImagePtr]) -> bool:
    """
    Private Function
    Print information about sorted images (by width and height)
    Return False if there's ImagePtr._lst is empty
    """
    if not lst:
        print("No image is being sorted into folder.")
        return False

    # print all sorted images and its related information
    for node in lst:
        # print sorted image size and all its related location
        print('Image Size: {}x{}'.format(node.width, node.height))
        # For every object, print all strings in List: node.path
        for location in node.path:
            print('| ', location)
    return True

# private function
def _is_image(file: str) -> Tuple:
    """
    verify whether it's image or not

    Return Tuple (img.width, img.height) if yes
    Return emtpy Tuple if no
    """
    try:
        with Image.open(file) as img:
            return img.size
    except IOError:
        return ()
