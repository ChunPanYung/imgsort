"""
Sorting all images files by height and width
"""
from typing import List # needed for Type aliases for 'List' data type
from PIL import Image

class ImagePtr:
    """
    Double link list.  For each node, it contains all images with
    same height, width, total number and their location.
    """

    def __init__(self, width, height, location):
        self.width: int = width
        self.height: int = height
        self.location: List[str] = []
        self.location.extend(location)

    def get_width(self) -> int:
        """ return the width of image : int """
        return self.width

    def get_height(self) -> int:
        """ return the height of image : int """
        return self.height

    def get_location(self) -> List[str]:
        """ return list of image location who shares the same height and weight """
        return self.location

    def add_list(self, location: str):
        """
        add location into location[] variable
        location : string
        return none
        """
        self.location.extend(location)
