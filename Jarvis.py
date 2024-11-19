import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
import webbrowser
import smtplib
import sys
import time
import pyautogui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_ActivityGUI


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():

    speak('Allow me to introduce myself I am JARVIS. Designed by Sahil Gulati.')

    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    
    if hour>=0 and hour<=12:
        speak(f"Good Morning, its {tt}")

    elif hour>=12 and hour<=16:
        speak(f"Good Afternoon, its {tt}")
    
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am JARVIS sir! How can I help you?")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()    

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, language='en-in')        
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please....")
            return "none"
        query = query.lower()
        return query 

    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            if "open notepad" in self.query:
                ntpath = "C:\\WINDOWS\\system32\\notepad.exe"
                speak('Ok Sir! Opening Notepad')
                os.startfile(ntpath)

            elif "close notepad" in self.query:
                speak("Ok Sir! Closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open paint" in self.query:
                npath = "C:\\WINDOWS\\system32\\mspaint.exe"
                speak('Ok Sir! Opening paint')
                os.startfile(npath)

            elif "close paint" in self.query:
                speak("Ok Sir! Closing paint")
                os.system("taskkill /f /im mspaint.exe")

            elif "thank you" in self.query:
                speak('Thank You to you Sir! for making me.')

            elif "open command prompt" in self.query:
                speak('Ok Sir! Opening command prompt')
                os.system("start cmd")

            elif "wikipedia" in self.query:
                speak("Searching Wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)

            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strTime}")

            elif "open youtube" in self.query:
                webbrowser.open("https://www.youtube.com")
                speak('Ok Sir! Opening You Tube')

            elif "open google" in self.query:
                webbrowser.open("https://www.google.com")
                speak('Ok Sir! Opening Google')

            elif "open whatsapp" in self.query:
                webbrowser.open("https://web.whatsapp.com")
                speak('Ok Sir! Opening WhatsApp')

            elif "open hotstar" in self.query:
                webbrowser.open("https://www.hotstar.com")
                speak('Ok Sir! Opening Hotstar')

            elif "you can leave" in self.query:
                speak("Thanks for using me sir , have a good day.")
                sys.exit()

            elif "introduce" in self.query:
                speak("I am JARVIS. I was designed by Sahil Gulati. To make your work easy by helping you in controlling your PC.")

            elif "hello" in self.query:
                speak("HI,it's really good to hear from you sir. I hope you and your loved ones are safe and healthy.")

            elif "how are you" in self.query:
                speak("I am fine sir. You are very kind to ask, especially in these tempestuous times.")

            elif "close it" in self.query:
                pyautogui.hotkey('alt','f4')
                speak('Ok Sir!')

            elif "screenshot" in self.query:
                pyautogui.hotkey('winleft','prtscr')
                speak('Screenshot done sir.')

            elif "file manager" in self.query:
                pyautogui.hotkey('winleft','e')
                speak('Ok sir, opening file manager.')

            elif "new folder" in self.query:
                pyautogui.hotkey('ctrl','shift','n')
                speak('Done Sir! New folder has save on your desktop.')

            elif "task manager" in self.query:
                pyautogui.hotkey('ctrl','shift','esc')
                speak('Ok Sir! Opening Task Manager.')

            elif "bluetooth connection" in self.query:
                pyautogui.hotkey('winleft','k')
                speak('Ok Sir! Opening bluetooth connection')

            elif "open run" in self.query:
                pyautogui.hotkey('winleft','r')
                speak('Done Sir! Run opened')

            elif "minimise" in self.query:
                pyautogui.hotkey('winleft','d')
                speak('Done Sir!')

            elif "volume up" in self.query:
                pyautogui.press("volumeup")
                speak('Done sir ')

            elif "volume down" in self.query:
                pyautogui.press("volumedown")
                speak('done sir')

            elif "volume mute" in self.query or "mute" in self.query:
                pyautogui.press("volumemute")
                speak('Done sir')

            


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ActivityGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../project jarvis/jarvis 4.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../project jarvis/jarvis.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../project jarvis/jarvis 3.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../project jarvis/634aeafde3993421dbdf337d49f425dc.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("../project jarvis/jarvis 2.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate) 
        self.ui.textBrowser.setText(lable_date)
        self.ui.textBrowser_2.setText(lable_time)




app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



        
  
    