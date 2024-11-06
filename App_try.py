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

        boton_registo = Button(text = "Ir a registros", pos_hint = {"center_x": 0.5}, background_color = (0.6, 1, 0.6, 1))
        boton_registo.bind(on_press = self.cambiar_registro)
        layout.add_widget(boton_registo)

        boton_historial = Button(text = "Ir a Hitorial de gastos", pos_hint= {"center_x": 0.5}, background_color = (0.5, 1, 0, 1))
        boton_historial.bind(on_press = self.cambiar_historial)
        layout.add_widget(boton_historial)

        self.add_widget(layout)

    def cambiar_registro (self, instance): 
        self.manager.current = 'registro'

    def cambiar_historial (self, instance):
        self.manager.current = 'historial'

class RegistroGastos(Screen): 
    def __init__(self, **kwargs):  
        super().__init__(**kwargs)

        Window.clearcolor= (0,0,0,1)

        self.layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        self.producto_input = TextInput(hint_text = "Ingrese el producto", multiline = False, font_size = '16sp',size_hint = (0.5, None), size_hint_y = None, height = 80)
        self.layout.add_widget(self.producto_input)

        self.precio_input = TextInput(hint_text = "Ingrese el costo del producto", multiline = False, font_size = '16sp',size_hint = (0.5, None), size_hint_y = None, height = 80) 
        self.layout.add_widget(self.precio_input)

        agregar_button = Button(text="Agregar producto", size_hint= (0.5, None), height = 100, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        agregar_button.bind(on_press=self.agregar_producto)
        self.layout.add_widget(agregar_button)

        self.resultado_label = Label(text="")
        self.layout.add_widget(self.resultado_label)

        boton_volver = Button(text = "Volver",pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_volver.bind(on_press = self.volver_registro)
        self.layout.add_widget(boton_volver)

        self.add_widget(self.layout)

        self.lista_precios = []

    def volver_registro (self , instance):
        self.manager.current = 'inicio'
    
    def agregar_producto(self,instance):  
        nom_product  =  self.producto_input.text
        try: 
            precio = float(self.precio_input.text)
            self.lista_precios.append ((nom_product, precio))

            self.producto_input.text = ""
            self.precio_input.text = ""
            self.resultado_label.text = "Producto Agregado"
        except ValueError:
            self.resultado_label.text= "Ingrese un precio valido"

class Historial (Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout (orientation = 'vertical', padding = 20, spacing = 10)

        self.scroll_view = ScrollView(size_hint = (1, None), size = (Window.width, 300))
        self.productos_layout = GridLayout (cols = 1, spacing = 10, size_hint_y = None)
        self.productos_layout.bind(minimum_height = self.productos_layout.setter ('height'))
        self.scroll_view.add_widget(self.productos_layout)
        layout.add_widget(self.scroll_view)

        boton_calcular_total = Button(text = "Calcular Total")
        boton_calcular_total.bind(on_press = self.calcular_total)
        layout.add_widget(boton_calcular_total)

        self.total_label = Label(text = "")
        layout.add_widget(self.total_label)

        boton_volver = Button(text = "Volver",pos_hint = {"center_x": 0.5}, background_color = (0,1,0,1))
        boton_volver.bind (on_press = self.volver_registro)
        layout.add_widget(boton_volver)

        self.add_widget(layout)

    def volver_registro (self , instance):
        self.manager.current = 'inicio'

    def calcular_total(self, instance):
        total = sum (precio for nombre, precio in App.get_running_app().root.get_screen('registro').lista_precios)
        self.total_label.text = f"Total gastado: ${total:.2f}"

    def on_enter(self):
        self.productos_layout.clear_widgets()
        productos = App.get_running_app().root.get_screen('registro').lista_precios
        for nombre, precio in productos: 
            etiqueta = Label(text = f"{nombre} - ${precio:.2f}", size_hint_y = None, height = 40)
            self.productos_layout.add_widget(etiqueta)

class GastosApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(Pantall_Inicio(name = 'inicio'))
        sm.add_widget(RegistroGastos(name = 'registro'))
        sm.add_widget(Historial(name = 'historial'))
        return sm 


GastosApp().run()



