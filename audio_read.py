import numpy as np
import pyaudio
import RPi.GPIO as GPIO          
from time import sleep

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
p=GPIO.PWM(en,5000)

p.start(0)

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)

while True:
    for i in range(0, int(RATE / CHUNK)):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak=np.average(np.abs(data))
        p.ChangeDutyCycle(100 * peak / 50000)