# CPU-Temperatur geregelte Lüftersteuerung
# Funktionstest der LED
# schaltet Lüfter ein und aus
# schaltet drei LED an und aus

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(27, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(17, GPIO.HIGH)

#Funktionstest der LED-Kontrollleuchten
for x in range(20):
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(23, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(27, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(22, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(23, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(27, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(22, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(23, GPIO.HIGH)
time.sleep(5)


#Lüftersteuerung
while 1:
 tempData = "/sys/class/thermal/thermal_zone0/temp"
 dateilesen = open(tempData, "r")
 temperatur = dateilesen.readline(2)
 dateilesen.close()
 print("Deine CPU hat " + temperatur + " Grad")

 normal = 50
 warm = 55
 heiss = 60
 temperatur = int(temperatur)
 if temperatur <= normal:
  #print ("Die CPU ist Normal, die grüne LED geht an.")
  GPIO.output(27, GPIO.HIGH)
  GPIO.output(22, GPIO.LOW)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(17, GPIO.LOW)
 if temperatur > normal:
  #print ("Die CPU ist Warm, die Gelbe LED geht auch an")
  GPIO.output(27, GPIO.HIGH)
  GPIO.output(22, GPIO.HIGH)
  GPIO.output(23, GPIO.LOW)
  GPIO.output(17, GPIO.LOW)
 if temperatur > heiss:
  #print ("Die CPU ist wärmer als warm! Die Rote LED geht an und wir schalten d$
  GPIO.output(23, GPIO.HIGH)
  GPIO.output(17, GPIO.HIGH)
 time.sleep(15)
