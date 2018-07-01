# Raspberry Pi Temperature Sensor

Tested with a Raspberry Pi Zero W and a DHT11 temperature sensor.

## Requirements:

[Adafruit's DHT](https://github.com/adafruit/Adafruit_Python_DHT)


## Basic Setup:


### Temperature sensor setup
1. Clone Adafurit's DHT repo `https://github.com/adafruit/Adafruit_Python_DHT`
2. `cd Adafruit_Python_DHT`
3. Install library: `sudo python setup.py install`

### Google Sheets setup
Reference this blog from [Twillio](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)

* Install `pip install gspread oauth2client`
* May need upgrade: `pip install --upgrade pyasn1-modules`