#include <ESP8266WiFi.h>
#include "ESPAsyncWebServer.h"
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

Adafruit_MPU6050 mpu;

const int RSSI_MAX =-34;// define maximum strength of signal in dBm
const int RSSI_MIN =-100;// define minimum strength of signal in dBm

WiFiClient client;

// Set Wifi network credentials
const char* ssid_cl = "HP-TECH";
const char* pswd_cl = "Carbon12";

// Set your access point network credentials
const char* ssid = "ESP8266-Access-Point";
const char* password = "123456789";
IPAddress ip(192,168,11,2);
IPAddress gateway(192,168,11,1);
IPAddress subnet(255,255,255,0);

//IMU and RSSI system Variables
float tempC=37;
float Humi=56;
float Acc_X, Acc_Y, Acc_Z;
float Gyro_Ro, Gyro_Pi, Gyro_Yw;
float rssi,rssiPer;

/*Return Value Function*/
String retValueTwo(float*);

String readGyro();
String readAccl();
String readRSSI();

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);


void setup(){
  // Serial port for debugging purposes
  Serial.begin(115200);
  Serial.println();

  //-----------------MPU Configuration-----------------//
  //--------------------------------------------------//
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");

   mpu.setAccelerometerRange(MPU6050_RANGE_2_G);
  Serial.print("Accelerometer range set to: ");
  switch (mpu.getAccelerometerRange()) {
  case MPU6050_RANGE_2_G:
    Serial.println("+-2G");
    break;
  case MPU6050_RANGE_4_G:
    Serial.println("+-4G");
    break;
  case MPU6050_RANGE_8_G:
    Serial.println("+-8G");
    break;
  case MPU6050_RANGE_16_G:
    Serial.println("+-16G");
    break;
  }
  mpu.setGyroRange(MPU6050_RANGE_250_DEG);
  Serial.print("Gyro range set to: ");
  switch (mpu.getGyroRange()) {
  case MPU6050_RANGE_250_DEG:
    Serial.println("+- 250 deg/s");
    break;
  case MPU6050_RANGE_500_DEG:
    Serial.println("+- 500 deg/s");
    break;
  case MPU6050_RANGE_1000_DEG:
    Serial.println("+- 1000 deg/s");
    break;
  case MPU6050_RANGE_2000_DEG:
    Serial.println("+- 2000 deg/s");
    break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  Serial.print("Filter bandwidth set to: ");
  switch (mpu.getFilterBandwidth()) {
  case MPU6050_BAND_260_HZ:
    Serial.println("260 Hz");
    break;
  case MPU6050_BAND_184_HZ:
    Serial.println("184 Hz");
    break;
  case MPU6050_BAND_94_HZ:
    Serial.println("94 Hz");
    break;
  case MPU6050_BAND_44_HZ:
    Serial.println("44 Hz");
    break;
  case MPU6050_BAND_21_HZ:
    Serial.println("21 Hz");
    break;
  case MPU6050_BAND_10_HZ:
    Serial.println("10 Hz");
    break;
  case MPU6050_BAND_5_HZ:
    Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  delay(100);
 //-----------------------------------------------------//
 //-----------------------------------------------------//

  //--------------------WiFi Setup---------------------//
 //----------------------------------------------------//
  WiFi.mode(WIFI_AP_STA);
  //Wifi Communication
  Serial.print("Connecting to ");
  Serial.println(ssid_cl);
  WiFi.begin(ssid_cl,pswd_cl);
  while(WiFi.status()!=WL_CONNECTED){
  delay(500);
  Serial.print(".");
  }
  Serial.print(ssid_cl);
  Serial.println(" Connected");
  Serial.println(WiFi.localIP());
 //----------------------------------------------------//
 //----------------------------------------------------//
 
  //------------------Access Point Setup----------------//
 //----------------------------------------------------//
  // Setting the ESP as an access point
  Serial.print("Setting AP (Access Point)…");
  // Remove the password parameter, if you want the AP (Access Point) to be open
  WiFi.softAPConfig(ip,gateway,subnet);
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);
  //---------------------------------------------------//
  //---------------------------------------------------//

  //-------------------Server SETUP--------------------//
  server.on("/gyro", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readGyro().c_str());
  });
  
  server.on("/Accl", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readAccl().c_str());
  });
  server.on("/RSSI", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readRSSI().c_str());
  }); 
  server.begin();
  //---------------------------------------------------//
  
}
 
void loop(){
  //server.handleClient();
  /*Get RSSI of the Station*/
  rssi = wifi_station_get_rssi();
  rssiPer=dBmtoPercentage(rssi);
  Serial.print("RSSI in dbm:");
  Serial.println(rssi);
  //Serial.print("\t");
  //Serial.print("InPercent: ");
  //Serial.println(rssiPer);
  //---------------------------------------------------//
  //-----------------MPU sensor reading----------------//
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Acc_X=a.acceleration.x;
  Acc_Y=a.acceleration.y;
  Acc_Z=a.acceleration.z;

  Gyro_Ro=g.gyro.x;
  Gyro_Pi=g.gyro.y;
  Gyro_Yw=g.gyro.z;
  
  /* Print out the values */
  //Serial.print("Acceleration X: ");
  //Serial.print(Acc_X);
  //Serial.print(", Y: ");
  //Serial.print(Acc_Y);
  //Serial.print(", Z: ");
  //Serial.print(Acc_Z);
  //Serial.println(" m/s^2");

  
  //Serial.print("Rotation X: ");
  //Serial.print(Gyro_Ro);
  //Serial.print(", Y: ");
  //Serial.print(Gyro_Pi);
  //Serial.print(", Z: ");
  //Serial.print(Gyro_Yw);
  //Serial.println(" rad/s");

  //Serial.print("Temperature: ");
  //Serial.print(temp.temperature);
  //Serial.println(" degC");

  //Serial.println("");
  //---------------------------------------------------//
  //---------------------------------------------------------------------------------------------------------------------//
  delay(1000);
}
int dBmtoPercentage(int dBm)
{
  int quality;
    if(dBm <= RSSI_MIN)
    {
        quality = 0;
    }
    else if(dBm >= RSSI_MAX)
    {  
        quality = 100;
    }
    else
    {
        quality = 2 * (dBm + 100);
   }
   return quality;
}//dBmtoPercentage

String retValueTwo(float *tmp){
  return String(*tmp);
  }


String readGyro(){
  String GyroCat="GyroData:,";
  GyroCat+=String(retValueTwo(&Gyro_Ro))+",";
  GyroCat+=String(retValueTwo(&Gyro_Pi))+",";
  GyroCat+=String(retValueTwo(&Gyro_Yw));
  
  return GyroCat;  
  }
String readAccl(){
  String AccCat="AccData:,";
  AccCat+=String(retValueTwo(&Acc_X))+",";
  AccCat+=String(retValueTwo(&Acc_Y))+",";
  AccCat+=String(retValueTwo(&Acc_Z));
  
 return AccCat; 
  }
String readRSSI(){
  String tempRssi=retValueTwo(&rssi);
  return tempRssi;
  }
