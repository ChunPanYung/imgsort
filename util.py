"""
Includes various utility functions
"""
import sys
import shutil
from pathlib import Path
from bool_collection import BoolCollection


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


def move_file(_file: str, new_directory: str, bool_value: BoolCollection):
    """
    attempt to either copy or move file(s) to new directory(s)
    output error if file with same name exists
    """
    try:
        if bool_value.copy:
            shutil.copy(_file, new_directory)
            if bool_value.verbose:
                print('COPY: "{}"\nTO:   "{}"'.format(_file, new_directory))
        else:
            shutil.move(_file, new_directory)
            if bool_value.verbose:
                print('MOVE: "{}"\nTO:   "{}"'.format(_file, new_directory))
    except shutil.Error as error:
        print('{0}'.format(error), file=sys.stderr)
