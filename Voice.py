import speech_recognition as sr
from grpc.framework.foundation import stream
import pyaudio
import audioop

r = sr.Recognizer()

# soundtrack properties
format = pyaudio.paInt16
rate = 16000
channel = 1
chunk = 1024
threshold = 150
file = 'audio.wav'

# intialise microphone stream
audio = pyaudio.PyAudio()
stream = audio.open(format=format,
                              channels=channel,
                              rate=rate,
                              input=True,
                              frames_per_buffer=chunk)

while True:
    data = stream.read(chunk, exception_on_overflow = False)
    rms = audioop.rms(data, 2)  # get input volume
    if rms > threshold:  # if input volume greater than threshold
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                if text.lower() == 'cisco' or text.lower() =='sisca' or text.lower() =='sisco':
                    print("Catch")

            except Exception as e:
                print(e)

