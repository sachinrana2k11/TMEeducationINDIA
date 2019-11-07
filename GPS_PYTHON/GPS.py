import sys
import time
import json
class GPS:
    def __init__(self):
        self.load_config()

    def load_config(self):
        try:
            with open('config.json') as f:
                data = json.load(f)
            self.gps_type = data['GPS_type']
            self.Baudrate = int(data['BaudRate'])
            self.COM_PORT = data['COM_PORT']
            self.EXT_NAME = data['EXT_NAME']
            self.delay = int(data['Time'])
        except:
            e = sys.exc_info()[0]
            print("ERROR IN :- " + str(e))
            return

    def getdata(self):
        try:
            a = str(self.serial1.readline())
            data_raw=a.split(",")
            if self.gps_type == "UBLOX_NEO6M":
                if data_raw[0] == "b'$GPRMC":#for old gps
                      if data_raw[2]=="A":
                          a=data_raw[3]#raw lat
                          b=data_raw[5]#raw lon
                          c=data_raw[7]#raw speed
                          lati=float(a)/100
                          longi=float(b)/100
                          speed=float(data_raw[7])*1.852
                          lati_int=int(lati)
                          longi_int=int(longi)
                          raw_lat=float(lati-lati_int)/60.0
                          raw_lon=float(longi-longi_int)/60.0
                          latitude=(lati_int+(raw_lat*100))
                          longitude=(longi_int+(raw_lon*100))
                          latitude = str(format(latitude, '.6f'))
                          longitude = str(format(longitude, '.6f'))
                          speed = str(format(speed, '.1f'))
                          print(latitude, longitude, speed + "-Km/h")
                          return latitude, longitude, speed
                if data_raw[2] == "V":
                    print("GPS data not Available..")
                    return 0, 0, 0

            if self.gps_type == "UBLOX_M8N":
                if data_raw[0] == "b'GPGGA":#for old NEO6m,NEO7m gps
                      if data_raw[2] == "A":
                          a = data_raw[3]  # raw lat
                          b = data_raw[5]  # raw lon
                          c = data_raw[7]  # raw speed
                          lati = float(a) / 100
                          longi = float(b) / 100
                          speed = float(data_raw[7]) * 1.852
                          lati_int = int(lati)
                          longi_int = int(longi)
                          raw_lat = float(lati - lati_int) / 60.0
                          raw_lon = float(longi - longi_int) / 60.0
                          latitude = (lati_int + (raw_lat * 100))
                          longitude = (longi_int + (raw_lon * 100))
                          latitude = str(format(latitude, '.6f'))
                          longitude = str(format(longitude, '.6f'))
                          speed = str(format(speed, '.1f'))
                          print(latitude,longitude,speed + "-Km/h")
                          return latitude, longitude, speed
                if data_raw[2] == "V":
                    print("GPS data not Available..")
                    return 0, 0, 0

        except:
            e = sys.exc_info()[0]
            print("ERROR IN :- " + str(e))
            return