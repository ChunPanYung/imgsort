""" contains NamedTuple to gather multiple variables into single object """
from typing import NamedTuple


class BoolCollection(NamedTuple):
    """
    Used for putting all boolean value as one object and pass to function
    """
    recursive: bool
    copy: bool
    verbose: bool
    unknown: bool
    include: bool  # False implies exclude is True or no image size limit
