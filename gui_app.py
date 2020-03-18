""" Main GUI entry """
import os
from typing import List

from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.popup import Popup
from dialog_app import LoadDialog, OptionDialog

from bool_collection import BoolCollection


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



class MainWindow(BaseApp):
    """ first gui windows to be displayed """

    def __init__(self):
        """ class variable & initialization """
        BaseApp.__init__(self)

    def load_file(self, _path, filename):
        """ Override: read files then close the load dialog """
        self.ids.selected_files.text += '\n'.join([os.path.join(_path, fn)
                                                   for fn in filename]) + '\n'
        # Close the popup windows
        self.dismiss_popup()

    def show_option(self):
        """ option dialog that contains options and select destination directory
            after confirming the integrity of data.
        """
        # split str into List[str]
        _files: List[str] = self.ids.selected_files.text.split('\n')

        _content: OptionDialog = OptionDialog(self.load_file, self.dismiss_popup,
                                              self.show_load(False), _files)
        self._popup = Popup(title="Selection Destination", content=_content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_process(self):
        """ display text telling user it's processing.
            when completed, it will display complete text box and confirm button
        """
        pass


class GuiApp(App):
    """ main gui entry """
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    GuiApp().run()
