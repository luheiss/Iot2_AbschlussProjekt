import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from RadomIntervalModule import RandomInterval
import random
kivy.require('1.10.1')

# Class for questions and pictures
class Question(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        title = Label(text='!!Aufgabe!!', font_size='24sp', size_hint=(1, 0.2))
        layout.add_widget(title)

        imgQuestion = Image(source="pictures/Mechanik_Aufgabe.png")
        imgQuestion.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        layout.add_widget(imgQuestion)

        topButtonsLayout = BoxLayout(orientation='horizontal', spacing=10)
       
        answerOneButton = Button(text="Antwort 1", size_hint_y=None, height=100)
        answerOneButton.bind(on_press=self.answer_one)
        topButtonsLayout.add_widget(answerOneButton)

        answerTwoButton = Button(text="Antwort 2", size_hint_y=None, height=100)
        answerTwoButton.bind(on_press=self.answer_two)
        topButtonsLayout.add_widget(answerTwoButton)

        answerThreeButton = Button(text="Antwort 3", size_hint_y=None, height=100)
        answerThreeButton.bind(on_press=self.answer_three)
        topButtonsLayout.add_widget(answerThreeButton)
        
        answerFourButton = Button(text="Antwort 4", size_hint_y=None, height=100)
        answerFourButton.bind(on_press=self.answer_four)
        topButtonsLayout.add_widget(answerFourButton)

        picturesButton = Button(text="Fertig", size_hint_x = 0.5, size_hint_y = None, height=100)
        picturesButton.bind(on_press=self.on_change_main)
        picturesButton.pos_hint = {'center_x' : 0.5}

        layout.add_widget(topButtonsLayout)
        layout.add_widget(picturesButton)
        self.add_widget(layout)

    def on_leave(self):
        RandomInterval.set_random_interval()
        
    def on_change_main(self, instance):
        self.manager.current = 'circle'

    def answer_one(self, instance):
        pass
    
    def answer_two(self, instance):
        pass
    
    def answer_three(self, instance):
        pass
    
    def answer_four(self, instance):
        pass
    


