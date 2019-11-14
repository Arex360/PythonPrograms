import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from tkinter import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def Say(audio):
    engine.say(audio)
    engine.runAndWait()
def add():
    a = int(input2.get())
    b = int(input3.get())
    c = a + b
    ans = str(c)
    Say(input2.get()+ " plus" + input3.get() + " is " + ans)
def sub():
    a = int(input2.get())
    b = int(input3.get())
    c = a - b
    ans = str(c)
    Say(input2.get()+ " minus" + input3.get() + " is " + ans)
def div():
    a = int(input2.get())
    b = int(input3.get())
    c = a / b
    ans = str(c)
    Say(input2.get()+ " over" + input3.get() + " is " + ans)
def mult():
    a = int(input2.get())
    b = int(input3.get())
    c = a + b
    ans = str(c)
    Say(input2.get()+ " multiply" + input3.get() + " is " + ans)
def Speak(event):
    output = input1.get()
    if "your name" in output:
        Say("My name is Arex")
        Say("I am AI Bot. I am under development but still I am sure I may help you")
    elif "your developer" in output:
        Say("Mohammad Owais Created me on May 20, 2019")
    elif "add" in output:
        add()
    elif "substract" in output:
        sub()
    elif "multiply" in output:
        mult()
    elif "divide" in output:
        div()
root = Tk()
LInput1 = Label(root, text = "What do you want from me? ")
LInput1.pack()
input1 = Entry(root)
input1.pack()
LInput2 = Label(root, text = "Input 1 (In case)")
LInput2.pack()
input2 = Entry(root)
input2.pack()
LInput3 = Label(root, text = "Input 2 (In case)")
LInput3.pack()
input3 = Entry(root)
input3.pack()
LInput4 = Label(root, text = "Email Address")
LInput4.pack()
input4 = Entry(root)
input4.pack()
LInput5 = Label(root, text = "Email Password")
LInput5.pack()
input5 = Entry(root)
input5.pack()
LInput6 = Label(root, text = "Subject")
LInput6.pack()
input6 = Entry(root)
input6.pack()
LInput7 = Label(root, text = "Target Address")
LInput7.pack()
input7 = Entry(root)
input7.pack()
LInput8 = Label(root, text = "Message")
LInput8.pack()
input8 = Entry(root)
input8.pack()
btn1 = Button(root, text = "Click")
btn1.pack()
btn1.bind('<Button-1>',Speak)

