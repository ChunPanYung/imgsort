"""
This module will only contain functions that manipulates class ImagePtr
in linked list.
"""
import os
from typing import List # needed for Type aliases for 'List' data type
from PIL import Image
from imgsort.image_ptr import ImagePtr

def sort(files) -> List[ImagePtr]:
    """
    sort images by height and width

    Return: lst: List[ImagePtr]
    """

    # Contains list of object ImagePtr, with each object contains images
    # who has the same width and height
    lst: List[ImagePtr] = []

    # Cycle through each file
    for file in files:
        # Check to see whether it can grab img width and height
        img_size = ImagePtr.is_image(file)

        if not img_size: # If it can, do the following:
            for node in lst: # Cycle through each node in list
                file = os.path.abspath(file) # Get absolute file path
                if node.is_same(img_size): # Add img path into node if same size
                    node.add_to_path(file)
                else: # otherwise create node that save all img with same size
                    lst.append(ImagePtr(img_size[0], img_size[1], file))

    # return linked list after sorting through all files
    return lst

def dry_run(lst: List[ImagePtr]) -> bool:
    """
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
