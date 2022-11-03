import wave
import numpy as np
import time
import sounddevice as sd

wav_obj = wave.open('StarWars60.wav', 'rb')

sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
t_audio = n_samples/sample_freq
print(t_audio)
n_channels = wav_obj.getnchannels()
print(n_channels)
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
sd.play(signal_array, sample_freq)
for i in range(n_samples):
    print(signal_array[i])
    time.sleep(1/sample_freq)
