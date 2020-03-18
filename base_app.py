""" Base GUI method/functions that will share among all child classes """
from typing import List
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from bool_collection import BoolCollection


class LoadDialog(FloatLayout):
    """ load dialog for selecting files/directories """
    def __init__(self, load: ObjectProperty, cancel: ObjectProperty):
        self.load: ObjectProperty = load
        self.cancel: ObjectProperty = cancel
        super(LoadDialog, self).__init__()

    def is_multiselect(self, _bool: bool) -> None:
        """ whether to allow selecting multiple files/directories.
            default is allowed. """
        self.ids.filechooser.multiselect = False # disable multi select


class BaseApp(Widget):
    """ basic class method that will be shared among widgets """
    def __init__(self):
        """ initialization """
        self._popup: Popup = None
        self._files: List[str] = None
        self._destination: str = None
        self._bool_value: BoolCollection = None
        self._limit_size: List[str] = None
        super(BaseApp, self).__init__()

    def dismiss_popup(self):
        """ remove/dismiss gui window """
        self._popup.dismiss()

    def load_file(self, _path, filename):
        """ empty method """

    def show_load(self, _bool: bool):
        """ display load dialog, assign function to load button and cancel button """
        _content: LoadDialog = LoadDialog(self.load_file, self.dismiss_popup)
        self._popup = Popup(title="Load file", content=_content,
                            size_hint=(0.9, 0.9))

        # disable multiselect: only one destination folder
        _content.is_multiselect(_bool)

        self._popup.open()
