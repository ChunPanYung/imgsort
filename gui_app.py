""" Main GUI entry """
import os

from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from dialog_app import LoadDialog, OptionDialog


class MainWindow(BoxLayout):
    """ first gui windows to be displayed """

    def __init__(self):
        """ class variable & initialization """
        self._popup: Popup = None
        super(MainWindow, self).__init__()

    def dismiss_popup(self):
        """ remove/dismiss gui window """
        self._popup.dismiss()

    def show_load(self):
        """ display load dialog, assign function to load button and cancel button """
        _content: LoadDialog = LoadDialog(self.load_file, self.dismiss_popup)
        self._popup = Popup(title="Load file", content=_content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load_file(self, path, filename):
        """ read files then close the load dialog """
        self.ids.selected_files.text = '\n'.join([os.path.join(path, fn)
                                                  for fn in filename])
        # Close the popup windows
        self.dismiss_popup()

    def confirm(self):
        """ option dialog that contains options and select destination directory
            after confirming the integrity of data.
        """
        return None


class GuiApp(App):
    """ main gui entry """
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    GuiApp().run()
