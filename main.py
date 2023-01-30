from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
from pygame import mixer
from time import sleep


class morseCode(App):
    def build(self):
        # cria a simbologia
        self.audio_bips = {'.': './sounds/bip_curto.mp3', '-': './sounds/bip_longo.mp3'}
        self.alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
                         'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                         'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                         'Y': '-.--', 'Z': '--..', ' ': ' ', '1': '.----',
                         '2': '..---', '3': '...--', '4': '....-',
                         '5': '.....', '6': '-....', '7': '--...',
                         '8': '---..', '9': '----.', '0': '-----',
                         '.': '.-.-.-', ',': '--..--', '?': '..--..',
                         '!': '-.-.--', '´': '.----.', '"': '.-..-.',
                         '(': '-.--.', ')': '-.--.-', '&': '.-...',
                         ':': '---...', ';': '-.-.-.', '/': '-..-.',
                         '_': '..--.-', '=': '-...-', '+': '.-.-.',
                         '-': '-....-', '$': '...-..-', '@': '.--.-.'
                         }
        # cria gerenciador de tela
        self.sm = ScreenManager()
        # cria tela 1
        self.screen1 = Screen(name='screen1')
        self.label_screen_1 = Label(text='Digite o texto e clique em "Gerar código"',
                                    size_hint=(0.8, 0.5),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.90},
                                    font_size=20,
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
        # inicializa o mixer de audio
        mixer.init(frequency=16000)

        return self.layout

    # troca para tela 1
    def switch_to_screen1(self, *args):
        self.sm.current = 'screen1'

    # troca para tela 2
    def switch_to_screen2(self, *args):
        self.sm.current = 'screen2'

    # cria o texto em morse
    def make_morse(self, *args):
        text = self.input_text_label_1._get_text().upper()
        morse = ''
        if len(text) < 51 and len(text) != 0:
            for key, value in enumerate(text):
                if value not in self.alphabet.keys():
                    msg = f'O caractere {value} não faz parte do padrão morse internacional.'
                    self.label_screen_1.text = msg
                    return
                else:
                    morse += self.alphabet[value]
            self.label_screen_1.text = morse
            self.label_screen_1.text_size = self.label_screen_1.size
        elif len(text) != 0:
            self.label_screen_1.text = f'Seu texto tem {len(text)} caracteres, o limite recomendado é 50 por conversão.'
            self.label_screen_1.text_size = self.label_screen_1.size
        else:
            return

    # limpa a caixa de texto
    def clear_text_label_screen_1(self, *args):
        self.input_text_label_1.text = ''
        self.label_screen_1.text = 'Para gerar um novo código digite o texto e clique em "Gerar código"'

    # copiar o texto do TextInput no label 1
    def copy_text_label_screen_1(self, *args):
        text_copied = Clipboard.copy(data=self.label_screen_1.text)
        return text_copied

    # tocar o código gerado no label 1
    def play_text_label_screen_1(self, *args):
        text = self.label_screen_1.text
        if text[0] in '.- ':
            for i in text:
                if i != ' ':
                    mixer.music.load(self.audio_bips[i])
                    mixer.music.play()
                    if i == '.':
                        sleep(0.2)
                    else:
                        sleep(0.4)
                    mixer.music.unload()
                else:
                    sleep(0.7)
        else:
            return


if __name__ == '__main__':
    morseCode().run()
