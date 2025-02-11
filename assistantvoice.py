import pyttsx3
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
from tkinter import *
from PIL import ImageTk,Image
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am sandy, how can i help you sir")       

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    
     query=takeCommand().lower()
     if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10,)
            speak("According to Wikipedia")
        
            print(results)
            speak(results)
       
     elif 'open instagram' in query:
           webbrowser.open("instagram.com")

     elif 'open youtube' in query:
           webbrowser.open("youtube.com")

     elif 'open google' in query:
           webbrowser.open("google.com")
        
     elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
            print(strTime)

     elif 'open ' in query:
           webbrowser.open("google.com")

class widget:
     def __init__(self):
      self.mausam=Tk()
      self.mausam.geometry("520x320")
      photo1=PhotoImage(file="stu3.png",width=600,height=180)
      anjali_label=Label(image=photo1)
      anjali_label.pack()
      anjali_label.place(x=380,y=0,width=500,height=180)

     user_text=StringVar()
     user_text.set("your virtual assistant")

     userframe=LabelFrame(self.mausam,borderwidth=3,background="black",width=500,height=600)
     userframe.pack(fill=BOTH)

     top=Message(userframe,textvariable=userframe,bg="black",fg="pink")
     top.config(font=("times new roman",15,"bold"))
     top.pack()
     btn=Button(root,text="run",font=("times new roman",15,"bold"))
     btn.pack()
     btn2=Button(root,text="close",font=("times new roman",15,"bold"))
     btn2.pack()
root=Tk()
root.geometry("300x400")

root.mainloop()
