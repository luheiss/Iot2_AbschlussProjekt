# IoT2 Abschlussprojekt - ESP32 Branch

Dieser Branch enthält den Code für die ESP32-Module, die im Rahmen des Projekts verwendet werden. Der Code ist für die Arduino IDE konzipiert und befindet sich in der Datei:
BLE_NO_v0.1.ino

## Wichtige Hinweise

Jedes ESP32-Modul benötigt eine eigene Service UUID.
Die Characteristic UUID kann für alle Module gleich bleiben.

### Anpassung der Service UUID

Da jedes ESP32-Modul eine eigene Service UUID benötigt, muss im Code folgender Abschnitt individuell angepasst werden:
```bash
BLEService beerPongService("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"); // Eindeutige Service UUID
BLECharacteristic beerPongCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLEWrite, 20);
```
```bash
Die Service UUID ("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx") muss für jedes Modul individuell generiert und eingetragen werden.
```
Die Characteristic UUID ("19B10001-E8F2-537E-4F6C-D104768A1214") kann für alle Module gleich bleiben.

Viel Erfolg mit der Entwicklung! 🚀


