import subprocess,time,os
import urllib
import win32com.client
import math
import sounddevice as sd
import requests


# Testing the camera
subprocess.run('start microsoft.windows.camera:', shell=True)
time.sleep(2)
subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)


# Testing the speakers
sd.default.device = None
sd.default.samplerate = samplerate = 48000

duration = 1.5
volume = 0.3
frequency = 440

# fade time in seconds:
fade_in = 0.01
fade_out = 0.3

buffer = memoryview(bytearray(int(duration * samplerate) * 4)).cast('f')

for i in range(len(buffer)):
    buffer[i] = volume * math.cos(2 * math.pi * frequency * i / samplerate)

fade_in_samples = int(fade_in * samplerate)
for i in range(fade_in_samples):
    buffer[i] *= i / fade_in_samples

fade_out_samples = int(fade_out * samplerate)
for i in range(fade_out_samples):
    buffer[-(i + 1)] *= i / fade_out_samples

for mapping in ([1], [2], [1, 2]):
    sd.play(buffer, blocking=True, mapping=mapping)
    sd.sleep(500)


# Testing Internet connection
while True:
    try:
        requests.get('https://www.google.com/').status_code
        print('Successful connection to internet\n')
        msg = urllib.request.urlopen('https://www.google.com/')
        print(msg)
        print()
        break
    except:
       print('No connection to Internet\n')
       break


# Detecting all USBs
def get_usb_device():
    try:
        wmi = win32com.client.GetObject("winmgmts:")
        with open("USB_Info.txt", "w") as USB_Info:

            for usb in wmi.InstancesOf("Win32_USBHub"):
                USB_Info.write(f"{usb.description} \n")
                #print(usb.description)
    except:
        print('Error')

get_usb_device()

