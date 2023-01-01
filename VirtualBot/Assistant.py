import pyttsx3
import speech_recognition as sr
import datetime
from wikipedia import *
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
from pynput.keyboard import Key, Controller
import subprocess
import pyautogui
from AshBot import *


#Intialisation
keyboard =  Controller()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Assistant Functions
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
#########################################################
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
##########################################################
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am ASHBOT. Please tell me how may I help you")
############################################################
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
#        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-in')
        print(f"User said: {text}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return text
#########################################################

# Commands/Funtions

def openLink(link):
    webbrowser.open(link)

def search(topic):
    pywhatkit.search(topic)

def playonyt(video):
    pywhatkit.playonyt(video)

def time():
    return datetime.datetime.now().strftime("%I:%M %p")

def openApp(app):
    os.startfile(app)

def cmdCommand(command):
    os.system(command)

def type(text):
    keyboard.type(text)

def press(button):
    keyboard.press(button)
    keyboard.release(button)

def deleteAll():
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)

def selectAll():
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)

def delete():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def copyText():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def pasteText():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def closeTab():
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)

def snipingTool():
    with pyautogui.hold('win'):
        with pyautogui.hold('shift'):
            pyautogui.press('s')

def desktop():
    with pyautogui.hold('win'):
        pyautogui.press('d')

def wikipedia(text):
    results = wikipedia.summary(text, sentences = 2)
    return results
