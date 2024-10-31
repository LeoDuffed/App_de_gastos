from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.uix.scrollview import ScrollView 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.core.window import Window 

class app(App):
    def build(self): 
        Window.clearcolor = (0,0,0,1)

        layout = BoxLayout(orientation='vertical', padding = 20, scpacing = 10  )

        label_instruccion= Label (text = 'Esta App es para ir anotando tus gastos', font_size = '30sp', color = (1, 0, 0, 1))
        layout.add_widget(label_instruccion)

        self.producto_ingreso = TextInput(hint_text= 'Ingrese en que gasto', font_size = '16sp', multiline = False, size_hint_y = None, height = 60)
        layout.add_widget(self.producto_ingreso)

        self.costo_ingreso = TextInput(hint_text= 'Ingresa el costo de lo que acabas de ingresar', font_size = '16sp', multiline = False, size_hint_y= None, height = 60)
        layout.add_widget(self.costo_ingreso)

        agregar_boton = Button(text = 'Agregar', size_hint = (0.5, None ), height = 100, post_hint= {"center_x": 0.5}, background_color= (0,1,1,1)) 







        return layout 
    
if __name__ == '__main__': 
    app().run()
