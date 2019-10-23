"""
This module will only contain functions that manipulates class ImagePtr
in linked list.
"""
import os
from typing import List
from typing import Tuple
from PIL import Image
from image_ptr import ImagePtr

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
        img_size: Tuple = ImagePtr.is_image(file)

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
