from tkinter import *
import tkinter as tk
import Main as Fu
from tkinter import messagebox,ttk
import random
import easygui as eg
import tool1 as tl
from PIL import Image, ImageTk

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
num = ['1','2','3','4','5','6','7','8','9','0']
cap_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
sp_char = ["<",">","-","/","@","!","~","#","&","?",":",";","(",")","[","]","*","^",".","?","+","%"]

def generate():
    result = ""
    for i in range(10):
        if i==5 :
            result += random.choice(sp_char)
        elif i>5:
            result += random.choice(num)            
        else:
            result += random.choice(alpha)


    return result

class PassGen:
    def __init__(self, root):
        
        root.title("Ankit's Password Generator App")

        frame = Frame(root,bg ='black')
        frame.pack(expand=True , fill =BOTH)
        f2 =Frame(frame,bg ='black')
        f2.place(x=0,y=0,width =550,height=550)
        self.f3 =Frame(frame,bg ='#001112')
        self.f3.place(x=550,y=0,width =350,height=550)
        f = Frame(frame,bd=2,relief="groove",bg ='#001112')
        f.place(x=25,y=100,width =500,height=300)
        
        
        GeneratedPass = StringVar()
        GeneratedPass.set("")
        passwordInfo = StringVar()
        arr = []
        info = []

        def change():
            GeneratedPass.set(generate())

        def save():
            if str(GeneratedPass.get()) == '':
                messagebox.showwarning('Alert','Generated Text Is Empty')
                return
            with open ('imp/passwords.imp' , 'r+') as filee:
                file_content = filee.read()
                if GeneratedPass.get() in file_content:
                    messagebox.showerror("Alert","Password Already exits")
                else:
                    with open ('imp/passwords.imp' , 'a+') as fileee:
                        arr.append(GeneratedPass.get())
                        inffo =eg.enterbox("Enter info for password")
                        info.append(inffo)
                        fileee.write(GeneratedPass.get()+"\n\n"+inffo +"\n")
                        messagebox.showinfo("Saved","Password Saved")
            Table()
            #Open Home page Function 
        
        def openHome():
            frame.pack_forget()
            app = Fu.WebUtility(root)
            
        def Inform(event):
            inf = event.widget.cget("text")
            number = int(inf[4:])
            innnfo =getPasswords()
            messagebox.showinfo("Information","Password "+innnfo[number -1][0] + " is for :" + innnfo[number-1][1])
        def getPasswords():
            with open ('imp/passwords.imp' , 'r+') as filee:
                file_content = filee.read()
                file_content = file_content.replace("\n\n", " ")
                file_content = file_content.replace("\n", ",")
                
                lst =file_content.split(",")
                for i in range(len(lst)):
                    lst[i]=lst[i].split(" ")
                
                return lst

        def copy(event):
            fV =event.widget.cget("text")
            root.clipboard_clear()
            root.clipboard_append(fV)
            # tl.CreateToolTip(event.widget, "Copied")
        
        def clearAll():
            with open ('imp/passwords.imp' , 'w+') as filee:
                filee.write("")
            Table()
        
        def Table():
            i=0
            Ty=40
            hgt=40
            self.f3.pack_forget()
            self.f3 =Frame(frame,bg ='#001112')
            self.f3.place(x=550,y=0,width =350,height=550)
            Head = Label(self.f3,text="Passwords Saved",bg="#001112",fg="green",font='arial 15 bold')
            Head.place(x=50,y=0,width=275,height=30)

            ClearBtn = Button(self.f3,text = 'Clear all' ,bg = "#001112", fg = "green",bd =2,relief= "groove",width = 5,command=clearAll,cursor = "hand2", font = 'arial 15 bold')
            ClearBtn.place(x = 240, y =500,width =100,height=40)
            pss =getPasswords()
            for i in range(len(pss)-1):
                # table0 = Label(self.f3,text=i+1,bg="#001112",fg="green",font='arial 13 bold')
                # table0.place(x=0,y=Ty,width=10,height=hgt)
                table1 = Label(self.f3,text=pss[i][0],bd=2,relief = "groove",bg="#001112",fg="green",cursor="hand2",font='arial 13 bold')
                table1.place(x=0,y=Ty,width=275,height=hgt)
                table1.bind("<Button>",copy)
                # temp = root.clipboard_get()
                # temp2 = table1["text"]
                # if temp == table1["text"]:
                #     tl.CreateToolTip(table1,"copied")
                # else:    
                tl.CreateToolTip(table1,"copy")
                image1 = Image.open("img/info.png")
                image1 =image1.resize((35,35), Image.ANTIALIAS)
                image2 = ImageTk.PhotoImage(image1)
                table2 = Label(self.f3,image =image2,text="Info"+str(i+1),bd=2,relief = "groove",bg="#001112",cursor="hand2",fg="green",font='arial 12 bold')
                table2.image =image2
                tl.CreateToolTip(table2,pss[i][1])
                table2.place(x=285,y=Ty,width=65,height=hgt)
                table2.bind("<Button>",Inform)
                Ty+=hgt
        Table()
        

        HeadLabel = Label(f2,text="Password Generator",bd=2,relief="groove",bg ="#001112",fg="green" ,font='Arial 15 bold')
        HeadLabel.place(x=25,y=30,width= 500,height=40)

        GenLabel = Label(f,textvariable = GeneratedPass,bg ="black",fg="green" ,font='Arial 12 bold')
        GenLabel.place(x=25,y=80,width= 450,height=40)
       
        GenerateBtn = Button(f,text="Generate",cursor= "hand2",command=change,width=10,bd =2,relief= "groove",bg="#010101",fg="green", font = 'arial 12 bold')
        GenerateBtn.place(x=100,y=200,width= 100,height=30)
        
        SaveBtn = Button(f,text="Save",cursor= "hand2",command=save,width=10,bd =2,relief= "groove",bg="#010101",fg="green",font = 'arial 12 bold')
        SaveBtn.place(x=300,y=200,width= 100,height=30)
        
        homeLabel = Button(f2,text = 'Home' ,bg = "#001112", fg = "green",bd =2,relief= "groove",width = 5,command=openHome,cursor = "hand2", font = 'arial 20 bold')
        homeLabel.place(x = 225, y =450,width =100,height=40)

        

