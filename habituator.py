import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class WelcomeScreen(Widget):
    pass


class HabituatorApp(App):
    def build(self):
        return WelcomeScreen()


if __name__ == "__main__":
    HabituatorApp().run()
