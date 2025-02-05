from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

#if the class is used as one screen out of many, it has to inherit Screen
class MainWindow(Screen):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        # Set windowsize to screensize
        Window.size = (Window.width, Window.height)
        Window.fullscreen = 'auto'
        # Backgroundcolor white
        Window.clearcolor = (1, 1, 1, 1)
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        gameOverLabel = Label(text='START THE GAME', font_size='40sp', size_hint=(1, 0.5), color=[1, 0, 0, 1])
        gameOverLabel.pos_hint = {'cencter_x' : 0.5}
        layout.add_widget(gameOverLabel)
        
        buttonLayout = BoxLayout(orientation='horizontal', spacing=10)
        circleButton = Button(text='Spiel starten', size_hint_x = 0.5, size_hint_y = None, height = 100)
        circleButton.bind(on_press=self.on_change_circle)
        buttonLayout.add_widget(circleButton)
        
        
        layout.add_widget(buttonLayout)
        self.add_widget(layout)
    

    def on_change_circle(self, instance):
        self.manager.current = 'circle'
    
   
