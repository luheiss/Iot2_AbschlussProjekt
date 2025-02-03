from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import MainWindowModule as mw
import CircleAppModule as ca
import QuestionsModule as qm
from kivy.clock import Clock


# This class has to inherit from App, since it´s the class that´s called in the main
class MyScreenManagerApp(App):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(mw.MainWindow(name='main'))
        sm.add_widget(ca.CircleApp(name='circle'))
        sm.add_widget(qm.Question(name='picture'))
        
        return sm

