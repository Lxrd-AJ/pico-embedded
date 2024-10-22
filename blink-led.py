import machine
import time

onboardLED = machine.Pin("LED", machine.Pin.OUT)
tempSensor = machine.ADC(4)
sleepTime = 5

def readTemperature(sensor):
    conversionFactor = 3.3 / 65535
    reading = sensor.read_u16() * conversionFactor
    return 27 - (reading - 0.706)/0.001721

while True:
    onboardLED.toggle()
    time.sleep(sleepTime)
    print(f"Toggling LED for {sleepTime}s")

    onboardLED.toggle()
    time.sleep(sleepTime)

    print(f"Device temperature: {readTemperature(tempSensor)} degrees celsius")
