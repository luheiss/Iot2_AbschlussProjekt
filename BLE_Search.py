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
# Hallo
CHARACTERISTIC_UUID = "19B10001-E8F2-537E-4F6C-D104768A1214"

async def find_esp32():
    """Scannt kontinuierlich nach ESP32-Modulen und aktualisiert deren Adressen."""
    print("🔍 Scanne nach ESP32-Modulen...")
    devices = await BleakScanner.discover()
    for device in devices:
        for name in ESP32_DEVICES:
            if device.name == name:
                if ESP32_DEVICES[name]["address"] != device.address:
                    ESP32_DEVICES[name]["address"] = device.address
                    print(f"✅ {name} gefunden: {device.address}")

async def connect_and_read(name, address):
    """
    Baut eine Verbindung zum ESP32 auf, startet den Notification-Handler,
    und bleibt in einer Schleife aktiv, solange die Verbindung besteht.
    """
    print(f"🔗 Versuche Verbindung mit {name} ({address}) aufzubauen...")
    try:
        async with BleakClient(address) as client:
            print(f"✅ Verbunden mit {name}")

            def notification_handler(sender, data):
                """Empfängt BLE-Daten und speichert sie in sensor_data."""
                values = list(data)
                if len(values) == 3:
                    sensor_data[name] = {
                        "Cup1": values[0],
                        "Cup2": values[1],
                        "Cup3": values[2]
                    }
                    save_sensor_data()

            await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

            # Warte solange die Verbindung aktiv ist
            while client.is_connected:
                await asyncio.sleep(5)

            print(f"❌ Verbindung zu {name} getrennt")
    except Exception as e:
        print(f"❌ Fehler bei {name}: {e}")

def save_sensor_data():
    """Speichert die Sensordaten in einer JSON-Datei."""
    try:
        with open(SENSOR_DATA_FILE, "w") as file:
            json.dump(sensor_data, file)
    except Exception as e:
        print(f"⚠️ Fehler beim Speichern der Daten: {e}")

def get_modul_daten(modulname):
    """Liest die Sensordaten aus der JSON-Datei."""
    if not os.path.exists(SENSOR_DATA_FILE):
        return {"Cup1": None, "Cup2": None, "Cup3": None}
    
    try:
        with open(SENSOR_DATA_FILE, "r") as file:
            data = json.load(file)
        return data.get(modulname, {"Cup1": None, "Cup2": None, "Cup3": None})
    except (json.JSONDecodeError, FileNotFoundError):
        return {"Cup1": None, "Cup2": None, "Cup3": None}

async def main():
    # Dictionary, um die aktuell aktiven Verbindungs-Tasks zu speichern
    connection_tasks = {}
    while True:
        await find_esp32()
        for name, info in ESP32_DEVICES.items():
            address = info["address"]
            if address is not None:
                # Falls kein Task existiert oder der vorherige Task beendet wurde, starte einen neuen
                task = connection_tasks.get(name)
                if task is None or task.done():
                    print(f"🔄 Starte Verbindungstask für {name}")
                    connection_tasks[name] = asyncio.create_task(connect_and_read(name, address))
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
