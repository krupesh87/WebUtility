#import library
from tkinter import *
import tkinter as tk
# import main as m
import Main as Fu
from tkinter import messagebox,ttk
from PIL import Image, ImageTk
import tool1 as tl
class WebBlock:
    def __init__(self, root):
        
        root.title("Ankit's WebBlock App")

        frame = Frame(root,bg ='black')
        frame.pack(expand=True , fill =BOTH)
        f2 =Frame(frame,bg ='black')
        f2.place(x=0,y=0,width =550,height=550)
        self.f3 =Frame(frame,bg ='#001112')
        self.f3.place(x=550,y=0,width =350,height=550)

        f = Frame(frame,bg ='#001112',bd=2,relief="groove")
        f.place(x=25,y=100,width =500,height=300)
        
        Websites = StringVar()
        Websites.set("Enter Websites here")
        arr =[]
        Blockedarr = []

        host_path = 'C:\Windows\System32\drivers\etc\hosts'
        ip_address = '127.0.0.1'

        #block function
        def Blocker():
            if str(Websites.get()) == '':
                messagebox.showwarning('Alert','Website Links cannot be empty')
                return
            elif str(Websites.get()) == "Enter Websites here":
                messagebox.showwarning('Alert','Website Links cannot be empty')
                return
            
            website_lists = Websites.get()
            Website = list(website_lists.split(","))
            
            with open (host_path , 'r+') as host_file:
                file_content = host_file.read()
                for website in Website:
                    if website in file_content:
                        messagebox.showinfo("Alert", "Already Blocked")
                        pass
                    elif 'www' in website:
                        host_file.write(ip_address + " " + website + '\n')
                        arr.append(website)
                    else:
                        host_file.write(ip_address + " www." + website + '\n')
                        arr.append(website)

        def getBlocked():
            with open (host_path , 'r+') as host_file:
                file_content = host_file.read()
                file_content = file_content.replace("127.0.0.1 ", "")
                file_content = file_content.replace("\n", " ")
                # print(file_content)
                lst = list(file_content.split(" "))
                return lst
        
        #Open Home page Function 
        def openHome():
            frame.pack_forget()
            app = Fu.WebUtility(root)
            
        WebText = Entry(f,width=55, textvariable= Websites,bd =2,relief= "groove",bg="#001112" ,fg="green")
        WebText["font"] ='Arial 12 bold'
        WebText.place(x=25,y=80,width= 450,height=40)
        def Text1(event):
            Websites.set("")
            WebText["font"] = 'Arial 12 bold'
            WebText["bg"] = 'black'
        WebText.bind("<Button>",Text1)
        
        def Unblock(event):
            temp = event.widget.cget("text")
            temp = int(temp[7:]) -1
            websiteToBeUnblocked = arr[temp]
            with open (host_path , 'r') as host_file:
                file_content = host_file.read()
                file_content = file_content.replace(ip_address + " " + websiteToBeUnblocked + '\n', "")
                arr.pop(temp)
            with open (host_path , 'w') as hst:  
                hst.write(file_content)
            messagebox.showinfo("UnBlocked", "UnBlocked " + websiteToBeUnblocked )
            Table()
    
        def Table():
            self.f3.pack_forget()
            self.f3 =Frame(frame,bg ='#001112')
            self.f3.place(x=550,y=0,width =350,height=550)
            Head = Label(self.f3,text="Blocked Websites",bg="#001112",fg="green",font='arial 13 bold')
            Head.place(x=40,y=0,width=275,height=30)
            # f3.pack()
            i=0
            Ty=40
            hgt=40
            Blocker =[]
            Blockedarr = getBlocked()
            image1 = Image.open("img/unlock5.png")
            image1 =image1.resize((35,35), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image1)
            for i in range(len(Blockedarr)-1):
                # table0 = Label(f3,text=i+1,bg="#001112",fg="green",font='arial 13 bold')
                # table0.place(x=0,y=Ty,width=10,height=hgt)
                table1 = Label(self.f3,text=Blockedarr[i],bd=2,relief = "groove",bg="#001112",fg="green",cursor="hand2",font='arial 13 bold')
                table1.place(x=0,y=Ty,width=275,height=hgt)
                table2 = Label(self.f3,image=image2,text="Unblock"+str(i+1),bd=2,relief = "groove",bg="#001112",cursor="hand2",fg="green",font='arial 12 bold')
                tl.CreateToolTip(table2,"UnBlock")
                table2.image = image2
                table2.place(x=270,y=Ty,width=75,height=hgt)
                table2.bind("<Button>",Unblock)
                Ty+=hgt
                arr.append(Blockedarr[i])
        def Gen():
            
            Blocker()
            Table()
            Websites.set("")
        Table()

        HeadLabel = Label(f2,text="Website Blocker",bg ="#001112",bd=2,relief="groove",fg="green" ,font='Arial 15 bold')
        HeadLabel.place(x=25,y=50,width= 500,height=40)

        BlockBtn = Button(f,text="Block",cursor= "hand2",command=Gen,bd =2,relief= "groove",width=10,bg="#010101",fg="green",font = 'arial 12 bold')
        BlockBtn.place(x=200,y=200,width= 100,height=30)

        homeLabel = Button(f2,text = 'Home' ,bg = "#001112", fg = "green",bd =2,relief= "groove",width = 5,command=openHome,cursor = "hand2", font = 'arial 20 bold')
        homeLabel.place(x = 225, y =450,width =100,height=40)

        
                


