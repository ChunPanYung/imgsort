"""
Sorting all images files by height and width
"""
from PIL import Image

class ImagePtr:
    """
    Double link list.  For each node, it contains all images with
    same height, width, total number and their location.
    """

    # static class variables
    _lst = [] # contains list of object ImagePtr

    def __init__(self, width, height, location):
        self.width = width
        self.height = height
        self.location = []
        self.location.extend(location)
        self.num = 1

    def get_width(self):
        """ return the width of image : int """
        return self.width

    def get_height(self):
        """ return the height of image : int """
        return self.height

    def add_list(self, location):
        """
        add location into location[] variable
        location : string
        return none
        """
        self.location.extend(location)
        self.num += 1

    @staticmethod
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
            except Exception:
                pass

    @staticmethod
    def _append(image):
        """
        append the image into the static class variable _lst as a new node
        image : string
        """
        ImagePtr._lst.extend(ImagePtr(image.get_width, image.get_height, image))
