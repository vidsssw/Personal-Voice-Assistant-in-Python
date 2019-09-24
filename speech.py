from time import ctime
import time
import os
from gtts import gTTS
global name
import pyttsx3
import speech_recognition as sr

def speak2(data):
    engine = pyttsx3.init()

    engine.say(data)

    engine.runAndWait()

def speak(data):
    print(data)
    tts=gTTS(text=data,lang='en')
    tts.save("audio.mp3")
    os.system("start audio.mp3")

def recordaudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)

    data=""
    try:
        data=r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't understand!")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return data

def q():
    speak2("Anything else?")
    d=recordaudio()
    if 'nothing' in d:
        speak2("okay bye")
        exit()

def jarvis(data):
    global name
    if 'how are you' in data:
        speak2("I'm good")
        q()

    elif 'what is my name' in data:
        speak2("Your name is "+name)
        speak2("I hope you aren't as ugly as your name.")
        q()
    elif 'time is it' in data:
        speak2(ctime())
        q()
    elif 'where is' in data:
        data=data.split(" ")
        loc=data[2]
        speak2("Hold on"+name+", I will show you where " + loc + " is.")
        speak2("Now you can go here and die")
        os.system("chromium-browser https://www.google.nl/maps/place/" + loc + "/&amp;")



#speak("Hi! What is your name? ")
speak2("Hi, What is your name? ")
name=recordaudio()
speak2("Welcome"+name)
while(1):
    speak2("What should I do for you?")
    data=recordaudio()
    jarvis(data)
