from datetime import datetime, date, timedelta
from datetime import time as tm
import time
import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import ServoRaspberry
from Arduino import Arduino #se debe instalar:  pip3 install arduino-python3
import pandas as pd #se debe instalar: sudo apt-get install python3-pandas
import csv
from pyexcel.cookbook import merge_all_to_a_book #instalar:  sudo pip3 install pyexcel pyexcel-xlsx
import glob


# Función que es llamada por los eventos
def tarea(servos,horario):
    abrir(Servos=servos) ##mover los servos para ponerlos en la posición en la cual puedan tomar datos
    leer(horario=horario)
    cerrar(Servos=servos) #Muevo los servos
    pass
    
def abrir(Servos):
  #angulos=[40,50,60,70,80]
  #i=0
  for servo in Servos:
    servo.angle(grados=180)
    #servo.angle(grados=angulos[i])
    #i=i+1
    pass  
  #Servos[0].angle(180)
  #Servos[1].angle(180)
  #Servos[2].angle(180)
  #Servos[3].angle(180)
  #Servos[4].angle(180)
  time.sleep(4)
  pass

def cerrar(Servos):
  for servo in Servos:
    servo.angle(grados=90)
    pass  
  time.sleep(4)
  pass

def map(x, in_min, in_max, out_min, out_max):

   return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
   pass
def voltaje(arduino,puerto):
   sensorValue=board.analogRead(puerto) ##leer
   return  map(sensorValue, 0, 1023, 0.0, 5.0)
def leer (horario):
  horario=horario
  cant = 0
  datos={}
  medidas = ["planta1","planta2","planta3","planta4","planta5"]
  puertos = [0,1,2,3,4,5]
  lecturasAnalogas = {}
  for planta in medidas:  #inicializo datos("key1"=[])   
        try:
            datos[planta] =[]
        except KeyError:
            datos[planta] = []
        pass
  board = Arduino()
  comienzo = time.time()
  tiempoEjecuecion = 5 
  final = comienzo + tiempoEjecuecion #defino en que momento se deja de tomar los datos
  while final > time.time(): #lee los datos durante 5 segundos
    try:        
        for puerto in puertos:   # leyendo el voltaje de los puertos analógicos     
            lecturasAnalogas[puerto] =voltaje(arduino=board,puerto=puerto)#envió la orden para leer datos analogico y enviarmelos
            pass
        
        
        #datos["planta1"].append(lecturasAnalogas[0] - lecturasAnalogas[1])
        #datos["planta2"].append(lecturasAnalogas[2] - lecturasAnalogas[3])
        #datos["planta3"].append(lecturasAnalogas[4] - lecturasAnalogas[5])
        #datos["planta4"].append(lecturasAnalogas[6] - lecturasAnalogas[7])
        #datos["planta5"].append(lecturasAnalogas[8] - lecturasAnalogas[9])
        for planta in medidas: #voy a almacenar los datos que le corresponden a cada planta
            try:
                #datos["planta1"].append(lecturasAnalogas[0] - lecturasAnalogas[1])
                #datos["planta2"].append(lecturasAnalogas[2] - lecturasAnalogas[3])
                #datos["planta3"].append(lecturasAnalogas[4] - lecturasAnalogas[5])
                #datos["planta4"].append(lecturasAnalogas[6] - lecturasAnalogas[7])
                #datos["planta5"].append(lecturasAnalogas[8] - lecturasAnalogas[9])
               puerto = planta.replace("planta","") #dejo solo el numero de la planta
               puerto1 = int(puerto)*2-1 #el numero de la planta tiene una relacion numerica con los puertos que le corresponden
               puerto2 = puerto1 - 1
               datos[planta].append(lecturasAnalogas[puerto1] - lecturasAnalogas[puerto2]) #resto el valor de los puertos y se los asigno a la planta correspondiente
           except KeyError:
                datos[planta] = 0.0 #por si no hay puerto para esa planta
        #    pass
    
    except KeyboardInterrupt: 
        board.close()
    pass
  board.close() 
  dfDatos = pd.DataFrame(datos) #convierto el diccionario a un DataFrame
  nombreArchivo = str(datetime.now().year)+"-"+str(+datetime.now().month)+"-"+str(datetime.now().day)
  nombreArchivo = nombreArchivo+horario
  dfDatos.reset_index().to_csv(nombreArchivo+".csv",header =True, index = None, index_label=None) #almaceno los datos en un archivo de texto plano con formato .csv  
  merge_all_to_a_book(glob.glob(nombreArchivo+".csv"), nombreArchivo+".xlsx") #almaceno los datos de texto plano en un formato xlsx
  pass

mañana = tm(23,55,0) #Mañana
tarde = tm(23,56,0) #Tarde
noche = tm(23,57,0) #Noche
horarios ={} #Defino un diccionario para los horarios
horarios["nuevo día"] = tm(23,59,58)
horarios["mañana"] = mañana
horarios["tarde"] = tarde
horarios["noche"] = noche
GPIO.setmode(GPIO.BOARD)
#Servo1 = ServoRaspberry.Servo(puerto = 8)  #Defino donde va a estar conectado el servo 1 a los puertos GPIO  de la raspberrypi
#Servo2 = ServoRaspberry.Servo(puerto = 9)  #Defino donde va a estar conectado el servo 2 a los puertos GPIO  de la raspberrypi
#Servo3 = ServoRaspberry.Servo(puerto = 10) #Defino donde va a estar conectado el servo 3 a los puertos GPIO  de la raspberrypi
#Servo4 = ServoRaspberry.Servo(puerto = 11) #Defino donde va a estar conectado el servo 4 puertos GPIO  de la raspberrypi
#Servo5 = ServoRaspberry.Servo(puerto = 12) #Defino donde va a estar conectado el servo 5  a los puertos GPIO  de la raspberrypi

puertos=[8,10,11,12,13]
pos=0
servos = [ ServoRaspberry.Servo(puerto = puertos[i]) for i in range(4)] #array q contiene los 4 servos
#for servo in servos:
#  servo = ServoRaspberry.Servo(puerto = puertos[pos])
#  pos=pos+1
#  pass



print('PROGRAMADOR INICIADO:')
mañana = False
tarde = False
noche = False
test =True
while test :
  time.sleep(1)
  horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
  if horarios["actual"] >= horarios["mañana"] :
    print("mañana")
    tarea(servos=servos,horario="mañana")
    mañana = True
    while mañana :
      time.sleep(1)
      horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
      if horarios["actual"] >= horarios["tarde"] :
        print("tarde")
        tarea(servos=servos,horario="tarde")
        mañana = False
        tarde = True
        while tarde:
          time.sleep(1)
          horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
          if horarios["actual"] >= horarios["noche"] :
            tarde = False
            noche = True
            tarea(servos,servos=servos,horario="noche")
            print("noche")
            while noche :
              time.sleep(1)
              horarios["actual"] = tm(datetime.now().hour,datetime.now().minute,datetime.now().second)
              if horarios["actual"] >= horarios["nuevo día"] :
                noche = False
                time.sleep(4)
                print ("Nuevo Día")
                pass
              pass 
            pass
          pass
        pass
      pass
    pass
  pass