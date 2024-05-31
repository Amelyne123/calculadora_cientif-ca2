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
            layout.add_widget(Button(text=str(i), on_press=self.on_button_press, background_color=(0.4, 0.4, 0.6, 1),
                                     font_size=20))
        layout.add_widget(Button(text='0', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.6, 1),
                                 font_size=20))
        layout.add_widget(Button(text='.', on_press=self.on_button_press, background_color=(0.3, 0.3, 0.3, 1),
                                 font_size=20))


        operations = ['+', '-', '*', '÷']
        for operation in operations:
            layout.add_widget(Button(text=operation, on_press=self.on_button_press, background_color=(0.3, 0.3, 0.3, 1),
                                     font_size=20))


        layout.add_widget(Button(text='sin', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='cos', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='tan', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='^', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='√', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='exp', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='log', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='π', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='(', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text=')', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='x^y', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='-', on_press=self.on_button_press, background_color=(0.4, 0.4, 0.4, 1),
                                 font_size=20))
        layout.add_widget(Button(text='deg->rad', on_press=self.on_button_press,
                                 background_color=(0.4, 0.4, 0.4, 1), font_size=15))
        layout.add_widget(Button(text='rad->deg', on_press=self.on_button_press,
                                 background_color=(0.4, 0.4, 0.4, 1), font_size=15))
        layout.add_widget(Button(text='=', on_press=self.on_button_press, background_color=(0, 0.6, 0, 1),
                                 font_size=20))
        layout.add_widget(Button(text='C', on_press=self.on_button_press, background_color=(0.6, 0, 0, 1),
                                 font_size=20))

        return layout

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                expression = self.display.text.replace('÷', '/').replace('π', str(math.pi))
                if 'x^y' in expression:
                    base, exponent = expression.split('x^y')
                    result = str(float(base) ** float(exponent))
                else:
                    result = str(eval(expression))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'C':
            self.display.text = ''
        elif instance.text == 'sin':
            try:
                result = str(math.sin(math.radians(eval(self.display.text))))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'cos':
            try:
                result = str(math.cos(math.radians(eval(self.display.text))))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'tan':
            try:
                result = str(math.tan(math.radians(eval(self.display.text))))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == '√':
            try:
                result = str(math.sqrt(eval(self.display.text)))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'exp':
            try:
                result = str(math.exp(eval(self.display.text)))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'log':
            try:
                result = str(math.log10(eval(self.display.text)))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'deg->rad':
            try:
                result = str(math.radians(eval(self.display.text)))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'rad->deg':
            try:
                result = str(math.degrees(eval(self.display.text)))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        else:
            self.display.text += instance.text


if __name__ == '__main__':
    Calculadora().run()