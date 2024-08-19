import tkinter
from tkinter import messagebox
from tkinter import *
expression = "" 
def show(value):  
	global expression 
	expression = expression + value 
	result.config(text=expression)

def equalpress():
    global expression
    result_text=''
    if expression!='':
        try:
            result_text=eval(expression)
        except:
            result_text='ERROR'
            expression = "" 
    result.config(text=result_text)

def clear(): 
	global expression 
	expression = "" 
	result.config(text=expression)


root=Tk()
root.configure(bg='white')
root.title("CALCULATOR")
root.geometry('500x600')
result=Label(root,width=25,height=2,text='',font=('arial',30),fg='white',bg='black')
result.pack()

Button(root,text='C',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='blue',command=lambda: clear()).place(x=20,y=100)
Button(root,text='/',width=4,height=1,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:show('/')).place(x=140,y=100)
Button(root,text='%',width=4,height=1,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:show('%')).place(x=260,y=100)
Button(root,text='*',width=4,height=1,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:show('*')).place(x=380,y=100)

Button(root,text='7',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('7')).place(x=20,y=200)
Button(root,text='8',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('8')).place(x=140,y=200)
Button(root,text='9',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('9')).place(x=260,y=200)
Button(root,text='-',width=4,height=1,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:show('-')).place(x=380,y=200)


Button(root,text='4',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('4')).place(x=20,y=300)
Button(root,text='5',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('5')).place(x=140,y=300)
Button(root,text='6',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('6')).place(x=260,y=300)
Button(root,text='+',width=4,height=1,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:show('+')).place(x=380,y=300)


Button(root,text='1',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('1')).place(x=20,y=400)
Button(root,text='2',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('2')).place(x=140,y=400)
Button(root,text='3',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('3')).place(x=260,y=400)
Button(root,text='=',width=4,height=3,font=('arial',30,'bold'),fg='black',bg='orange',command=lambda:equalpress()).place(x=380,y=400)

Button(root,text='0',width=9,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('0')).place(x=20,y=500)
Button(root,text='.',width=4,height=1,font=('arial',30,'bold'),fg='white',bg='black',command=lambda:show('.')).place(x=260,y=500)
root.mainloop()
