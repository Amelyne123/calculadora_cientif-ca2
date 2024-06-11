import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
import mysql.connector

Window.clearcolor = (0, 0, 0, 1)
Window.size = (380, 690)
Window.set_icon('icone.png')

def connect():
    # Configurar a conexão com o banco de dados aqui
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calculadora_cientifica"
    )

class ImageButton(ButtonBehavior, Image):
    pass

class Calculadora(Screen):
    def __init__(self, **kwargs):
        super(Calculadora, self).__init__(**kwargs)
        self.font_path = 'DejaVuSans.ttf' 
        self.mydb = connect()  # Conectar ao banco de dados
        
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
        
        modo1_button = Button(
            text=' ',
            background_color=(1, 1, 1, 0.2),
            font_size=20,
            font_name=self.font_path,
            valign='middle',
            halign='center'
        )
        modo1_button.bind(on_press=self.change_to_calculadora_c)
        modo1_image = Image(source='botaocalculadora.png', size_hint=(None, None), size=(90, 90))
        modo1_button.add_widget(modo1_image)
        modo1_button.bind(size=self.resize_image)
        row.add_widget(modo1_button)

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
        self.add_widget(main_layout)

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
                self.insert_historico(expression, result)  # Insere no histórico
            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'C':
            self.display.text = ''
        elif instance.text == '⌫':
            self.display.text = self.display.text[:-1]
        else:
            self.display.text += instance.text

    def on_historico_press(self, instance):
        self.manager.current = 'Historico'  # Mudar para a tela de histórico

    def insert_historico(self, operacao, resultado):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO historico (operacao, resultado) VALUES (%s, %s)"
        val = (operacao, resultado)
        mycursor.execute(sql, val)
        self.mydb.commit()
        mycursor.close()

    def change_to_calculadora_c(self, instance):
        self.manager.current = 'CalculadoraC'

class CalculadoraC(Screen):
    def __init__(self, **kwargs):
        super(CalculadoraC, self).__init__(**kwargs)
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
        row.add_widget(Button(text='π', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='0', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='.', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='÷', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path,
                              color=(0.9, 0.6, 0.3, 1)))
        main_layout.add_widget(row)

        main_layout.add_widget(create_button_row('sin', 'cos', 'x^y', '√'))

        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='exp', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='tan', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='log', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='=', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=30, font_name=self.font_path))
        main_layout.add_widget(row)

        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='deg->rad', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=15, font_name=self.font_path))
        row.add_widget(Button(text='(', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text=')', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=30, font_name=self.font_path))
        row.add_widget(Button(text='C', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=35, font_name=self.font_path))
        main_layout.add_widget(row)

        row = BoxLayout(orientation='horizontal', spacing=5)
        row.add_widget(Button(text='rad->deg', on_press=self.on_button_press, background_color=(1, 1, 1, 0.2), font_size=15, font_name=self.font_path))

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

        modo2_button = Button(
            text=' ',
            on_press=self.change_to_calculadora,
            background_color=(1, 1, 1, 0.2),
            font_size=30,
            font_name=self.font_path
        )
        modo2_image = Image(source='botaocalculadora.png', size_hint=(None, None), size=(90, 90))
        modo2_button.add_widget(modo2_image)
        modo2_button.bind(size=self.resize_image)
        row.add_widget(modo2_button)
   
        row.add_widget(Button(text='⌫', on_press=self.on_button_press, background_color=(0.9, 0.6, 0.3, 1), font_size=20, font_name=self.font_path))

        main_layout.add_widget(row)
        self.add_widget(main_layout)

    def resize_image(self, instance, value):
        for child in instance.children:
            if isinstance(child, Image):
                child.size = (instance.width * 0.4, instance.height * 0.8)
                child.center = instance.center

    def on_button_press(self, instance):
        if instance.text == '=':
            try:
                expression = self.display.text.replace('÷', '/').replace('×', '*').replace('π', str(math.pi))

                expression = self.replace_custom_functions(expression)

                result = str(eval(expression))
                self.display.text = result

                self.insert_historico(expression, result)

            except Exception as e:
                self.display.text = 'Erro'
        elif instance.text == 'C':
            self.display.text = ''
        elif instance.text == '⌫':
            self.display.text = self.display.text[:-1]
        elif instance.text == 'x^y':
            self.display.text += '^'
        elif instance.text in ['sin', 'cos', 'tan', 'exp', 'log', '√']:
            self.display.text += instance.text + '('
        elif instance.text == 'deg->rad':
            self.display.text += 'deg->rad'
        elif instance.text == 'rad->deg':
            self.display.text += 'rad->deg'
        else:
            self.display.text += instance.text

    def replace_custom_functions(self, expression):
        expression = expression.replace('sin(', 'math.sin(')
        expression = expression.replace('cos(', 'math.cos(')
        expression = expression.replace('tan(', 'math.tan(')
        expression = expression.replace('√(', 'math.sqrt(')
        expression = expression.replace('exp(', 'math.exp(')
        expression = expression.replace('log(', 'math.log10(')
        expression = expression.replace('^', '**')

        if 'deg->rad' in expression:
            value = float(expression.replace('deg->rad', ''))
            expression = str(math.radians(value))
        if 'rad->deg' in expression:
            value = float(expression.replace('rad->deg', ''))
            expression = str(math.degrees(value))

        return expression
    
    def insert_historico(self, operacao, resultado):
        pass

    def on_historico_press(self, instance):
        self.manager.current = 'Historico'
    
    def change_to_calculadora(self, instance):
        self.manager.current = 'Calculadora'

class Historico(Screen):
    def __init__(self, **kwargs):
        super(Historico, self).__init__(**kwargs)
        self.font_path = 'DejaVuSans.ttf'
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=15)

        top_layout = BoxLayout(size_hint=(1, None), height=50, spacing=5)

        back_button = ImageButton(source='setavoltar.png', size_hint=(None, None), size=(27, 50))
        back_button.bind(on_press=self.on_back_press)
        top_layout.add_widget(back_button)

        title_label = Label(
            text='Histórico',
            font_size=24,
            font_name=self.font_path,
            bold=True,
            size_hint=(1, None),
            height=50,
            halign='center'
        )
        top_layout.add_widget(title_label)

        main_layout.add_widget(top_layout)

        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)

        historico_layout = BoxLayout(orientation='vertical', spacing=10, padding=400, size_hint_y=None)
        historico_layout.bind(minimum_height=historico_layout.setter('height'))

        historico = self.get_historico()
        for operacao, resultado in historico:
            historico_label = Label(
                text=f"{operacao} = {resultado}",
                font_size=13,
                font_name=self.font_path,
                size_hint_y=None,
                height=200,
                text_size=(Window.width - 20, None),
                halign='left',
                valign='middle',
                color=(0.9, 0.6, 0.3, 1),
            )
            historico_label.bind(texture_size=historico_label.setter('size'))
            historico_layout.add_widget(historico_label)

        scroll_view.add_widget(historico_layout)

        main_layout.add_widget(scroll_view)

        self.add_widget(main_layout)

    def get_historico(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="calculadora_cientifica"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT operacao, resultado FROM historico ORDER BY id_historico DESC LIMIT 100")
        historico = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return historico

    def on_back_press(self, instance):
        self.manager.current = 'Calculadora'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Calculadora(name='Calculadora'))
        sm.add_widget(CalculadoraC(name='CalculadoraC'))
        sm.add_widget(Historico(name='Historico'))
        return sm

if __name__ == '__main__':
    MyApp().run()