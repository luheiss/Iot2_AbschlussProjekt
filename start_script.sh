#!/bin/bash

# Stelle sicher, dass wir im richtigen Verzeichnis sind
cd /home/ParryHotter/BeerPong

# Aktiviere die virtuelle Umgebung
source .venv/bin/activate

# Starte BLE_Search.py und warte, bis es fertig ist
python BLE_Search.py

# Danach starte main.py
python main.py
