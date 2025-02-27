import json
import asyncio
from bleak import BleakScanner, BleakClient
import os

SENSOR_DATA_FILE = "sensor_data.json"
sensor_data = {}

ESP32_DEVICES = {
    "ESP_Modul1": {"address": None, "service_uuid": "19B10000-E8F2-537E-4F6C-D104768A1214"},
    "ESP_Modul2": {"address": None, "service_uuid": "19B10000-E8F2-537E-4F6C-D104768A1215"}
}

CHARACTERISTIC_UUID = "19B10001-E8F2-537E-4F6C-D104768A1214"


async def find_esp32():
    """Scannt nach ESP32-Geräten und speichert die Adressen."""
    print("🔍 Scanne nach ESP32-Modulen...")
    devices = await BleakScanner.discover()
    found = False
    for device in devices:
        for name in ESP32_DEVICES.keys():
            if device.name == name:
                ESP32_DEVICES[name]["address"] = device.address
                print(f"✅ {name} gefunden: {device.address}")
                found = True
    return found


async def connect_and_read(name, address):
    """Verbindet sich mit einem ESP32, empfängt Daten und speichert sie."""
    print(f"🔗 Verbindung mit {name} ({address}) wird aufgebaut...")

    try:
        async with BleakClient(address) as client:
            print(f"✅ Erfolgreich verbunden mit {name}")

            def notification_handler(sender, data):
                """Speichert die empfangenen BLE-Daten in sensor_data"""
                values = list(data)  # BLE-Daten in eine Liste umwandeln
                if len(values) == 3:
                    sensor_data[name] = {
                        "Cup1": values[0],
                        "Cup2": values[1],
                        "Cup3": values[2]
                    }
                    print(f"📡 {name} - Cup1: {values[0]}, Cup2: {values[1]}, Cup3: {values[2]}")
                    save_sensor_data()  # Speichern in Datei

            await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

            try:
                while True:
                    await asyncio.sleep(5)
            except KeyboardInterrupt:
                print("🔌 Beenden...")
            finally:
                await client.stop_notify(CHARACTERISTIC_UUID)

    except Exception as e:
        print(f"❌ Fehler bei {name}: {e}")
        # Falls das Modul nicht mehr erreichbar ist, entferne es aus den Daten
        if name in sensor_data:
            del sensor_data[name]
            save_sensor_data()
        print(f"❌ {name} entfernt aus der Liste, da keine Verbindung möglich war.")


def save_sensor_data():
    """Speichert die Sensordaten in eine JSON-Datei."""
    try:
        with open(SENSOR_DATA_FILE, "w") as file:
            json.dump(sensor_data, file)
    except Exception as e:
        print(f"⚠️ Fehler beim Speichern der Daten: {e}")


def get_modul_daten(modulname):
    """Liest die Sensordaten aus der JSON-Datei."""
    if not os.path.exists(SENSOR_DATA_FILE):
        return None  # Falls die Datei nicht existiert, kein ESP verbunden

    try:
        with open(SENSOR_DATA_FILE, "r") as file:
            data = json.load(file)
        return data.get(modulname, None)  # Falls kein Modul vorhanden, gebe None zurück
    except (json.JSONDecodeError, FileNotFoundError):
        return None


async def main():
    """Hauptprozess: Scannt und verbindet sich mit ESP32-Modulen"""
    while True:
        if await find_esp32():
            tasks = []
            for name, info in ESP32_DEVICES.items():
                if info["address"]:
                    await asyncio.sleep(2)  # Warte kurz zwischen Verbindungen
                    tasks.append(connect_and_read(name, info["address"]))
            if tasks:
                await asyncio.gather(*tasks)
        await asyncio.sleep(5)  # Wartezeit zwischen Scans


if __name__ == "__main__":
    asyncio.run(main())
