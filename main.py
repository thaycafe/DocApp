#coding: utf-8
import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button

class Inicial(Screen):
    pass

class WidgetsKivy(Screen):
    pass

class SintaxePy(Screen):
    pass

class SintaxeKv(Screen):
    pass

class SintaxeLb(Screen):
    def clique(self):
        layout = GridLayout(cols=1)
        popuplb= Label(text='Você clicou na Label!')
        popupbt= Button(text='Fechar Popup')
        layout.add_widget(popuplb)
        layout.add_widget(popupbt)
        popup = Popup(title='Função ao clicar na Label', auto_dismiss=False,content=layout, size_hint=(.5, .3))
        popupbt.bind(on_press=popup.dismiss)
        popup.open()

class TransicaoTela(ScreenManager):
    transition = NoTransition(duration = 0)


class DocApp(App):
    def build(self):
        return TransicaoTela()

Window.clearcolor = [1, 1, 1, 1]
DocApp().run()
