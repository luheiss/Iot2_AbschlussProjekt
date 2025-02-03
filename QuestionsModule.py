import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from RadomIntervalModule import RandomInterval
import random
kivy.require('1.10.1')

# Class for questions and pictures
class Question(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        layout = GridLayout(cols=3, padding=10, spacing=40)
        img = Image(source="pictures/Mechanik_Aufgabe.png")
        layout.add_widget(img)

        answerOneButton = Button()
        answerTwoButton = Button()
        answerThreeButton = Button()
        answerFourBurron = Button()
        picturesButton = Button(text="Fertig", size_hint_y=None, height=100)
        picturesButton.bind(on_press=self.on_change_main)
        layout.add_widget(picturesButton)
        self.add_widget(layout)

        
    def on_change_main(self, instance):
        self.manager.current = 'circle'
        RandomInterval.set_random_interval()

    def on_enter(self):
        randomQuestion = random.randint()

    


