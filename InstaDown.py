from tkinter import *
import tkinter as tk
import Main as Fu
from tkinter import messagebox,ttk
import instaloader
import tool1 as tl
import webbrowser
from PIL import Image,ImageTk
class InstaDown:
    def __init__(self, root):
        
        root.title("WebBlock App")

        frame = Frame(root,bg ='black')
        frame.pack(expand=True , fill =BOTH)
        f2 =Frame(frame,bg ='black')
        f2.place(x=0,y=0,width =550,height=550)
        
        f = Frame(frame,bd=2,relief="groove",bg ='#001112')
        f.place(x=25,y=100,width =400,height=300)
        
        # f4 =Frame(frame,bg ='black')
        # mycanvas=Canvas(f4)
        # mycanvas.pack(side = LEFT,fill="both",expand=True)
        # yscrollbar=Scrollbar(f4,orient="vertical",command=mycanvas.yview)
        # yscrollbar.pack(side=RIGHT,fill=Y)
        # mycanvas.configure(yscrollcommand=yscrollbar.set)
        # mycanvas.bind('<Configure>',lambda e:mycanvas.configure(scrollregion = mycanvas.bbox('all')))   
        self.f3 =Frame(frame,bg ='#001112')
        self.f3.place(x=450,y=0,width =450,height=550)
        # mycanvas.create_window((20,0),window=self.f3,anchor='nw')
        # f4.place(x=450,y=0,width =450,height=550)
        # for i in range(25):
        #     btn = Button(self.f3,text="wroki")
        #     btn.pack()
        L = instaloader.Instaloader()        
        Username = StringVar()
        Username.set("Enter Instagram Username")
    

        #Open Home page Function 
        def openHome():
            frame.pack_forget()
            app = Fu.WebUtility(root)
            
        
        arr= []
        arr2 =[]
        def Get_Posts():
            if str(Username.get()) == '':
                messagebox.showwarning('Alert','Username cannot be empty')
                return
            elif str(Username.get()) == "Enter Instagram Username":
                messagebox.showwarning('Alert','Enter a Valid Username')
                return
            
            try:
                L = instaloader.Instaloader()
                
                posts = instaloader.Profile.from_username(L.context, Username.get()).get_posts()
                arr.clear()
                # f4.pack_forget()
                for post in posts:
                    arr2.append(post)
                    p = str(post)
                    p = p[6:len(p)-1]
                    arr.append("https://www.instagram.com/p/" + p)
                UpdateLabel("Photos Extracted")
            except:
                messagebox.showwarning('Alert','Enter a Valid Username')
                UpdateLabel("Error occured")


        def Download(event):
            d =event.widget.cget("text")
            d=int(d[8:])
            L= instaloader.Instaloader()
            L.download_post(arr2[d-1], str(Username.get()) + "-Instapics")
            messagebox.showinfo("Downloaded","Post is Downloaded in " + Username.get() + " Named Folder")

        
        def check(event):
            d =event.widget.cget("text")
            webbrowser.open(d)
        def Table():
            i=0
            Ty=40
            hgt=40
            self.f3.pack_forget()
            self.f3 =Frame(frame,bg ='#001112')
            self.f3.place(x=450,y=0,width =450,height=550)
            Head = Label(self.f3,text="Generated Posts",bg="#001112",fg="green",font='arial 15 bold')
            Head.place(x=80,y=0,width=275,height=30)
            image1 = Image.open("img/download.png")
            image1 =image1.resize((35,35), Image.ANTIALIAS)
            image2 = ImageTk.PhotoImage(image1)
            for i in range(len(arr)):
                
                # table0 = Label(f3,text=i+1,bg="#001112",fg="green",font='arial 13 bold')
                # table0.place(x=0,y=Ty,width=10,height=hgt)
                table1 = Label(self.f3,text=arr[i],bd=2,relief = "groove",bg="#001112",fg="green",cursor="hand2",font='arial 13 bold')
                table1.place(x=0,y=Ty,width=400,height=hgt)
                table1.bind("<Button>",check)   
                tl.CreateToolTip(table1,"Check Photo")
                
                table2 = Label(self.f3,image = image2,text="Download"+str(i+1),bd=2,relief = "groove",bg="#001112",cursor="hand2",fg="green",font='arial 12 bold')
                table2.image = image2
                tl.CreateToolTip(table2,"Download Photo")
                table2.place(x=410,y=Ty,width=40,height=hgt)
                table2.bind("<Button>",Download)
                Ty+=hgt
        
        def UpdateLabel(text):
            self.UpdLabel.pack_forget()
            self.UpdLabel = Label(f,text =text,bg ="#001112",fg="green" ,font='Arial 15 bold')
            self.UpdLabel.place(x=70,y=250,width= 260,height=40)

        def Gen():
            Get_Posts()
            Table()
        Table()

        
        self.UpdLabel = Label(f,text="",bg ="#001112",fg="green" ,font='Arial 15 bold')
        self.UpdLabel.place(x=70,y=250,width= 260,height=40)

        HeadLabel = Label(frame,text="Instagram Post Downloader",bd=2,relief="groove",bg ="#001112",fg="green" ,font='Arial 15 bold')
        HeadLabel.place(x=25,y=50,width= 400,height=40)

        userId = Entry(f,width=55, textvariable= Username,bg="#001112" ,bd=2,relief="groove",fg="green",font = "Arial 12 bold")
        userId.place(x=25,y=80,width= 350,height=40)
        def Text1(event):
            UpdateLabel("")
            Username.set("")
            userId["font"] = 'Arial 12 bold'
            userId["bg"] = 'black'
        userId.bind("<Button>",Text1)
        
        GenerateBtn = Button(f,text="Generate Posts",cursor= "hand2",command=Gen,width=10,bg="#000101",fg="green",bd=2,relief="groove", font = 'arial 12 bold')
        GenerateBtn.place(x=100,y=200,width= 200,height=30)

        homeLabel = Button(f2,text = 'Home' ,bg = "#001112", fg = "green",width = 5,bd=2,relief="groove",command=openHome,cursor = "hand2", font = 'arial 20 bold')
        homeLabel.place(x = 175, y =450,width =100,height=40)

        
                


