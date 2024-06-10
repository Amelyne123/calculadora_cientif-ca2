import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)
Window.size = (390, 700)
Window.set_icon('icone.png')

class Historico(App):
    def build(self):

        self.font_path = 'DejaVuSans.ttf'
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=5)
    

if __name__ == '__main__':
    Historico().run()