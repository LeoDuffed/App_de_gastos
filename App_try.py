from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput
from kivy.core.window import Window 

class Aplication(App): 
    def build(self): 

        Window.clearcolor= (1,1,1,1)

        layout = BoxLayout(orientation = 'vertical', padding = 20, spacing = 10)

        intruction_label = Label(text = "Ingresa el producto y su costo", font_size = '30sp', color = (0,0,0,1))
        layout.add_widget(intruction_label)

        self.producto_input = TextInput(hint_text = "Ingrese el producto", font_size = '16sp', multiline = False, size_hint_y= None, height = 60)
        layout.add_widget(self.producto_input)

        self.costo_input = TextInput(hint_text = "Ingrese el costo del producto", font_size = '16sp', multiline = False, size_hint_y = None, height = 60) 
        layout.add_widget(self.costo_input)

        agregar_button1 = Button(text = "Agregar producto", size_hint= (0.5, None), height = 100, pos_hint = {"center_x":0.5}, background_color = (0,1,0,1))
        agregar_button1.bind(on_press = self.agregar_producto)
        layout.add_widget(agregar_button1)

        scroll_view = ScrollView(size_hint = (1, None), height = 200)
        self.lista_productos = BoxLayout (orientation = 'vertical', size_hint_y = None)
        self.lista_productos.bind (minimum_height = self.lista_productos.setter('height'))
        scroll_view.add_widget(self.lista_productos)
        layout.add_widget(scroll_view)

        self.suma_total = 0 

        return layout
    def agregar_producto(self,instance): 
        producto = self.producto_input.text
        costo = float(self.costo_input.text)

        self.suma_total += costo
        
        producto_label = Label(text = f"{producto}: $ {costo}", font_size = '16sp', size_hint_y = None, height = 30, color = (0,0,0,1))
        self.lista_productos.add_widget(producto_label)

        self.producto_input.text = ""
        self.costo_input.text = ""
    
if __name__ == '__main__':
    Aplication().run()

 



