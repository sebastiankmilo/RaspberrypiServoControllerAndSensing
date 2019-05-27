import RPi.GPIO as GPIO

class Servo(object):
  
  def  __init__(self,puerto):
    GPIO.setup(puerto,GPIO.OUT) #Ponemos el pin puerto como el modo deseado(salida o entrada)
    self.p = GPIO.PWM(puerto,50)
    self.p.start(map(grados,90,214,2.1,11.45)) #Enviamos un pulso del 7.5% para centrar el servo
    pass
  def angle(self, grados):
    porcentaje = map(grados,30,214,2.1,11.45)
    self.p.ChangeDutyCycle(porcentaje)
    pass
  def stop(self):
    self.p.stop()
    GPIO.cleanup() 
    pass
  
  pass
def map(x, in_min, in_max, out_min, out_max):
    return ((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)