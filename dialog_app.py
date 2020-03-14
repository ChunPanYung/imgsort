""" Contains all dialog that float on top of main window """
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty



class LoadDialog(FloatLayout):
    """ load dialog for selecting files/directories """
    def __init__(self, _load: ObjectProperty, _cancel: ObjectProperty):
        self._load: ObjectProperty = _load
        self._cancel: ObjectProperty = _cancel
        super(LoadDialog, self).__init__()

class OptionDialog(FloatLayout):
    """ Option dialog and for choosing destination directory """
    def __init__(self, _next: ObjectProperty, _cancel: ObjectProperty):
        self._next: ObjectProperty = _next
        self._cancel: ObjectProperty = _cancel
        super(OptionDialog, self).__init__()
