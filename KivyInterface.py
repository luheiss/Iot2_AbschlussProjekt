from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse

globalState = 1

class CircleWidget(Widget):
    def __init__(self, posx : int, posy : int, radius : float, **kwargs):
        super().__init__(**kwargs)
        self.posy = posy
        self.posx = posx
        self.radius = radius
        with self.canvas:
            self.isred = False
            # Initiale Farbe und Kreis zeichnen
            self.color_instruction = Color(0, 0, 1, 1)  # Blau in RGBA
            self.ellipse = Ellipse(pos=(self.posx, self.posy), size=(2*self.radius, 2*self.radius))

    def change_color(self):
        self.isred = not self.isred
        # Farbe direkt ändern
        if self.isred == True:
            self.color_instruction.rgba = (1, 0, 0, 1)
        else:
            self.color_instruction.rgba = (0, 0, 1, 1)

class CircleApp(App):
    def build(self):
        # Fenstergröße auf Bildschirmgröße setzen
        Window.size = (Window.width, Window.height)
        # Optional: Fenster in den Vollbildmodus setzen
        Window.fullscreen = 'auto'
        # Hintergrundfarbe auf Weiß setzen
        Window.clearcolor = (1, 1, 1, 1)

        # Hauptlayout erstellen
        layout = GridLayout(cols=3, padding=10, spacing=40)

        # Kreis-Widget erstellen
        self.circle_widget1 = CircleWidget(200,200,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget2 = CircleWidget(400,400,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget3 = CircleWidget(200,600,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget4 = CircleWidget(1400,200,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget5 = CircleWidget(1200,400,50.0, size_hint=(None, None), size=(100, 100))
        self.circle_widget6 = CircleWidget(1400,600,50.0, size_hint=(None, None), size=(100, 100))

        
        self.list_with_funcs = [self.on_change_color_button1, self.on_change_color_button2, self.on_change_color_button3, self.on_change_color_button4, self.on_change_color_button5, self.on_change_color_button6]

        # Buttons hinzufügen
        for i in range(1, 7):
            button = Button(text=f"Button {i}", size_hint_y=None, height=100)
            button.bind(on_press=self.list_with_funcs[i-1])
            print(i)
            layout.add_widget(button)

        exitButton = Button(text="Fenster wechseln", size_hint_y = None, height=100)
        exitButton.bind(on_pess=self.on_change_status)
        layout.add_widget(exitButton)        
        layout.add_widget(self.circle_widget1, index=0)  # Kreis zuerst hinzufügen
        layout.add_widget(self.circle_widget2, index=0)  # Kreis zuerst hinzufügen
        layout.add_widget(self.circle_widget3, index=0)  # Kreis zuerst hinzufügen
        layout.add_widget(self.circle_widget4, index=0)  # Kreis zuerst hinzufügen
        layout.add_widget(self.circle_widget5, index=0)  # Kreis zuerst hinzufügen
        layout.add_widget(self.circle_widget6, index=0)  # Kreis zuerst hinzufügen
        return layout

    #handler for changing color, instance is needed!
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
    
    def on_change_status(self, instance):
        global globalState
        globalState = 1



class MainWindow(App):
    def build(self):
        # Fenstergröße auf Bildschirmgröße setzen
        Window.size = (Window.width, Window.height)
        # Optional: Fenster in den Vollbildmodus setzen
        Window.fullscreen = 'auto'
        # Hintergrundfarbe auf Weiß setzen
        Window.clearcolor = (1, 1, 1, 1)
        # Hauptlayout erstellen
        layout = GridLayout(cols=3, padding=10, spacing=40)

        exitButton = Button(text="Fenster wechseln", size_hint_y=None, height=100)
        exitButton.bind(on_press=self.on_change_status)
        layout.add_widget(exitButton)        
        
        return layout
        
    def on_change_status(self, instance):
        global globalState
        globalState = 2
        print(f"Global State in MainWindow: {globalState}")


if __name__ == '__main__':
    if globalState == 1:
        MainWindow().run()
    elif globalState == 2:
        CircleApp().run()
