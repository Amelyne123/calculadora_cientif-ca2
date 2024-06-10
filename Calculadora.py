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

class Calculadora(App):
    def build(self):
        
        self.font_path = 'DejaVuSans.ttf' 
        
       
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=5)

        
        self.display = TextInput(multiline=False, readonly=True, font_size=30, background_color=(1, 1, 1, 0.07),
                                 foreground_color=(0.9, 0.6, 0.3, 1), size_hint=(1, 1.8), font_name=self.font_path)
        main_layout.add_widget(self.display)

        
        def create_button_row(*buttons):
            row = BoxLayout(orientation='horizontal', spacing=5)
            for button_text in buttons:
                
                if button_text in ['+', '-', '×', '÷']:
                    button = Button(text=button_text, on_press=self.on_button_press, background_color=(1, 1, 1, 0.2),
                                    font_size=30, font_name=self.font_path, color=(0.9, 0.6, 0.3, 1))
                else:
                    button = Button(text=button_text, on_press=self.on_button_press, background_color=(1, 1, 1, 0.2),
                                    font_size=30, font_name=self.font_path)
                row.add_widget(button)
            return row

        
        main_layout.add_widget(create_button_row('7', '8', '9', '+'))

        
        main_layout.add_widget(create_button_row('4', '5', '6', '-'))

        
        main_layout.add_widget(create_button_row('1', '2', '3', '×'))

    
        row = BoxLayout(orientation='horizontal', spacing=5)
        
       
        historico_button = Button(
            text=' ',
            on_press=self.on_historico_press,
            background_color=(1, 1, 1, 0.2),
            font_size=20,
            font_name=self.font_path,
            valign='middle',
            halign='center'
        )
        historico_image = Image(source='botaohistorico.png', size_hint=(None, None), size=(90, 90))
        historico_button.add_widget(historico_image)
        historico_button.bind(size=self.resize_image)
        row.add_widget(historico_button)
        
       
        row.add_widget(Button(text='0', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        
       
        row.add_widget(Button(text='.', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        
        
        row.add_widget(Button(text='÷', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path, color=(0.9, 0.6, 0.3, 1)))
        
        main_layout.add_widget(row)

        
        row = BoxLayout(orientation='horizontal', spacing=5)
        
        modo_button = Button(
            text=' ',
            on_press=self.on_button_press,
            background_color=(1, 1, 1, 0.2),
            font_size=20,
            font_name=self.font_path,
            valign='middle',
            halign='center'
        )
        modo_image = Image(source='botaocalculadora.png', size_hint=(None, None), size=(90, 90))
        modo_button.add_widget(modo_image)
        modo_button.bind(size=self.resize_image)
        row.add_widget(modo_button)

        
        igual_button = Button(
            text='=',
            on_press=self.on_button_press,
            background_color=(0.9, 0.6, 0.3, 1),
            font_size=30,
            font_name=self.font_path
        )
        row.add_widget(igual_button)

        
        row.add_widget(Button(text='C', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=30, font_name=self.font_path))
        
       
        row.add_widget(Button(text='⌫', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=20, font_name=self.font_path))

        main_layout.add_widget(row)

        return main_layout

    def resize_image(self, instance, value):
        
        for child in instance.children:
            if isinstance(child, Image):
                child.size = (instance.width * 0.4, instance.height * 0.8)
                child.center = instance.center

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                
                expression = self.display.text.replace('÷', '/').replace('×', '*')
                result = str(eval(expression))
                self.display.text = result
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'C':
            self.display.text = ''
        elif instance.text == '⌫':
            self.display.text = self.display.text[:-1]
        else:
            self.display.text += instance.text

    def on_historico_press(self, instance):
        
        self.display.text += "[Histórico] "  

if __name__ == '__main__':
    Calculadora().run()
