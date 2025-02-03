from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from RadomIntervalModule import RandomInterval


#if it´s a class for shape, it has to inherit from Widget
class CircleWidget(Widget):
    def __init__(self, posx : int, posy : int, radius : float, **kwargs):
        super().__init__(**kwargs)
        self.posy = posy
        self.posx = posx
        self.radius = radius
        with self.canvas:
            self.isred = False
            # draw initial color and circle
            self.color_instruction = Color(0, 0, 1, 1)  # blue in RGBA values
            self.ellipse = Ellipse(pos=(self.posx, self.posy), size=(2*self.radius, 2*self.radius))

    def change_color(self):
        self.isred = not self.isred
        #change color, siwtching from blue to red
        if self.isred == True:
            self.color_instruction.rgba = (1, 0, 0, 1)
        else:
            self.color_instruction.rgba = (0, 0, 1, 1)


class CircleApp(Screen):
    def __init__(self, **kwargs):
        super(CircleApp, self).__init__(**kwargs)

        #See docs in MainWindowModule
        Window.size = (Window.width, Window.height)
        Window.fullscreen = 'auto'
        Window.clearcolor = (1, 1, 1, 1)
        layout = GridLayout(cols=3, padding=10, spacing=40)
  
        # Create circle widgets 
        self.circle_widget1 = CircleWidget(200,150,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget2 = CircleWidget(400,350,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget3 = CircleWidget(200,550,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget4 = CircleWidget(1400,150,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget5 = CircleWidget(1200,350,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget6 = CircleWidget(1400,550,50.0, size_hint=(None, None), size=(100, 100))
        self.list_with_funcs = [self.on_change_color_button1, self.on_change_color_button2, self.on_change_color_button3, self.on_change_color_button4, self.on_change_color_button5, self.on_change_color_button6]
    
        # Add buttons and functionality
        for i in range(1, 7):
            button = Button(text=f"Button {i}", size_hint_y=None, height=100)
            button.bind(on_press=self.list_with_funcs[i-1])
            layout.add_widget(button)

        exitButton = Button(text="Fenster wechseln", size_hint_y=None, height=100)
        exitButton.bind(on_press=self.on_change_status)

        layout.add_widget(exitButton)        
        layout.add_widget(self.circle_widget1, index=0)  
        layout.add_widget(self.circle_widget2, index=0)  
        layout.add_widget(self.circle_widget3, index=0)   
        layout.add_widget(self.circle_widget4, index=0)   
        layout.add_widget(self.circle_widget5, index=0)   
        layout.add_widget(self.circle_widget6, index=0)   
        self.add_widget(layout)
        
    
    #handler for changing color, instance parameter is required!
    #instance in Callback Funktionen, die z.B. durch Button ausgelöst werden
    #instace repräsentiert das Widget-Objekt (Button etc), dass das Ereignis ausgelöst hat
    def on_change_color_button1(self, instance):
        self.circle_widget1.change_color()
    def on_change_color_button2(self, instance):
        self.circle_widget2.change_color()
    def on_change_color_button3(self, instance):
        self.circle_widget3.change_color()
    def on_change_color_button4(self, instance):
        self.circle_widget4.change_color()
    def on_change_color_button5(self, instance):
        self.circle_widget5.change_color()
    def on_change_color_button6(self, instance):
        self.circle_widget6.change_color()
    
    #on_enter ist keine vordefinierte Funktion, wird aber vom ScreenManager automatisch aufgerufen wenn dieser Fenster erscheint
    #on_leave wäre, wenn Fenster in Hintergrund rückt
    def on_enter(self):
        # Random Timer starten, wenn dieses Fenster betreten wird
        interval = RandomInterval.get_random_interval()
        Clock.schedule_once(self.go_to_third_screen, interval)

    #Argument dt (delta time) wird von Clock automatisch an die Klasse übergeben
    def go_to_third_screen(self, dt):
        self.manager.current = 'picture'

    def on_change_status(self, instance):
        self.manager.current = 'main'