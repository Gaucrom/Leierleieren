import json
import kivymd

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

from kivymd.uix.card import MDCard


class Homepage(MDScreen):
    pass    


class Lernstrategien(MDScreen):
    pass

class WindowManager(MDScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        Window.size = [400, 600]
        return Builder.load_file('leierleieren.kv')
        #return Homepage()

    # def on_start(self):
    #     self.root.dispatch('on_enter')


if __name__ == "__main__":
    MainApp().run()