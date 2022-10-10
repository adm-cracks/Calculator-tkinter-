from tkinter import *
root=Tk()
root.config(background="white")
root.title("Cal")
root.geometry("190x270")
def press(num):
    global ex_var
    ex_var=ex_var+str(num)
    l1["text"]=ex_var
def evale():
    global ex_var
    resu=str(eval(ex_var))
    l1["text"]=resu
    ex_var=""
def clear():
    
    global ex_var
    ex_var=''
    l1["text"]=ex_var  
ex_var=''
eq=StringVar()
f1=Frame(root,width=30,height=20)
f1.place(x=20,y=0)
l1=Label(f1,textvariable='',font=('Arial',20),bg="white")
l1.pack(expand=TRUE,fill=BOTH)
b1=Button(root,text="1",border=4,width=3,height=2,command=lambda:press(1))
b1.place(x=20,y=50)
b1=Button(root,text="2",border=4,width=3,height=2,command=lambda:press(2))
b1.place(x=60,y=50)
b1=Button(root,text="3",border=4,width=3,height=2,command=lambda:press(3))
b1.place(x=100,y=50)
b1=Button(root,text="+",border=4,width=3,height=2,command=lambda:press("+"))
b1.place(x=140,y=50)
b1=Button(root,text="4",border=4,width=3,height=2,command=lambda:press(4))
b1.place(x=20,y=100)
b1=Button(root,text="5",border=4,width=3,height=2,command=lambda:press(5))
b1.place(x=60,y=100)
b1=Button(root,text="6",border=4,width=3,height=2,command=lambda:press(6))
b1.place(x=100,y=100)
b1=Button(root,text="-",border=4,width=3,height=2,command=lambda:press("-"))
b1.place(x=140,y=100)
b1=Button(root,text="7",border=4,width=3,height=2,command=lambda:press(7))
b1.place(x=20,y=150)
b1=Button(root,text="8",border=4,width=3,height=2,command=lambda:press(8))
b1.place(x=60,y=150)
b1=Button(root,text="9",border=4,width=3,height=2,command=lambda:press(9))
b1.place(x=100,y=150)
b1=Button(root,text="*",border=4,width=3,height=2,command=lambda:press("*"))
b1.place(x=140,y=150)
b1=Button(root,text="Ac",border=4,width=3,height=2,command=lambda:clear())
b1.place(x=20,y=200)
b1=Button(root,text="0",border=4,width=3,height=2,command=lambda:press(0))
b1.place(x=60,y=200)
b1=Button(root,text="=",border=4,width=3,height=2,command=evale)
b1.place(x=100,y=200)
b1=Button(root,text="/",border=4,width=3,height=2,command=lambda:press("/"))
b1.place(x=140,y=200)

root.mainloop()
