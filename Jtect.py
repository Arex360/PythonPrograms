import pyttsx3
from tkinter import *
root = Tk()
root.title("JTech Voice")
root.geometry("450x300")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def Say(audio):
    engine.say(audio)
    engine.runAndWait()
def male():
    engine.setProperty('voice', voices[0].id)
    a = Msg.get()
    Say(a)
def female():
    engine.setProperty('voice', voices[1].id)
    a = Msgf.get()
    Say(a)
    
def fun1():
    Msg.grid(row=4,padx=20,pady=10)
    Btn = Button(root,text="Speak",width=30,bg="red",fg="white")
    Btn.grid(row=5,padx=20,pady=10)
    Btn['command'] = male
def fun2():
    Msgf.grid(row=4,padx=20,pady=10)
    Btnf = Button(root,text="Speak",width=30,bg="red",fg="white")
    Btnf.grid(row=5,padx=20,pady=10)
    Btnf['command'] = female
Title = Label(root, text="Select  Voice  Assistant")
Title.grid(row=0)
Title = Label(root, text="JTech Solutions", fg="blue")
Title.grid(row=0,column=1)
btn1 = Button(root,text="Male",width=30,bg="blue",fg="white")
btn1.grid(row=1,column=0)
btn2 = Button(root,text="Female",width=30,bg="pink",fg="white")
btn2.grid(row=1,column=1,padx=10)
Msg = Entry(root,width=40)
Msgf = Entry(root,width=40)
btn1['command'] = fun1
btn2['command'] = fun2
