
import sounddevice as sd

import wavio


duration = 10.5
fs = 44100  # veya 48000
myRecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

sd.play(myRecording, fs)
sd.wait()


#wav a kaydetme
outputFile = "kayıt.wav"
wavio.write(outputFile, myRecording, fs, sampwidth=2)
print("Kayıt başarıyla kaydedildi:", outputFile)
