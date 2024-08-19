#Creating a simple to do list using tkinter and python
import tkinter
from tkinter import messagebox
def add_task():
    task=txt.get()
    if len(task)==0:
        messagebox.showinfo('Error',"The field is empty")
    else:
        tasks.append(task)
        update_list()
        txt.delete(0,'end')
        pass
def update_list():
    clear_list()
    for item in tasks:
        lb.insert('end',item)
def clear_list():
    lb.delete(0,'end')
def delete_task():
    del_task=del_txt.get()
    if len(tasks)==0:
        messagebox.showinfo('Error',"The list is empty")
    else:
        tasks.remove(del_task)
        update_list()
        del_txt.delete(0,'end')
        pass
def no_of_tasks():
    length=len(tasks)
    msg="Number of tasks = %d"%length
    messagebox.showinfo('Tasks',msg)
    

root=tkinter.Tk()
root.configure(bg='black')
root.title('TO DO LIST')
root.geometry('250x500')
tasks=[]
title= tkinter.Label(root,text='To Do List',bg='black')
title.pack()
display=tkinter.Label(root,text='',bg='black')
display.pack()
addtask=tkinter.Label(root,text="Add Task",fg='white',bg='black')
addtask.pack()
txt=tkinter.Entry(root,width=25)
txt.pack()
btnaddtask=tkinter.Button(root,text='Submit',fg='black',bg='white',command=add_task)
btnaddtask.pack()
deltask=tkinter.Label(root,text='Delete Task',fg='white',bg='black')
deltask.pack()
del_txt=tkinter.Entry(root,width=25)
del_txt.pack()
deletetask=tkinter.Button(root,text='Submit',fg='black',bg='white',command=delete_task)
deletetask.pack()
display1=tkinter.Label(root,text='',bg='black')
display1.pack()
deleteall=tkinter.Button(root,text='Delete All',fg='black',bg='white',command=clear_list)
deleteall.pack()
display2=tkinter.Label(root,text='',bg='black')
display2.pack()
nooftasks=tkinter.Button(root,text='Number of Tasks',fg='black',bg='white',command=no_of_tasks)
nooftasks.pack()

frame = tkinter.Frame(root)
frame.pack(pady=10)
lb = tkinter.Listbox(frame, width=25, height=8, bd=0, fg='black', bg='white')
lb.pack(side='left')
sb = tkinter.Scrollbar(frame, orient='vertical',command=lb.yview)
sb.pack(side='right', fill='y')
lb.config(yscrollcommand=sb.set)
root.mainloop()
