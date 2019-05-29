from Arduino import Arduino

def map(x, in_min, in_max, out_min, out_max):

   return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
   pass

board = Arduino()
try:
    while True :
        sensorValue=board.analogRead(5)
        value = map(sensorValue, 0, 1023, 0.0, 5.0)
        print(value)

except KeyboardInterrupt: 
  board.close()
  