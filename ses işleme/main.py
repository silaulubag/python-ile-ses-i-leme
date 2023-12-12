import wave

obj = wave.open("output.wav","rb")

print("Number of Channels", obj.getnchannels())
print("sample width",obj.getsampwidth())
print("sample framerate",obj.getframerate())
print("Frame sayisi", obj.getnframes())
print("parametres",obj.getparams())


t_audio = obj.getnframes()/obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/4.0)
#birebir aynısı
obj_new =wave.open("Kayıt_new.wav","wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000)
obj_new.writeframes(frames)
obj_new.close()

obj_new =wave.open("Kayıt_new1.wav","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(3)
obj_new.setframerate(4000)
obj_new.writeframes(frames)
obj_new.close()

