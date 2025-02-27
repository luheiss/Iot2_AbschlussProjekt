![GitHub repo size](https://img.shields.io/github/repo-size/luheiss/Iot2_AbschlussProjekt)
![GitHub last commit](https://img.shields.io/github/last-commit/luheiss/Iot2_AbschlussProjekt)
![GitHub stars](https://img.shields.io/github/stars/luheiss/Iot2_AbschlussProjekt)
![GitHub issues](https://img.shields.io/github/issues/luheiss/Iot2_AbschlussProjekt)


# IoT2 Abschlussprojekt: 3D-Drucker-Wartezeitüberbrückungsmodul

Dieses Projekt ist eine digitale Umsetzung des beliebten Spiels BeerPong. Ziel ist es, mithilfe eines Raspberry Pi und entsprechender Software eine smarte, automatisierte Version des Spiels zu realisieren.

## Installation auf dem Raspberry Pi

### 1. Vorbereitung

Erstelle ein neues Verzeichnis und wechsle in dieses:
```bash
mkdir ProjektBeerPong
cd ProjektBeerPong
```

### 2. Repository klonen

Klonen des Git-Repositories

### 3. Virtuelle Umgebung einrichten

Erstelle eine virtuelle Umgebung im Verzeichnis:

```bash
python3 -m venv .venv
```

Aktiviere die virtuelle Umgebung:
```bash
source .venv/bin/activate
```

### 5. Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 6. Start-Skript ausführbar machen
```bash
sudo chmod +x start_script.sh
´´´

### 7. Autostart-Service einrichten

Erstelle eine neue Service-Datei:
```bash
sudo nano /etc/systemd/system/projekt_beerpong.service
```
Füge folgenden Inhalt ein:
```bash
[Unit]
Description=Projekt BeerPong Autostart
After=network.target

[Service]
ExecStart=/bin/bash /home/ParryHotter/ProjektBeerPong/start_script.sh
WorkingDirectory=/home/ParryHotter/ProjektBeerPong
StandardOutput=inherit
StandardError=inherit
Restart=always
User=ParryHotter

[Install]
WantedBy=multi-user.target
```
Speichere und schließe die Datei.

### 8. Service aktivieren und starten

Lade die Systemd-Daemon neu, Aktiviere den Service für den automatischen Start und Starte den Service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable projekt_beerpong
sudo systemctl start projekt_beerpong
```

### 9. Branch für die Anwendung auf dem Raspberry Pi

Für die Anwendung auf dem Raspberry Pi sollte der main-Branch verwendet werden:


### Funktionsweise

Das System erkennt Treffer auf Becher und wertet das Spiel in Echtzeit aus. Zudem werden in unregelmäßegen abständen Fragen angezeigt.

# Viel Spaß beim digitalen BeerPong! 🍻
![Alt Text](<div class="tenor-gif-embed" data-postid="16765874" data-share-method="host" data-aspect-ratio="1" data-width="100%"><a href="https://tenor.com/view/stone-cold-steve-austin-drink-beer-drinking-beer-beer-bash-wwe-gif-16765874">Stone Cold Steve Austin Drink Beer GIF</a>from <a href="https://tenor.com/search/stone+cold+steve+austin-gifs">Stone Cold Steve Austin GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>)
