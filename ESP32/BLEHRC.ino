#include <ArduinoBLE.h>
#include <NewPing.h>

// BLE UUIDs
#define SERVICE_UUID "19B10000-E8F2-537E-4F6C-D104768A1214"
#define CHARACTERISTIC_UUID "19B10001-E8F2-537E-4F6C-D104768A1214"

// BLE Service und Charakteristik
BLEService sensorService(SERVICE_UUID);
BLECharacteristic sensorCharacteristic(CHARACTERISTIC_UUID, BLERead | BLENotify, 3); // 3 Bytes für 3 Sensoren

// Ultraschallsensor-Pins
#define LED_OUT        5
#define TRIGGER_PIN_1  23
#define ECHO_PIN_1     22
#define TRIGGER_PIN_2  19
#define ECHO_PIN_2     18
#define TRIGGER_PIN_3  16
#define ECHO_PIN_3     15
#define MAX_DISTANCE 200

// Ultraschallsensor-Objekte
NewPing sonar_1(TRIGGER_PIN_1, ECHO_PIN_1, MAX_DISTANCE);
NewPing sonar_2(TRIGGER_PIN_2, ECHO_PIN_2, MAX_DISTANCE);
NewPing sonar_3(TRIGGER_PIN_3, ECHO_PIN_3, MAX_DISTANCE);

// Zustände der Cups
bool is_Cup1 = false;
bool is_Cup2 = false;
bool is_Cup3 = false;

void setup() {
  Serial.begin(115200);
  pinMode(LED_OUT, OUTPUT);

  // BLE Initialisierung
  if (!BLE.begin()) {
    Serial.println("BLE initialisation ERROR!");
    while (1);
  }

  // BLE Setup
  BLE.setLocalName("ESP_Ultrasonic");
  BLE.setAdvertisedService(sensorService);
  sensorService.addCharacteristic(sensorCharacteristic);
  BLE.addService(sensorService);
  BLE.advertise();
  Serial.println("BLE Server is running!");
}

void loop() {
  // BLE-Verbindung prüfen
  BLEDevice central = BLE.central();
  if (central) {
    Serial.println("Connected to central device!");
    digitalWrite(LED_OUT, HIGH);

    while (central.connected()) {
      // Ultraschallsensoren abfragen
      unsigned int uS_1 = sonar_1.ping();
      unsigned int uS_2 = sonar_2.ping();
      unsigned int uS_3 = sonar_3.ping();

      float distance_1 = uS_1 / US_ROUNDTRIP_CM;
      float distance_2 = uS_2 / US_ROUNDTRIP_CM;
      float distance_3 = uS_3 / US_ROUNDTRIP_CM;

      // Cups detektieren
      is_Cup1 = (distance_1 > 0 && distance_1 < 5);
      is_Cup2 = (distance_2 > 0 && distance_2 < 5);
      is_Cup3 = (distance_3 > 0 && distance_3 < 5);

      // Zustände in ein Byte-Array packen
      uint8_t sensorData[3] = {is_Cup1, is_Cup2, is_Cup3};

      // BLE-Charakteristik aktualisieren
      sensorCharacteristic.writeValue(sensorData, sizeof(sensorData));

      // Debug-Ausgabe
      Serial.print("Cup1: "); Serial.print(is_Cup1);
      Serial.print(", Cup2: "); Serial.print(is_Cup2);
      Serial.print(", Cup3: "); Serial.println(is_Cup3);

      delay(500); // Datenübertragungsrate
    }

    Serial.println("Central device disconnected!");
    digitalWrite(LED_OUT, LOW);
  }
}
