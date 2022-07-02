"""
This class is only used when doing summary or dry-run
"""
import os
from typing import Tuple
from util import sizeof_fmt


class ImageInfo():
    """
    This class contains all images who has the same height and width.
    """


    def __init__(self, width: int, height: int, _file: str):
        self.width: int = width
        self.height: int = height
        # num of image with same width and height
        self.num: int = 1
        self.paths: list[str] = [_file]
        # total size(bytes) of all images who share the same width and height
        if _file is None:
            self.total_size: int = 0
        else:
            self.total_size: int = os.path.getsize(_file)

    def get_width(self) -> int:
        """ return the width of image : int """
        return self.width

    def get_height(self) -> int:
        """ return the height of image : int """
        return self.height

    def get_num(self) -> int:
        """ return number of images who share the same width and height """
        return self.num

    def get_total_size(self) -> int:
        """ return total size of images who share the same width and height
            return int is in bytes size
        """
        return self.total_size

    def increment(self, _file: str) -> bool:
        """ increment the number by image by one and total_size by img_size """
        self.num += 1
        self.total_size += os.path.getsize(_file)
        self.paths.append(_file)
        return True

    def is_same(self, tup: Tuple[int, int]) -> bool:
        """
        recive that tuple that contains 2 value (width: int, height: int)

        return true if it's the same as object, false otherwise
        """
        if tup[0] == self.width and tup[1] == self.height:
            return True

        return False

    def to_string(self) -> bool:
        """
        print all value in a class
        """
        print('Image size: {0}x{1}'.format(self.width, self.height))
        print('-Total numbers: {}'.format(self.num))
        print('-Total size: {}\n'.format(sizeof_fmt(self.total_size)))

        return True
