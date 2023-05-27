#rom imu import MPU6050
import time
from machine import Pin, I2C
import network
import urequests
from PiicoDev_MPU6050 import PiicoDev_MPU6050

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000) #Pin bilgisini ve haberleşme frekansı bilgisini tanımlıyoruz.
imu = PiicoDev_MPU6050() #IMU isimli bir değişken yaratıp, MPU6050 kütüphanesi ile kullanıyoruz.

led = Pin(16, Pin.OUT)
buzzer = Pin(2, Pin.OUT)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Wifi Name","Wifi Password")
time.sleep(5)
print(wlan.isconnected())
#temp = gY
gyro = imu.read_gyro_data()
def mesaj_gonder():
    led.value(1)
    buzzer.value(1)
    print("deprem oldu")
    temp_readings = { 'value1':gyro }
    request_headers = {'Content-Type': 'application/json'}
    request = urequests.post(
    'https://maker.ifttt.com/trigger/deprem_olcer/with/key/IFTTT API KEY',
    json=temp_readings,
    headers=request_headers)
    time.sleep(3)
    led.value(0)
    buzzer.value(0)
    print("mesaj gönderildi")

while True:
   
    accel = imu.read_accel_data() # read the accelerometer [ms^-2]
    aX = round(accel["x"])
    aY = round(accel["y"])
    aZ = round(accel["z"])
    print("x:" + str(aX) + " y:" + str(aY) + " z:" + str(aZ))
    gyro = imu.read_gyro_data()
    gX = round(gyro["x"])
    gY = round(gyro["y"])
    gZ = round(gyro["z"])
    print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))
    temp = imu.read_temperature()
    
    #print(imu.accel.xyz,imu.gyro.xyz,imu.temperature,end='\r') #Ham veri.
    print(aX,"\t",aY,"\t",aZ,"\t",gX,"\t",gY,"\t",gZ,"\t",temp,"        ",end="\r") #Yuvarlatılmış veri.
    
    if gX >=2.00 or gY >=2.00 or gZ >=2.00:
        time.sleep(3)
        mesaj_gonder()
#
#rom imu import MPU6050

