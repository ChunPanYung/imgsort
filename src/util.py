"""
Includes various utility functions
"""
import sys
import shutil
from pathlib import Path


def sizeof_fmt(num):
    """ Credit to Fred Cirera
        print human readable file size
    """
    for unit in ['Bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f%s" % (num, unit)
        num /= 1024.0
    return num


def create_dir(directory: str) -> bool:
    """
        Create from directory:str
        It will create parent directory if it doesn't exist.
        It won't throw Exception if directory already exists.
    """
    try:
        Path(directory).mkdir(parents=True, exist_ok=True)
    except FileExistsError as error:
        sys.exit(error)

    return True

