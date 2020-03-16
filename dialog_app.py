""" Contains all dialog that float on top of main window """
from typing import List
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty



class LoadDialog(FloatLayout):
    """ load dialog for selecting files/directories """
    def __init__(self, load: ObjectProperty, cancel: ObjectProperty):
        self.load: ObjectProperty = load
        self.cancel: ObjectProperty = cancel
        super(LoadDialog, self).__init__()

class OptionDialog(FloatLayout):
    """ Option dialog and for choosing destination directory """
    def __init__(self, next: ObjectProperty, cancel: ObjectProperty,
                 files: List[str]):
        self.next: ObjectProperty = next
        self.cancel: ObjectProperty = cancel
        self.files: List[str] = files # contains list of source file path
        super(OptionDialog, self).__init__()
