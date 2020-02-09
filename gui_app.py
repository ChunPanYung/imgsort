from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainWindow(Widget):
    pass

class GuiApp(App):

    def build(self):
        return MainWindow()
