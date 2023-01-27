from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard


class morseCode(App):
    def build(self):
        # cria a simbologia
        self.short_bit = '.'
        self.long_bit = '_'
        self.alphabet = {'A': (), 'B': (), 'C': (), 'D': (), 'E': (), 'F': (),
                         'G': (), 'H': ()}
        # cria gerenciador de tela
        self.sm = ScreenManager()
        # cria tela 1
        self.screen1 = Screen(name='screen1')
        self.label_screen_1 = Label(text='Digite o texto e clique em "Gerar código"',
                                    size_hint=(0.8, 0.2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.75}
                                    )
        self.input_text_label_1 = TextInput(hint_text='Digite seu texto aqui',
                                            size_hint=(0.8, 0.2),
                                            pos_hint={'center_x': 0.5, 'center_y': 0.5}
                                            )
        self.button_screen_1_clear = Button(text='Limpar',
                                            size_hint=(0.4, 0.15),
                                            pos_hint={'center_x': 0.30, 'center_y': 0.25},
                                            on_press=self.clear_text_label_screen_1
                                            )
        self.button_screen_1_ok = Button(text='Gerar código',
                                         size_hint=(0.4, 0.15),
                                         pos_hint={'center_x': 0.70, 'center_y': 0.25},
                                         on_press=self.make_morse
                                         )
        self.button_screen_1_copy = Button(text='Copiar',
                                           size_hint=(0.4, 0.15),
                                           pos_hint={'center_x': 0.30, 'center_y': 0.10},
                                           on_press=self.copy_text_label_screen_1
                                           )
        self.button_screen_1_play = Button(text='Tocar código',
                                           size_hint=(0.4, 0.15),
                                           pos_hint={'center_x': 0.70, 'center_y': 0.10},
                                           on_press=self.play_text_label_screen_1
                                           )
        self.screen1.add_widget(self.label_screen_1)
        self.screen1.add_widget(self.input_text_label_1)
        self.screen1.add_widget(self.button_screen_1_clear)
        self.screen1.add_widget(self.button_screen_1_ok)
        self.screen1.add_widget(self.button_screen_1_copy)
        self.screen1.add_widget(self.button_screen_1_play)
        # cria tela 2
        self.screen2 = Screen(name='screen2')
        self.label_screen_2 = Label(text='This is screen 2')
        self.screen2.add_widget(self.label_screen_2)
        # adiciona telas no gerenciador de telas
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
        # cria o layout
        self.layout = BoxLayout(orientation='vertical')
        # cria o menu e adiciona botões ao menu
        self.menu = BoxLayout(size_hint=(1, None), height=50)
        self.menu.add_widget(Button(text='Gerar código morse', on_press=self.switch_to_screen1))
        self.menu.add_widget(Button(text='Traduzir código morse', on_press=self.switch_to_screen2))
        # adiciona o menu e o gerenciador de telas ao layout do app
        self.layout.add_widget(self.menu)
        self.layout.add_widget(self.sm)

        return self.layout

    # troca para tela 1
    def switch_to_screen1(self, *args):
        self.sm.current = 'screen1'

    # troca para tela 2
    def switch_to_screen2(self, *args):
        self.sm.current = 'screen2'

    # cria o texto em morse
    def make_morse(self, *args):
        self.label_screen_1.text = self.input_text_label_1._get_text()

    # limpa a caixa de texto
    def clear_text_label_screen_1(self, *args):
        self.input_text_label_1.text = ''
        self.label_screen_1.text = 'Digite o texto e clique em "Gerar código"'

    # copiar o texto do TextInput no label 1
    def copy_text_label_screen_1(self, *args):
        text_copied = Clipboard.copy(data=self.label_screen_1.text)
        return text_copied

    # tocar o código gerado no label 1
    def play_text_label_screen_1(self, *args):
        return self.label_screen_1.text


if __name__ == '__main__':
    morseCode().run()
