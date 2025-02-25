from bleak import BleakScanner, BleakClient
import asyncio
import global_data

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
    if not found:
        print("❌ Keine ESP32-Module gefunden.")
    return found

async def connect_and_read(name, address):
    """Verbindet sich mit einem ESP32, empfängt Daten und speichert sie in global_data."""
    print(f"🔗 Versuche Verbindung mit {name}: {address}")
    
    try:
        async with BleakClient(address) as client:
            print(f"✅ Erfolgreich verbunden mit {name}")

            def notification_handler(sender, data):
                global_data.sensor_data[name] = list(data)
                print(f"📡 {name} - Cup1: {data[0]}, Cup2: {data[1]}, Cup3: {data[2]}")

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
        print(f"🔄 Erneuter Verbindungsversuch in 5 Sekunden...")
        await asyncio.sleep(5)
        await connect_and_read(name, address)

async def main():
    """Hauptfunktion, die ESP32-Module scannt und verbindet."""
    while True:
        if await find_esp32():
            tasks = []
            for name, info in ESP32_DEVICES.items():
                if info["address"]:
                    await asyncio.sleep(2)  # ⏳ Wartezeit zwischen Verbindungen
                    tasks.append(connect_and_read(name, info["address"]))
            if tasks:
                await asyncio.gather(*tasks)
        await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
