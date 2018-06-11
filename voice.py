import speech_recognition as sr
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
##audio = pyaudio.PyAudio()
##stream = audio.open(format=format,
##                              channels=channel,
##                              rate=48000,
##                              input=True,
##                              frames_per_buffer=chunk)

def listen():
    with sr.Microphone( device_index = 2) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
##            if text.lower() == 'cisco' or text.lower() =='sisca' or text.lower() =='sisco':
##                return 1
##            else:
##                return 0
        except Exception as e:
            print(e)
listen()


##while True:
##    data = stream.read(chunk, exception_on_overflow = False)
##    rms = audioop.rms(data, 2)  # get input volume
##    if rms > threshold:  # if input volume greater than threshold
##        with sr.Microphone( device_index = 2, sample_rate = 44100, chunk_size = 512) as source:
##            audio = r.listen(source)
##            try:
##                text = r.recognize_google(audio)
##                print(text)
##                if text.lower() == 'cisco' or text.lower() =='sisca' or text.lower() =='sisco':
##                    print("Catch")
##
##            except Exception as e:
##                print(e)


