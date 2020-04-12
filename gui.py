from tkinter import *
import tkinter.messagebox as tsmg
from tkinter import ttk
root=Tk()
root.title("Chatbot")
root.geometry("400x500")

msg = StringVar()

head=Label(root,text="PUSBOT",fg="blue",bg="skyblue",font="50")
head.place(x=150,y=0)

def chatbox():
    global f,mylist
    sb = Scrollbar()
    sb.pack(side = RIGHT, fill = Y) 
    
    mylist = Listbox(root, yscrollcommand = sb.set ,height='23',width='50') 
    mylist.place(x=50,y=50)  
    sb.config()
    abc()
    
def abc():
    e2=Entry(root , font=('arial', 15),textvariable=msg,width=25)
    e2.place(x=50,y=450)

    b2=Button(root,text="Send",font="8",bg="blue",fg="green",command=send)
    b2.place(x=300,y=450)
     
  
def send():
    global i
    i=50
    #l2=Label(root,text=msg.get(),fg="red",bg="white",font="20")
    #l2.place(x=50,y=i)
    mylist.insert(END,"you: --"+msg.get())
    i=i+100
    msg.set('')

   

    
    abc()

    
chatbox()
root.mainloop()
