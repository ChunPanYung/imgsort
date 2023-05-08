"""
Static class for keeping checking of image file path and number of images who
share the same size.
"""
from typing import List, Tuple
from image_info import ImageInfo


class ImageNum():
    """ Static class with only static variables.

        image_info: List[ImageInfo] contains image size and number of image for
        that said size.

        path:List[List[str]] contains List, with each node is another List.
        For each List in a node, it's str -- file path to single image.
        """
    image_info: List[ImageInfo]
    path: List[List[str]]


    @staticmethod
    def get_image_info() -> List[ImageInfo]:
        """ return image_info: List[ImageInfo] """
        return ImageNum.image_info

    @staticmethod
    def get_path() -> List[List[str]]:
        """ return image_info: List[ImageInfo] """
        return ImageNum.path

    @staticmethod
    def clear_path(index: int) -> List[str]:
        """ Clear List of file path and return them """
        ret_value: List[str] = ImageNum.path[index].copy()
        ImageNum.path[index] = ['']
        return ret_value

    @staticmethod
    def _append(size: Tuple[int, int], file_path: str) -> bool:
        """ Record size of image and its file path into static variable.
            If node with such image size exists, add info into such node,
            otherwise create a new one.

        """
        is_append: bool = False
        # Cycle through each node, getting both index and value
        for index, node in enumerate(ImageNum.image_info):
            # if they are the same size, number value increase by 1,
            # record file path
            if node.is_same(size):
                node.increment(file_path)
                ImageNum.path[index].append(file_path)
                is_append = True
        # if is_append: bool is still false, it means that we need to create a
        # new node in both image_info: List and path: List
        if not is_append:
            ImageNum.image_info.append(ImageInfo(size[0], size[1], file_path))
            ImageNum.path.append([file_path])

        return True
