""" This is for pylintrc, init-hook variable.
    It's for indicating where to find virtualenv library and bin
    before executing pylintrc
"""
import os
import sys
from platform import python_version
from pylint.config import find_pylintrc


def set_path() -> None:
    """ import virtualenv path into sys.path """
    # Get the directory of pylintrc file
    _dirname: str = os.path.dirname(find_pylintrc())
    # Get the bin directory
    _bin: str = os.path.join(_dirname, 'bin')
    # Get the site_packages directory
    _site_packages: str = os.path.join(_dirname, 'lib', 'python' + python_version(),
                                       'site_packages')

    sys.path.append(_bin)
    sys.path.append(_site_packages)

# Execute it when this file import
set_path()
