from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen

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
        layout = GridLayout(cols=3, padding=10, spacing=40)

        circleButton = Button(text="Kreis", size_hint_y=None, height=100)
        circleButton.bind(on_press=self.on_change_circle)
        picturesButton = Button(text="Bild", size_hint_y=None, height=100)
        picturesButton.bind(on_press=self.on_change_picture)
        layout.add_widget(circleButton)
        layout.add_widget(picturesButton)        
        self.add_widget(layout)

    def on_change_circle(self, instance):
        self.manager.current = 'circle'
    def on_change_picture(self, instance):
        self.manager.current = 'picture'