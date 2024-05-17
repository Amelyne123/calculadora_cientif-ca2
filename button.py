import math
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

Window.clearcolor = (0.2, 0.2, 0.2, 1)  


class Calculadora(App):
    def build(self):
        layout = GridLayout(cols=4, spacing=5, padding=5)

        self.display = TextInput(multiline=False, font_size=20, background_color=(0.1, 0.1, 0.1, 1),
                                 foreground_color=(1, 1, 1, 1))
        layout.add_widget(self.display)

        for i in range(1, 10):
         layout.add_widget(Button(text=str(i), on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                     font_size=20))
        layout.add_widget(Button(text='.', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='0', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))

        operations = ['+', '-', 'x', '÷']
        for operation in operations:
            layout.add_widget(Button(text=operation, on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                     font_size=20))

        layout.add_widget(Button(text='C', on_press=self.on_button_press, background_color=(0.8, 0, 0, 1),
                                 font_size=20))
        layout.add_widget(Button(text='sin', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='cos', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='tan', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='^', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='sqrt', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='exp', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='deg->rad', on_press=self.on_button_press,
                                 background_color=(0.4, 0.4, 0.4, 1), font_size=15))
        layout.add_widget(Button(text='rad->deg', on_press=self.on_button_press,
                                 background_color=(0.4, 0.4, 0.4, 1), font_size=15))
        layout.add_widget(Button(text='=', on_press=self.on_button_press, background_color=(0, 0.6, 0, 1),
                                 font_size=20))

        return layout


if __name__ == '__main__':
    Calculadora().run()
