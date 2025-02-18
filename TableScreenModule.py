from screeninfo import get_monitors
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from RadomIntervalModule import RandomInterval

"""
-If we connect the raspy, it´s probably best to write an on_enter function to check the cups
-Sometimes a bug occurs after game over screen -> retry -> game start it switches almost instantly to the question (will fix later)
"""


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

    def get_is_red(self):
        return self.isred
    

class CircleApp(Screen):
    def __init__(self, **kwargs):
        super(CircleApp, self).__init__(**kwargs)

        #See docs in MainWindowModule
        Window.size = (Window.width, Window.height)
        Window.fullscreen = 'auto'
        Window.clearcolor = (1, 1, 1, 1)
        monitor = get_monitors()[0]
        windowWidth = monitor.width
        windowHeight = monitor.height
        layout = GridLayout(cols=3, padding=10, spacing=40)
        
        """TODO
            -Add list with all circleWidget
        """
        radius = (windowWidth/30)

        # Create circle widgets 
        self.circleWidget1 = CircleWidget(radius * 3, (windowHeight/5), radius)
        self.circleWidget2 = CircleWidget(radius * 6, (windowHeight/5) * 2, radius)
        self.circleWidget3 = CircleWidget(radius * 3, (windowHeight/5) * 3, radius)
        self.circleWidget4 = CircleWidget((windowWidth - radius * 4),(windowHeight/5), radius)
        self.circleWidget5 = CircleWidget((windowWidth - radius * 7),(windowHeight/5) * 2, radius)
        self.circleWidget6 = CircleWidget((windowWidth - radius * 4),(windowHeight/5) * 3, radius)

        self.teamOneCircles = [self.circleWidget1, self.circleWidget2, self.circleWidget3]
        self.teamTwoCircles = [self.circleWidget4, self.circleWidget5, self.circleWidget6]
        self.list_with_funcs = [self.on_change_color_button1, self.on_change_color_button2, self.on_change_color_button3, self.on_change_color_button4, self.on_change_color_button5, self.on_change_color_button6]
    
        # Add buttons and functionality
        for i in range(1, 7):
            button = Button(text=f"Button {i}", size_hint_y=None, height=100)
            button.bind(on_press=self.list_with_funcs[i-1])
            layout.add_widget(button)

        exitButton = Button(text="Fenster wechseln", size_hint_y=None, height=100)
        exitButton.bind(on_press=self.on_change_status)

        layout.add_widget(self.circleWidget1)  
        layout.add_widget(self.circleWidget2)  
        layout.add_widget(self.circleWidget3)   
        layout.add_widget(self.circleWidget4)   
        layout.add_widget(self.circleWidget5)   
        layout.add_widget(self.circleWidget6)   
        layout.add_widget(exitButton, index = 0)        
    
        self.add_widget(layout)
    
    #handler for changing color, instance parameter is required!
    #instance in Callback Funktionen, die z.B. durch Button ausgelöst werden
    #instace repräsentiert das Widget-Objekt (Button etc), dass das Ereignis ausgelöst hat
    def on_change_color_button1(self, instance):
        self.circleWidget1.change_color()
        if all(circle.get_is_red() for circle in self.teamOneCircles):
            self.manager.current = 'gameover'

    #DRY - don´t repeat yourself duh, add to todo 
    def on_change_color_button2(self, instance):
        self.circleWidget2.change_color()
        if all(circle.get_is_red() for circle in self.teamOneCircles):
            self.manager.current = 'gameover'

    def on_change_color_button3(self, instance):
        self.circleWidget3.change_color()
        if all(circle.get_is_red() for circle in self.teamOneCircles):
            self.manager.current = 'gameover'

    def on_change_color_button4(self, instance):
        self.circleWidget4.change_color()
        if all(circle.get_is_red() for circle in self.teamTwoCircles):
            self.manager.current = 'gameover'

    def on_change_color_button5(self, instance):
        self.circleWidget5.change_color()
        if all(circle.get_is_red() for circle in self.teamTwoCircles):
            self.manager.current = 'gameover'

    def on_change_color_button6(self, instance):
        self.circleWidget6.change_color()
        if all(circle.get_is_red() for circle in self.teamTwoCircles):
            self.manager.current = 'gameover'
    
    #on_enter ist keine vordefinierte Funktion, wird aber vom ScreenManager automatisch aufgerufen wenn dieser Fenster erscheint
    #on_leave wäre, wenn Fenster in Hintergrund rückt
    def on_enter(self):
        # Random Timer starten, wenn dieses Fenster betreten wird
        interval = RandomInterval.get_random_interval()
        Clock.schedule_once(self.go_to_third_screen, interval)

    #Argument dt (delta time) wird von Clock automatisch an die Klasse übergeben
    def go_to_third_screen(self, dt):
        if self.manager.current =='circle':
            self.manager.current = 'picture'

    def on_change_status(self, instance):
        self.manager.current = 'main'