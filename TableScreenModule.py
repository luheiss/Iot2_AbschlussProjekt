from screeninfo import get_monitors
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from BLE_Search import get_modul_daten  # Holt ESP32-Daten
from RadomIntervalModule import RandomInterval  # Fügt zufällige Wartezeit hinzu


class CircleWidget(Widget):
    def __init__(self, posx: int, posy: int, radius: float, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        with self.canvas:
            self.color_instruction = Color(0, 0, 1, 1)  # Standard: Blau (Cup ist voll)
            self.ellipse = Ellipse(pos=(posx, posy), size=(2 * radius, 2 * radius))

    def set_color(self, is_red):
        """Setzt die Farbe: Blau (False) für 1, Rot (True) für 0."""
        self.color_instruction.rgba = (1, 0, 0, 1) if is_red else (0, 0, 1, 1)


class CircleApp(Screen):
    def __init__(self, **kwargs):
        super(CircleApp, self).__init__(**kwargs)

        # Bildschirmgröße holen
        monitor = get_monitors()[0]
        windowWidth = monitor.width
        windowHeight = monitor.height
        Window.size = (windowWidth, windowHeight)
        Window.fullscreen = 'auto'
        Window.clearcolor = (1, 1, 1, 1)

        # Layout für das UI
        self.layout = GridLayout(cols=3, padding=10, spacing=40)
        self.radius = windowWidth / 30

        # Erstelle Kreis-Widgets
        self.circleWidget1 = CircleWidget(self.radius * 3, (windowHeight / 5), self.radius)
        self.circleWidget2 = CircleWidget(self.radius * 6, (windowHeight / 5) * 2, self.radius)
        self.circleWidget3 = CircleWidget(self.radius * 3, (windowHeight / 5) * 3, self.radius)
        self.circleWidget4 = CircleWidget((windowWidth - self.radius * 4), (windowHeight / 5), self.radius)
        self.circleWidget5 = CircleWidget((windowWidth - self.radius * 7), (windowHeight / 5) * 2, self.radius)
        self.circleWidget6 = CircleWidget((windowWidth - self.radius * 4), (windowHeight / 5) * 3, self.radius)

        # Speichert, ob das ESP32-Modul verbunden ist
        self.esp1_connected = False
        self.esp2_connected = False

        # Startet regelmäßige Updates der Sensordaten
        Clock.schedule_interval(self.update_circle_colors, 0.5)

        self.add_widget(self.layout)  # Grid ins Hauptlayout setzen

    def update_circle_colors(self, dt):
        """Holt die aktuellen Sensorwerte und setzt die Farben der Kreise."""
        modulOne = get_modul_daten("ESP_Modul1")
        modulTwo = get_modul_daten("ESP_Modul2")

        # Prüfe, ob ESP32-Module verbunden sind
        esp1_now_connected = modulOne and modulOne.get("Cup1") is not None
        esp2_now_connected = modulTwo and modulTwo.get("Cup1") is not None

        # Falls sich der Verbindungsstatus geändert hat, Layout neu laden
        if esp1_now_connected != self.esp1_connected or esp2_now_connected != self.esp2_connected:
            self.esp1_connected = esp1_now_connected
            self.esp2_connected = esp2_now_connected
            self.reload_layout()

        # Falls ESP1 verbunden ist, aktualisiere die Farben
        if self.esp1_connected:
            self.circleWidget1.set_color(modulOne.get("Cup1", 1) == 0)
            self.circleWidget2.set_color(modulOne.get("Cup2", 1) == 0)
            self.circleWidget3.set_color(modulOne.get("Cup3", 1) == 0)

        # Falls ESP2 verbunden ist, aktualisiere die Farben
        if self.esp2_connected:
            self.circleWidget4.set_color(modulTwo.get("Cup1", 1) == 0)
            self.circleWidget5.set_color(modulTwo.get("Cup2", 1) == 0)
            self.circleWidget6.set_color(modulTwo.get("Cup3", 1) == 0)

        # Falls alle Kreise eines Teams rot sind → Game Over
        if self.esp1_connected and all(circle.color_instruction.rgba == (1, 0, 0, 1) for circle in [self.circleWidget1, self.circleWidget2, self.circleWidget3]):
            self.manager.current = 'gameover'
        if self.esp2_connected and all(circle.color_instruction.rgba == (1, 0, 0, 1) for circle in [self.circleWidget4, self.circleWidget5, self.circleWidget6]):
            self.manager.current = 'gameover'

    def reload_layout(self):
        """Aktualisiert das Layout basierend auf der ESP32-Verbindung."""
        self.layout.clear_widgets()

        if self.esp1_connected:
            self.layout.add_widget(self.circleWidget1)
            self.layout.add_widget(self.circleWidget2)
            self.layout.add_widget(self.circleWidget3)

        if self.esp2_connected:
            self.layout.add_widget(self.circleWidget4)
            self.layout.add_widget(self.circleWidget5)
            self.layout.add_widget(self.circleWidget6)

        # "Fenster wechseln"-Button hinzufügen
        #exitButton = Button(text="Fenster wechseln", size_hint_y=None, height=100)
        #exitButton.bind(on_press=self.on_change_status)
        #self.layout.add_widget(exitButton, index=0)

    def on_enter(self):
        """Startet das regelmäßige Update & den zufälligen Timer beim Betreten des Fensters."""
        Clock.schedule_interval(self.update_circle_colors, 0.5)

        # Startet zufälliges Intervall für Bildschirmwechsel
        interval = RandomInterval.get_random_interval()
        Clock.schedule_once(self.go_to_next_screen, interval)

    def on_leave(self):
        """Stoppt das Update, wenn der Screen verlassen wird."""
        Clock.unschedule(self.update_circle_colors)

    def go_to_next_screen(self, dt):
        """Wechselt zufällig zum nächsten Screen."""
        if self.manager.current == 'circle':
            self.manager.current = 'picture'

    def on_change_status(self, instance):
        """Wechselt zum nächsten Fenster, wenn der Button gedrückt wird."""
        self.manager.current = 'main'
