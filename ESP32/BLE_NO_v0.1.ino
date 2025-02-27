#include <ArduinoBLE.h>

// BLE UUIDs
#define SERVICE_UUID "19B10000-E8F2-537E-4F6C-D104768A1214"
#define CHARACTERISTIC_UUID "19B10001-E8F2-537E-4F6C-D104768A1214"

// BLE Service und Charakteristik
BLEService sensorService(SERVICE_UUID);
BLECharacteristic sensorCharacteristic(CHARACTERISTIC_UUID, BLERead | BLENotify, 3); // 3 Bytes für 3 Sensoren

// Ultraschallsensor-Pins
#define LED_OUT        13
#define NO_1           25
#define NO_2           26
#define NO_3           27

void setup() {
  Serial.begin(115200);

  pinMode(LED_OUT, OUTPUT);
  pinMode(NO_1, INPUT);
  pinMode(NO_2, INPUT);
  pinMode(NO_3, INPUT);

  // BLE Initialisierung
  if (!BLE.begin()) {
    Serial.println("BLE initialisation ERROR!");
    while (1);
  }

  // BLE Setup
  BLE.setLocalName("ESP_Modul1");
  BLE.setAdvertisedService(sensorService);
  sensorService.addCharacteristic(sensorCharacteristic);
  BLE.addService(sensorService);
  BLE.advertise();
  Serial.println("BLE Server is running!");
}

void loop() {
  // BLE-Verbindung prüfen
  BLEDevice central = BLE.central();

  //Taktgeschwindigkeit begrenzen
  delay(500);

 //LED Blink in Search Modus
  if(digitalRead(LED_OUT)){
    digitalWrite(LED_OUT, LOW);
  } else{
    digitalWrite(LED_OUT, HIGH);
  }

  Serial.println("Searching Device!");
  if (central) {
    Serial.println("Connected to central device!");
    digitalWrite(LED_OUT, HIGH);

    while (central.connected()) {

      // Zustände in ein Byte-Array packen
      uint8_t sensorData[3] = {digitalRead(NO_1), digitalRead(NO_2), digitalRead(NO_3)};
      // Debug-Ausgabe
      Serial.print("Cup1: "); Serial.print(sensorData[0]);
      Serial.print(", Cup2: "); Serial.print(sensorData[1]);
      Serial.print(", Cup3: "); Serial.println(sensorData[2]);

      // BLE-Charakteristik aktualisieren
      sensorCharacteristic.writeValue(sensorData, sizeof(sensorData));

      delay(500); // Datenübertragungsrate
    }
    Serial.println("Central device disconnected!");
    digitalWrite(LED_OUT, LOW);
  } 
}
