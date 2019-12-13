from typing import NamedTuple


class BoolCollection(NamedTuple):
    """
    Used for putting all boolean value as one object and pass to function
    """
    recursive: bool
    copy: bool
    verbose: bool
