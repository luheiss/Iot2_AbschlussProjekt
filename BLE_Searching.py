from bleak import BleakScanner, BleakClient
import asyncio
import global_data

ESP32_DEVICES = {
    "ESP_Modul1": {"address": None, "service_uuid": "19B10000-E8F2-537E-4F6C-D104768A1214"},
    "ESP_Modul2": {"address": None, "service_uuid": "19B10000-E8F2-537E-4F6C-D104768A1214"}
}

CHARACTERISTIC_UUID = "19B10001-E8F2-537E-4F6C-D104768A1214"

async def find_esp32():
    print("Scanne nach ESP32-Modulen...")
    devices = await BleakScanner.discover()
    found = False
    for device in devices:
        for name in ESP32_DEVICES.keys():
            if device.name == name:
                ESP32_DEVICES[name]["address"] = device.address
                print(f"{name} gefunden: {device.address}")
                found = True
    if not found:
        print("Keine ESP32-Module gefunden.")
    return found

async def connect_and_read(name, address):
    async with BleakClient(address) as client:
        print(f"Verbunden mit {name}: {address}")

        def notification_handler(sender, data):
            global_data.sensor_data[name] = list(data)
            print(f"{name} - Cup1: {data[0]}, Cup2: {data[1]}, Cup3: {data[2]}")

        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        try:
            while True:
                await asyncio.sleep(5)
        except KeyboardInterrupt:
            print("Beenden...")
        finally:
            await client.stop_notify(CHARACTERISTIC_UUID)

async def main():
    while True:
        if await find_esp32():
            tasks = []
            for name, info in ESP32_DEVICES.items():
                if info["address"]:
                    tasks.append(connect_and_read(name, info["address"]))
            if tasks:
                await asyncio.gather(*tasks)
        await asyncio.sleep(5)

asyncio.run(main())
