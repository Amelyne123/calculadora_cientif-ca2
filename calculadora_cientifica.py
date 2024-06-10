import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window

# Ajustes no tamanho, cor e ícone da calculadora
Window.clearcolor = (0, 0, 0, 1)
Window.size = (380, 690)
Window.set_icon('icone.png')

class Calculadora(App):
    def build(self):
        # Fonte personalizada
        self.font_path = 'DejaVuSans.ttf'  # Caminho para a fonte personalizada
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=5)

        # Display da calculadora
        self.display = TextInput(multiline=False, readonly=True, font_size=30, background_color=(1, 1, 1, 0.07),
                                 foreground_color=(0.9, 0.6, 0.3, 1), size_hint=(1, 1.8), font_name=self.font_path)
        main_layout.add_widget(self.display)

        # Função auxiliar para criar linhas de botões
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

        # Primeira linha de botões (1 a 3)
        main_layout.add_widget(create_button_row('7', '8', '9', '+'))

        # Segunda linha de botões (4 a 6)
        main_layout.add_widget(create_button_row('4', '5', '6', '-'))

        # Terceira linha de botões (7 a 9)
        main_layout.add_widget(create_button_row('1', '2', '3', '×'))

        # Quarta linha de botões (π, 0, ., ÷)
        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='π', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='0', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='.', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='÷', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=35, font_name=self.font_path, color=(0.9, 0.6, 0.3, 1)))
        main_layout.add_widget(row)

        # Linha para funções adicionais (sin, cos, tan, √)
        main_layout.add_widget(create_button_row('sin', 'cos', 'x^y', '√'))

        # Linha para funções adicionais (exp, log, tan, =)
        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='exp', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='tan', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='log', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='=', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=30, font_name=self.font_path))
        main_layout.add_widget(row)

        # Linha para funções adicionais (deg->rad, (, ), C)
        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='deg->rad', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=15, font_name=self.font_path))
        row.add_widget(Button(text='(', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text=')', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='C', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=35, font_name=self.font_path))
        main_layout.add_widget(row)

        # Linha para funções adicionais (rad->deg, Modo, Histórico, ⌫)
        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='rad->deg', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=15, font_name=self.font_path))
        
        # Botão "Modo" com imagem sobreposta
        modo_button = Button(
            text=' ',
            on_press=self.on_button_press,
            background_color=(1, 1, 1, 0.2),
            font_size=20,
            font_name=self.font_path,
            valign='middle',
            halign='center'
        )

        # Adiciona a imagem sobre o botão "Modo"
        modo_image = Image(source='botaocalculadora.png', size_hint=(None, None), size=(80, 80))
        modo_button.add_widget(modo_image)

        # Ajuste de propriedades visuais e posicionamento
        modo_button.bind(size=self.resize_image)
        
        row.add_widget(modo_button)

        # Botão "Histórico" com imagem sobreposta
        historico_button = Button(
            text=' ',
            on_press=self.on_button_press,
            background_color=(1, 1, 1, 0.2),
            font_size=20,
            font_name=self.font_path,
            valign='middle',
            halign='center'
        )

        # Adiciona a imagem sobre o botão "Histórico"
        historico_image = Image(source='botaohistorico.png', size_hint=(None, None), size=(90, 90))
        historico_button.add_widget(historico_image)

        # Ajuste de propriedades visuais e posicionamento
        historico_button.bind(size=self.resize_image)

        row.add_widget(historico_button)
        
        row.add_widget(Button(text='⌫', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=20, font_name=self.font_path))
        main_layout.add_widget(row)

        return main_layout

    def resize_image(self, instance, value):
        # Ajuste o tamanho da imagem ao tamanho do botão
        for child in instance.children:
            if isinstance(child, Image):
                child.size = (instance.width * 0.4, instance.height * 0.8)
                child.center = instance.center

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                expression = self.display.text.replace('÷', '/').replace('×', '*').replace('π', str(math.pi))
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
        elif instance.text == '⌫':  # Função para remover o último caractere
            self.display.text = self.display.text[:-1]
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

