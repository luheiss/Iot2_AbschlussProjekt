import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from RadomIntervalModule import RandomInterval
import random
import json
kivy.require('1.10.1')

# Class for questions and pictures
class Question(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('Questions.json', 'r') as file:
            self.data = json.load(file)
        self.question = 0
        self.randomQuestion = list(range(1,len(self.data["Questions"].keys())+1 ))
        random.shuffle(self.randomQuestion)
        
        title = Label(text='!!Aufgabe!!', font_size='24sp', size_hint=(1, 0.2),  color=[1, 0, 0, 1])
       
        self.layout = BoxLayout(orientation = "vertical", padding = 10, spacing = 10)
        self.layout.add_widget(title)
        self.imgQuestion = Image()
        self.imgQuestion.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.layout.add_widget(self.imgQuestion)        

        topButtonsLayout = BoxLayout(orientation='horizontal', spacing=10)
       
        self.answerOneButton = Button( size_hint_y=None, height=100)
        self.answerOneButton.bind(on_press=self.answer_one)
        topButtonsLayout.add_widget(self.answerOneButton)

        self.answerTwoButton = Button(text="Antwort 2", size_hint_y=None, height=100)
        self.answerTwoButton.bind(on_press=self.answer_two)
        topButtonsLayout.add_widget(self.answerTwoButton)

        self.answerThreeButton = Button(text="Antwort 3", size_hint_y=None, height=100)
        self.answerThreeButton.bind(on_press=self.answer_three)
        topButtonsLayout.add_widget(self.answerThreeButton)
        
        self.answerFourButton = Button(text="Antwort 4", size_hint_y=None, height=100)
        self.answerFourButton.bind(on_press=self.answer_four)
        topButtonsLayout.add_widget(self.answerFourButton)

        picturesButton = Button(text="Fertig", size_hint_x = 0.5, size_hint_y = None, height=100)
        picturesButton.bind(on_press=self.on_change_main)
        picturesButton.pos_hint = {'center_x' : 0.5}

        self.layout.add_widget(topButtonsLayout)
        self.layout.add_widget(picturesButton)
        self.add_widget(self.layout)
        
    def on_enter(self, instance=None):
        # Aktualisiere den Bildpfad und setze das Bild neu
        self.path = self.data["Questions"][str(self.randomQuestion[self.question])]["picturePath"]
        self.answerOneButton.text = self.data["Questions"][str(self.randomQuestion[self.question])]["answers"][0]
        self.answerTwoButton.text = self.data["Questions"][str(self.randomQuestion[self.question])]["answers"][1]
        self.answerThreeButton.text = self.data["Questions"][str(self.randomQuestion[self.question])]["answers"][2]
        self.answerFourButton.text = self.data["Questions"][str(self.randomQuestion[self.question])]["answers"][3]
        self.imgQuestion.source = self.path
        self.answerTwoButton.background_color = (1, 1, 1, 1)
        self.answerOneButton.background_color = (1, 1, 1, 1)
        self.answerThreeButton.background_color = (1, 1, 1, 1)
        self.answerFourButton.background_color = (1, 1, 1, 1)
        
        # Fancy way to increment to the numbers of len and then start with 0 over if it exceeds the length
        self.question = (self.question + 1) % len(self.data["Questions"].keys())
        
    def on_leave(self):
        RandomInterval.set_random_interval()
        
    def on_change_main(self, instance):
        self.manager.current = 'circle'

    def answer_one(self, instance):
        if self.data["Questions"][str(self.randomQuestion[self.question])]["correctAnswer"] == 1:
            self.answerOneButton.background_color=(0, 1, 0, 1)
            self.answerTwoButton.background_color=(1, 0, 0, 1)
            self.answerThreeButton.background_color=(1, 0, 0, 1)
            self.answerFourButton.background_color=(1, 0, 0, 1)
    
    def answer_two(self, instance):
        if self.data["Questions"][str(self.randomQuestion[self.question])]["correctAnswer"] == 2:
            self.answerTwoButton.background_color=(0, 1, 0, 1)
            self.answerOneButton.background_color=(1, 0, 0, 1)
            self.answerThreeButton.background_color=(1, 0, 0, 1)
            self.answerFourButton.background_color=(1, 0, 0, 1)
    
    def answer_three(self, instance):
        if self.data["Questions"][str(self.randomQuestion[self.question])]["correctAnswer"] == 3:
            self.answerThreeButton.background_color=(0, 1, 0, 1)
            self.answerOneButton.background_color=(1, 0, 0, 1)
            self.answerTwoButton.background_color=(1, 0, 0, 1)
            self.answerFourButton.background_color=(1, 0, 0, 1)
    
    def answer_four(self, instance):
        if self.data["Questions"][str(self.randomQuestion[self.question])]["correctAnswer"] == 4:    
            print("Antwort 4 ist wahr")
            self.answerFourButton.background_color=(0, 1, 0, 1)
            self.answerOneButton.background_color=(1, 0, 0, 1)
            self.answerTwoButton.background_color=(1, 0, 0, 1)
            self.answerThreeButton.background_color=(1, 0, 0, 1)
