import os
import webbrowser

import pyttsx3
import speech_recognition as sr

greeting_list = ["hello jarvis", "hi jarvis", "wake up jarvis"]
launch_list = ['open', 'launch']

folder_dic = {"desktop": "/Users/akhileshsingh/Desktop", "driver": "/Users/akhileshsingh/Desktop/Drivers",
              "facebook": "https://facebook.com", "music": "/System/Applications/Music.app"}
try:
    engine = pyttsx3.init()
except Exception as e:
    print(e)

r = sr.Recognizer()
mic = sr.Microphone()

# getting os details
os_info = os.uname().sysname


# To speak the response or output
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Validating voice input to perform specific action
def validate_voice_input(list_, input):
    for value in list_:
        if value in input:
            return True
    else:
        return False


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

    if validate_voice_input(greeting_list, input):
        speak('Hello, How are you sir.')

    elif validate_voice_input(launch_list, input):
        for name, path in folder_dic.items():
            key = ''
            for value in launch_list:
                try:
                    key = input.split(value)[1].strip().lower()
                except IndexError:
                    pass
            value = folder_dic.get(key)
            if value is not None:
                speak('Sure sir.')
                os_info = 'Windows'
                if os_info == 'Darwin':
                    cmd = 'open {}'.format(value)
                    os.system(cmd)
                elif os_info == 'Windows':
                    if 'http' in value:
                        webbrowser.open(value)
                    elif '.exe' in value:
                        cmd = 'run {}'.format(value)
                        os.system(cmd)
                    else:
                        cmd = 'open {}'.format(value)
                        os.system(cmd)
            break
    else:
        print('Command not found.')
