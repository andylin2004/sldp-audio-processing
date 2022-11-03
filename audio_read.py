import wave
import numpy as np
wav_obj = wave.open('StarWars60.wav', 'rb')

sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
time = n_samples/sample_freq
print(time)
n_channels = wav_obj.getnchannels()
print(n_channels)
signal_wave = wav_obj.readframes(n_samples)
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
l_channel = signal_array[0::2]
r_channel = signal_array[1::2]
print(l_channel)
print(r_channel)