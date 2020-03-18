""" Contains all dialog that float on top of main window """
from typing import List
from kivy.properties import ObjectProperty
from base_app import BaseApp


class OptionDialog(BaseApp):
    """ Option dialog and for choosing destination directory """
    def __init__(self, _next: ObjectProperty, cancel: ObjectProperty,
                 load: ObjectProperty, files: List[str]):
        self._next: ObjectProperty = _next
        self.cancel: ObjectProperty = cancel
        self.load: ObjectProperty = load

        self.files: List[str] = files # contains list of source file path

        super(OptionDialog, self).__init__()
