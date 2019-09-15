"""
This class contains all images who has the same height and width.
"""
from typing import List # needed for Type aliases for 'List' data type
from PIL import Image

class ImagePtr:
    """
    This class contains all images who has the same height and width.
    """

    def __init__(self, width, height, file):
        self.width: int = width
        self.height: int = height
        # contains all images path who share the same width and height
        self.path: List[str] = []
        self.path.extend(file)

    def get_width(self) -> int:
        """ return the width of image : int """
        return self.width

    def get_height(self) -> int:
        """ return the height of image : int """
        return self.height

    def get_path(self) -> List[str]:
        """ return list of image path who shares the same height and weight """
        return self.path

    def add_to_path(self, file: str) -> bool:
        """
        add image file path into path[] variable
        if it's image and has same width and height as in this class
        return none
        """
        with Image.open(file) as img:
            if img.size == (self.width, self.height):
                self.path.extend(file)
                return True
        return False
