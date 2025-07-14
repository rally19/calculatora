import os
import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class CalculatoraApp(App):
    def build(self):
        self.icon = resource_path('icon.ico')
        Window.size = (400, 400)
        
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        self.hasil = Label(text="Hasil: ", font_size=32, size_hint=(1, 0.1))
        layout.add_widget(self.hasil)
        
        layout.add_widget(Label(text="Nilai a:", size_hint=(1, 0.05)))
        self.input_a = TextInput(multiline=False, font_size=24, size_hint=(1, 0.1))
        layout.add_widget(self.input_a)
        
        layout.add_widget(Label(text="Nilai b:", size_hint=(1, 0.05)))
        self.input_b = TextInput(multiline=False, font_size=24, size_hint=(1, 0.1))
        layout.add_widget(self.input_b)
        
        operators = ['+', '-', '*', '/']
        btn_layout = BoxLayout(spacing=5, size_hint=(1, 0.1))
        
        for op in operators:
            btn = Button(text=op, font_size=24)
            btn.bind(on_press=self.calculate)
            btn_layout.add_widget(btn)
        
        layout.add_widget(btn_layout)
        
        clear_btn = Button(text="Reset", font_size=24, size_hint=(1, 0.1))
        clear_btn.bind(on_press=self.reset)
        layout.add_widget(clear_btn)
        
        return layout
    
    def calculate(self, instance):
        try:
            a = float(self.input_a.text)
            b = float(self.input_b.text)
            operator = instance.text
            
            operations = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y if y != 0 else "Dibagi nol kagak bisa coy!"
            }
            
            if operator in operations:
                hasil = operations[operator](a, b)
                self.hasil.text = f"Hasil: {hasil}"
            else:
                self.hasil.text = "Error: Operator macam apa ini?"
        except ValueError:
            self.hasil.text = "Error: Input macam apa ini?"
    
    def reset(self, instance):
        self.input_a.text = ""
        self.input_b.text = ""
        self.hasil.text = "Hasil: "

if __name__ == '__main__':
    CalculatoraApp().run()

# Made by rally19