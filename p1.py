from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import webbrowser

bot =ChatBot('Bot')
trainer=ListTrainer(bot)
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

for files in os.listdir('C:/Users/Siri/Desktop/ai/data/'):
    data= open('C:/Users/Siri/Desktop/ai/data/'+files,'r').readlines()
    trainer.train(data)




from tkinter import *
import tkinter.messagebox as tsmg
from tkinter import ttk
root=Tk()
root.title("Chatbot")
root.geometry("400x500")

message = StringVar()
res = StringVar()


head=Label(root,text="PUSBOT",fg="blue",bg="skyblue",font="70")
head.place(x=320,y=0)

def chatbox():
    global f,mylist
    sb = Scrollbar()
    sb.pack(side = RIGHT, fill = Y) 
    
    mylist = Listbox(root, yscrollcommand = sb.set ,height='35',width='120') 
    mylist.place(x=20,y=30)  
    sb.config()
    abcd()

'''def abc():
    global reply
    


        

    if message.get()!='Bye':
        reply=bot.get_response(message.get())
        #print('TARZ :',reply)

    if message.get()=='Bye':
        reply='bye'
        #print('TARZ :Bye')
    
        send()'''
    
def abcd():
    e2=Entry(root , font=('arial', 20),textvariable=message,width=25)
    e2.place(x=170,y=600)

    b2=Button(root,text="Send",font="8",bg="blue",fg="green",command=send)
    b2.place(x=520,y=600)
     
  
def send():

    if message.get()!='Bye':
        reply=bot.get_response(message.get())
        #print('TARZ :',reply)

    if message.get()=='Bye':
        reply='bye'
    res.set(reply)
    #l2=Label(root,text=msg.get(),fg="red",bg="white",font="20")
    #l2.place(x=50,y=i)
    mylist.insert(END,"YOU: --"+message.get())
    mylist.insert(END,"PUSbot: --"+res.get())
    #i=i+100
    message.set('')
    res.set('')

   

    
    abcd()

    
chatbox()
root.minsize(770,750)
root.mainloop()


