"""
This class contains all images who has the same height and width.
"""
from typing import List, Tuple # needed for Type aliases for 'List' data type
from PIL import Image

class ImagePtr:
    """
    This class contains all images who has the same height and width.
    """

    def __init__(self, width, height, img):
        self.width: int = width
        self.height: int = height
        # contains all images path who share the same width and height
        self.path: List[str] = []
        self.path[:0] = [img]

    def get_width(self) -> int:
        """ return the width of image : int """
        return self.width

    def get_height(self) -> int:
        """ return the height of image : int """
        return self.height

    def get_path(self) -> List[str]:
        """ return list of image path who shares the same height and weight """
        return self.path

    def add_to_path(self, img: str) -> None:
        """
        Add image file path into path[] variable
        if it's image and has same width and height as in this class

        Return image width and height
        else return empty tuple
        """
        self.path[:0] = [img]

    def is_same(self, tup: Tuple) -> bool:
        """
        recive that tuple that contains 2 value (width: int, height: int)

        return true if it's the same as object, false otherwise
        """
        if tup[0] == self.width and tup[1] == self.height:
            return True

        return False

    @staticmethod
    def is_image(file: str) -> Tuple:
        """
        verify whether it's image or not

        Return Tuple (img.width, img.height) if yes
        Return emtpy Tuple if no
        """
        with Image.open(file) as img:
            if img.verify:
                return img.size
        return ()
