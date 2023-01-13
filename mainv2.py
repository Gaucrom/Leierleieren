import json
import kivymd

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from kivymd.uix.card import MDCard


class HomePage(MDScreen):
    pass

class MainApp(MDApp):
    def build(self):
        Window.size = [400, 600]
        Builder.load_file('leierleieren.kv')
        return HomePage()

    # def on_start(self):
    #     self.root.dispatch('on_enter')


if __name__ == "__main__":
    MainApp().run()