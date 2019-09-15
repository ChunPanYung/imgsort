"""
This module will only contain functions that manipulates class ImagePtr
"""
from typing import List # needed for Type aliases for 'List' data type
from PIL import Image
from imgsort import image_ptr as ImagePtr

def append(files):
    """
    append image files into static class variable _lst
    if they are image files
    files : list
    """
    # check whether each file is img file,
    # then get the width and height
    # put them in a list
    for file in files:
        img = Image.open(file)
        try: # verify whether it's image (loose verifcation)
            img.verify()
            # check if it's ImagePtr already exist
            length = len(ImagePtr._lst)
            if length != 0:
                # check each ImagePtr to see whether it matches the width and height
                for node in ImagePtr._lst:
                    # if it's the same width and height
                    if img.size == (node.get_width, node.get_height):
                        node.add_list(file)
                    # Otherwise create a new ImagePtr object on the list
                    else:
                        ImagePtr._append(file)
            # Otherwise create a new ImagePtr object on the list
            else:
                ImagePtr._append(file)
        except IOError:
            print('Unable to read image file(s)')

def _append(image):
    """
    append the image into the static class variable _lst as a new node
    image : string
    """
    ImagePtr._lst.extend(ImagePtr(image.get_width, image.get_height, image))

def list_all():
    """
    Print information about sorted images (by width and height)
    Return False if there's ImagePtr._lst is empty
    """
    if not ImagePtr._lst:
        print("No image is being sorted into folder.")
        return False

    # print all sorted images and its related information
    for _sorted in ImagePtr._lst:
        # print sorted image size and all its related location
        print('Image Size: {}x{}'.format(_sorted.width, _sorted.height))
        if not _sorted.location:
            for loc in _sorted.location:
                print('| ', loc)
    return True
