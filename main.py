import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

try:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
except sr.UnknownValueError as e:
    print(e)

input = r.recognize_google(audio).lower()

if 'hello' in input:
    engine.say('Hello How are you sir.')
    engine.runAndWait()
else:
    engine.say('I am not able to get you.')
    engine.runAndWait()
