IoT2 Abschlussprojekt - BeerPong Digitalisierung

Dieses Projekt ist eine digitale Umsetzung des beliebten Spiels BeerPong. Ziel ist es, mithilfe eines Raspberry Pi und entsprechender Software eine smarte, automatisierte Version des Spiels zu realisieren.

Installation auf dem Raspberry Pi

1. Vorbereitung

Erstelle ein neues Verzeichnis und wechsle in dieses:

mkdir ProjektBeerPong
cd ProjektBeerPong

2. Repository klonen

Klonen des Git-Repositories:

git clone <REPO_URL> .

3. Virtuelle Umgebung einrichten

Erstelle eine virtuelle Umgebung im Verzeichnis:

python3 -m venv .venv

Aktiviere die virtuelle Umgebung:

source .venv/bin/activate

4. Zum Interface-Branch wechseln

git checkout interface

5. Abhängigkeiten installieren

pip install -r requirements.txt

6. Start-Skript ausführbar machen

sudo chmod +x start_script.sh

7. Autostart-Service einrichten

Erstelle eine neue Service-Datei:

sudo nano /etc/systemd/system/projekt_beerpong.service

Füge folgenden Inhalt ein:

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

Speichere und schließe die Datei.

8. Service aktivieren und starten

Lade die Systemd-Daemon neu:

sudo systemctl daemon-reload

Aktiviere den Service für den automatischen Start:

sudo systemctl enable projekt_beerpong

Starte den Service:

sudo systemctl start projekt_beerpong

9. Branch für die Anwendung auf dem Raspberry Pi

Für die Anwendung auf dem Raspberry Pi sollte der main-Branch verwendet werden:

git checkout main

Funktionsweise

Das System erkennt Treffer auf Becher und wertet das Spiel in Echtzeit aus. Es bietet eine smarte Benutzeroberfläche zur Anzeige der Spielstände und ermöglicht eine interaktive Spielerfahrung.

Viel Spaß beim digitalen BeerPong! 🍻
