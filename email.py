from email.mime.text import MIMEText
from tkinter import *
from email.mime.multipart import MIMEMultipart
import smtplib
import webbrowser
root = Tk()
root.title("Send Email")
root.geometry("350x400")
def sendMail(event):
    source = email.get()
    password = password2.get()
    target = to.get()
    msg = MIMEMultipart()
    msg['From'] = source
    msg['To'] = target
    msg['Subject'] = subject.get()
    out = message.get()
    msg.attach(MIMEText(out,'plain'))
    text = msg.as_string()
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(source, password)
        server.sendmail(source,target,text)
        suc = Label(root, text = "Message Successfully sent", fg = "red")
        suc.pack()
    except:
        error = Label(root, text = "You don't have given access to gmail account to send email", fg = "red")
        error.pack()
        webbrowser.open("https://myaccount.google.com/lesssecureapps",new= 1)
lEmail = Label(root, text = "your email")
lEmail.pack()
email = Entry(root,width = 40)
email.pack()
lPassword = Label(root, text = "your Password")
lPassword.pack()
password2 = Entry(root,width = 40, show = "-")
password2.pack()
btn = Button(root, text = "Send")
lSubject = Label(root, text = "Enter Subject")
lSubject.pack()
subject = Entry(root,width = 40)
subject.pack()
lTo = Label(root, text = "Enter Address of user")
lTo.pack()
to = Entry(root,width = 40)
to.pack()
lMessage = Label(root, text = "Enter Message")
lMessage.pack()
message = Entry(root,width = 40)
message.pack()
btn.bind('<Button-1>',sendMail)
btn.pack()
root.mainloop()
