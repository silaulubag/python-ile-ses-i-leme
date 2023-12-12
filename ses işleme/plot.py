import wave
import matplotlib.pyplot as plt
import numpy as np

obj= wave.open("output.wav","rb")
sample_freq = obj.getframerate()
n_samples =obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio= n_samples/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int32)
times= np.linspace(0,t_audio,num = n_samples)

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Ses Sinyali")
plt.ylabel("Sinyal Dalgası")
plt.xlabel("Zaman(s)")
plt.xlim(0,t_audio)
plt.show()

obj_new =wave.open("Kayıt_new2.wav","wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(24000)
obj_new.writeframes(frames)
obj_new.close()