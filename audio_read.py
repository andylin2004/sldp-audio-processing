import numpy as np
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

while True:
    for i in range(0, int(RATE / CHUNK)):
        data = np.fromstring(stream.read(CHUNK), dtype=np.int16)
        peak=np.average(np.abs(data))
        print(peak)