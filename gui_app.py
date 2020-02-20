from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty

class MainWindow(BoxLayout):
    pass

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content: LoadDialog = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup: Popup = Popup(title="Load file", content=content,
                                   size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.ids.selected_files.text = stream.read()

class LoadDialog(FloatLayout):
    load: ObjectProperty = ObjectProperty(None)
    cancel: ObjectProperty = ObjectProperty(None)

class GuiApp(App):
    def build(self):
        return MainWindow()


