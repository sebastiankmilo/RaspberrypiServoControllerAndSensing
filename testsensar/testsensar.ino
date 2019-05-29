#include <ArduinoJson.h>
const int sensorPin = A0;   // seleccionar la entrada para el sensor
int sensorValue;         // variable que almacena el valor raw (0 a 1023)
float value;            // variable que almacena el voltaje (0.0 a 5.0)
const int sensorPin1 = A1;   // seleccionar la entrada para el sensor
int sensorValue1;         // variable que almacena el valor raw (0 a 1023)
float value1;
char orden,opcion; 
char enviar,cancelar,recivido;

void setup() 
{
   Serial.begin(9600);
   opcion='n';
   orden=' ';
   enviar='l';
cancelar='n';
recivido=10;
}
 
void loop() 
{  
   
   if (Serial.available())
   {
    orden=Serial.read();
   }
   else
   {
    orden='v';
   }
   
   if (orden == enviar){
    opcion = 'l';
   /*Serial.print("opcion:");
   Serial.print(opcion);
   Serial.print(' ');
   Serial.print("orden:");
   Serial.println(orden);*/
   }
   else  
   {    
    if(orden == 'v'||orden == recivido){
     /*Serial.print("opcion:");
     Serial.print(opcion);
     Serial.print(' ');
     Serial.print("orden:");
     Serial.println(orden); */     
    }
    else{
       /*Serial.print("opcion:");
       Serial.print(opcion);
       Serial.print(' ');
       Serial.print("orden:");
       Serial.println(orden);*/
       opcion='n';    
    }
   }
   if (opcion == enviar){  
    sensorValue = analogRead(sensorPin);          // realizar la lectura
    value = fmap(sensorValue, 0, 1023, 0.0, 5.0);   // cambiar escala a 0.0 - 5.0
     sensorValue1 = analogRead(sensorPin1);          // realizar la lectura
    value1 = fmap(sensorValue1, 0, 1023, 0.0, 5.0);   // cambiar escala a 0.0 - 5.0
    const int capacity = JSON_OBJECT_SIZE(3);
    
    StaticJsonDocument<capacity> doc;
    doc["planta1"]=value-value1;
    doc["sensor2"]=value1;
    serializeJsonPretty(doc, Serial);
    Serial.println("");
    Serial.flush();
    //recivido = Serial.read();   
    delay(10);    
    
   }
   
   delay(1000);
}
 
// cambio de escala entre floats
float fmap(float x, float in_min, float in_max, float out_min, float out_max)
{
   return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
