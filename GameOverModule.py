from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

class GameOverScreen(Screen):
    def __init__(self, **kwargs):
        super(GameOverScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        gameOverLabel = Label(text='GAME OVER', font_size='40sp', size_hint=(1, 0.5), color=[1, 0, 0, 1])
        gameOverLabel.pos_hint = {'cencter_x' : 0.5}
        layout.add_widget(gameOverLabel)
        
        buttonLayout = BoxLayout(orientation='horizontal', spacing=10)
        retryButton = Button(text='Nochmal', size_hint_x = 0.5, size_hint_y = None, height = 100)
        retryButton.bind(on_press=self.retry_button)
        buttonLayout.add_widget(retryButton)
        
        exitButton = Button(text='Beenden', size_hint_x = 0.5, size_hint_y = None, height = 100)
        exitButton.bind(on_press=self.exit_button)
        buttonLayout.add_widget(exitButton)
        
        layout.add_widget(buttonLayout)
        self.add_widget(layout)

    def exit_button(self, instance):
        App.get_running_app().stop()

    def retry_button(self, instance):
        self.manager.current = 'main'