import tkinter as tk
from tkinter import *
from tkinter import ttk 

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("My_To_Do_List")
        #sets up the screen
        self.root.geometry('650*410+310+156')
        #creating the label
        self.label= Label(self.root, text='My To Do List', font='ariel, 25, bold, width=10 bd=5, bg="pink",fg="black')
        self.label.pack(side='top', fill=BOTH)


        self.label2= Label(self.root, text='Add Task', font='ariel, 18, bold, width=10 bd=5, bg="pink",fg="black')
        self.label.place(x="40", y="54")

        self.labe3= Label(self.root, text='Tasks', font='ariel, 18, bold, width=10 bd=5, bg="pink",fg="black')
        self.label.place(x=320, y=54)

        self.main_text = Listbox(self.root , height=9, bd=5, width=23,font='ariel, 25, italic bold')
        self.main_text.place(x=200,y=100)
        
        self.text = Text(self.root, font='ariel, 10, bold, width=30 bd=5,height=2')
        self.text.place(x=20, y=120)

        #functions
        def add():
            content = self.text.get(1,0,END)
            self.main.insert(END, content)
            with open('data.txt','w') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)

        def delete():
            delete_ = self.main.text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek()
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)

            f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt','r')as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END,ready)
        file.close()

        self.button = Button(self.root, text='Add', font='sarif,20,bold italic', width=10,
                            bd=5,bg='pink', fg='black',command=add)
        self.button.place(x=20, y=100)

        self.button2 = Button(self.root, text='Delete', font='sarif,20,bold italic', width=10,
                            bd=5,bg='pink', fg='black',command=delete)
        self.button2.place(x=20, y=280)




def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()