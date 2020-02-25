import os

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


class LoadDialog(FloatLayout):
    load: ObjectProperty = ObjectProperty(None)
    cancel: ObjectProperty = ObjectProperty(None)


class MainWindow(BoxLayout):
    pass

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        # display load dialog, assign function to load button and cancel button
        content: LoadDialog = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup: Popup = Popup(title="Load file", content=content,
                                   size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        """ read files then close the load dialog """
        self.ids.selected_files.text = '\n'.join([os.path.join(path, fn) 
                                                for fn in filename])
        # Close the popup windows
        self.dismiss_popup()


class GuiApp(App):
    def build(self):
        return MainWindow()
