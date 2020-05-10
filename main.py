import os

import pyttsx3
import speech_recognition as sr

folder_dic = {"desktop": "/Users/akhileshsingh/Desktop", "driver": "/Users/akhileshsingh/Desktop/Drivers"}
try:
    engine = pyttsx3.init()
except Exception as e:
    print(e)

r = sr.Recognizer()
mic = sr.Microphone()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print('Listening...')
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            return r.recognize_google(audio).lower()
    except sr.UnknownValueError as e:
        print(e)
    except sr.WaitTimeoutError as e:
        print(e)
    except Exception as e:
        print(e)


while True:
    input = listen()
    print(input)
    if 'hello' in input:
        speak('Hello How are you sir.')
    elif 'open' in input:
        for name, path in folder_dic.items():
            key = input.split('open ')[1].strip().lower()
            value = folder_dic.get(key)
            cmd = 'open {}'.format(value)
            os.system(cmd)
            break
    else:
        print('Command not found.')
