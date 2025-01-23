import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
kivy.require('1.10.1')

# Haupt-Anwendungsfenster
class Question(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        layout = BoxLayout()
        img = Image(source="pictures/Mechanik_Aufgabe.png")
        layout.add_widget(img)
        picturesButton = Button(text="Bild", size_hint_y=None, height=100)
        picturesButton.bind(on_press=self.on_change_main)
        layout.add_widget(picturesButton)
        self.add_widget(layout)

        
    def on_change_main(self, instance):
        self.manager.current = 'main'
    


