from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.scrollview import ScrollView 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.core.window import Window 

class app(App):

    def build(self): 
        # Poner todos los widgets :)
        Window.clearcolor = (1,1,1,1)

        layout = BoxLayout(orientation='vertical', padding = 20, spacing = 10  )

        label_instruccion= Label (text = 'Esta App es para ir anotando tus gastos', font_size = '20sp', color = (1, 0, 0, 1))
        layout.add_widget(label_instruccion)

        self.producto_ingreso = TextInput(hint_text= 'Ingrese en que gasto', font_size = '16sp', multiline = False, size_hint_y = None, height = 60)
        layout.add_widget(self.producto_ingreso)

        self.costo_ingreso = TextInput(hint_text= 'Ingresa el costo de lo que acabas de ingresar', font_size = '16sp', multiline = False, size_hint_y= None, height = 60)
        layout.add_widget(self.costo_ingreso)

        agregar_boton = Button(text = "Agregar", size_hint = (0.5, None ), height = 100, pos_hint= {"center_x": 0.5}, background_color= (0,1,0,1)) 
        agregar_boton.bind(on_press = self.agregar_producto)
        layout.add_widget(agregar_boton)

        agregar_boton2 = Button(text = "Gastos totales", size_hint = (0.5, None), height = 90, pos_hint = {"center_x": 0.5}, background_color= (0,1,1,1,))
        agregar_boton2.bind (on_press = self.agregar_producto)
        layout.add_widget(agregar_boton2)

        scroll_view = ScrollView(size_hint= (1, None), height = 200)
        self.lista_producto = BoxLayout (orientation = 'vertical', size_hint_y= None)
        self.lista_producto.bind (minimun_height = self.lista_producto.setter('height'))
        scroll_view.add_widget(self.lista_producto)
        layout.add_widget(scroll_view)

        scrool_view = ScrollView(size_hint= (1, None), height = 200) 
        self.lista_precios = BoxLayout (orientation = 'vertical', size_hint_y = None)
        self.lista_precios.bind (minimun_height = self.lista_precios.setter('height'))
        scroll_view.add_widget(self.lista_precios)
        layout.add_widget(scroll_view)

        self.suma_total = 0

        return layout

    def agregar_producto(self, instance):
        producto = self.producto_input.text
#        try: 
#            costo = float(self.costo_input.text)
#            self.suma_total += costo
#            self.suma_lebel.text = f"Suma total: {self.suma_total}"









        return layout 
    
if __name__ == '__main__': 
    app().run()
