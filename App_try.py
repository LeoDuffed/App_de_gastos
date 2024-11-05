from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window 

class Pantall_Inicio (Screen):
    def __init__ (self, **kwargs):

        super().__init__(**kwargs)
        layout  = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)
        Welcome_label= Label (text= "Programa de gastos", font_size = '30sp', color = (0,0,0,1))
        layout.add_widget(Welcome_label)

        boton_registo = Button(text = "Ir a registros", pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_registo.bind(on_press = self.cambiar_registro)
        layout.add_widget(boton_registo)

        boton_historial = Button(text = "Ir a Hitorial de gastos", pos_hint= {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_historial.bind = Label (on_press = self.cambiar_historial)
        layout.add_widget(boton_historial)

        self.add_widget(layout)

    def cambiar_registro (self, instance): 
        self.manager.current = 'registro'

    def cambiar_historial (self, instance):
        self.manager.current = 'historial'

class RegistroGastos(Screen): 
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

        Window.clearcolor= (1,1,1,1)

        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        self.producto_input = TextInput(hint_text = "Ingrese el producto", font_size = '16sp', multiline = False, size_hint_y= None, height = 60)
        self.layout.add_widget(self.producto_input)

        self.costo_input = TextInput(hint_text = "Ingrese el costo del producto", font_size = '16sp', multiline = False, size_hint_y = None, height = 60) 
        self.layout.add_widget(self.costo_input)

        agregar_button = Button(text = "Agregar producto", size_hint= (0.5, None), height = 100, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        agregar_button.bind(on_press = self.agregar_producto)
        self.layout.add_widget(agregar_button)

        self.resultado_label = Label (text = "")
        self.layout.add_widget(self.resultado_label)

        boton_volver = Button(text = "Volver",pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_volver.bind (on_press = self.volver_registro)
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)

        self.lista_precios = []
        self.producto-layout = None

    def volver_registro (self , instance):
        self.manager.current = 'inicio'
    
    def agregar_producto(self,instance): 
        producto = self.producto_input.text
        costo = float(self.costo_input.text)

        self.suma_total += costo
        
        producto_label = Label(text = f"{producto}: $ {costo}", font_size = '16sp', size_hint_y = None, height = 30, color = (0,0,0,1))
        self.lista_productos.add_widget(producto_label)

        self.producto_input.text = ""
        self.costo_input.text = ""
    
if __name__ == '__main__':
    Pantall_Inicio().run()

 



