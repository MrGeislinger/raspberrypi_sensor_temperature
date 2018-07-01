from time import sleep
import Adafruit_DHT

# Using DHT11 at GPIO pin #4
sensor = 11
pin = 4
wait_time = 3

while True:
    # Getting humidity percentage and temperature in Celcius
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

   
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    # Wait a few seconds
    sleep(wait_time)