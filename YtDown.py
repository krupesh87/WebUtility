import tkinter as tk
import Main as Fu
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog



class YtDown:
    def __init__(self, root):
        root.title("Ankit's Youtube Downloader App")
        frame =Frame(root,bg ='black')
        frame.pack(expand =True,fill = BOTH)
        # f2 =Frame(frame,bg ='black')
        # f2.place(x=0,y=0,width =550,height=550)  
        f = Frame(frame,bd=2,relief="groove",bg ='#001112')
        f.place(x=200,y=100,width =500,height=300)
        video_Link = StringVar()
        video_Link.set("Enter YouTube Video's Link")
        download_Path = StringVar()
        download_Path.set("Enter Storage path")
        def openHome(event):
            f.pack_forget()
            app = Fu.WebUtility(root)
        def Browse():
            download_Directory = filedialog.askdirectory()
            download_Path.set(download_Directory)
    
        def Download():

            if str(video_Link.get()) == '':
                messagebox.showwarning('Alert','Youtube Link cannot be empty')
                return
            elif str(video_Link.get()) == "Enter YouTube Video's Link":
                messagebox.showwarning('Alert','Enter a Valid Youtube Link')
                return
            if str(download_Path.get()) =='':
                messagebox.showwarning('Alert','Destination Path cannot be empty')
                return
            elif str(download_Path.get()) =='Enter Storage path':
                messagebox.showwarning('Alert','Destination Path cannot be empty')
                return
            Youtube_link = video_Link.get()
            download_Folder = download_Path.get()
            try:
                getVideo = YouTube(Youtube_link)
                videoStream = getVideo.streams.first()
                videoStream.download(download_Folder)
                messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder)
            except:
                messagebox.showinfo("Alert" ,"Please Enter a Valid Youtube Link")
            video_Link.set("Enter YouTube Video's Link")
            linkText["bg"] = '#001112'
            download_Path.set("Enter Storage path")
            destinationText["bg"] = "#001112"


       
        #designing the Page :

        # link_label = Label(f,text="YouTube link  :",bg="#E8D579")
        # # link_label.grid(row=3,column=0,pady=5,padx=5)
        # link_label.place(x=10,y=20,)

        HeadLabel = Label(frame,text="Youtube Video Downloader",bd=2,relief="groove",bg ="#001112",fg="green" ,font='Arial 15 bold')
        HeadLabel.place(x=200,y=50,width= 500,height=40)

        linkText = Entry(f,width=55,textvariable=video_Link,bd =2,relief="groove",bg="#001112",fg="green")
        linkText["font"] ='Arial 12 bold'
        linkText.place(x=25,y=40,width= 450,height=30)
        def Text1(event):
            video_Link.set("")
            linkText["bg"] = 'black'
        linkText.bind("<Button>",Text1)
    
        destinationText = Entry(f,width=40,textvariable=download_Path,font = 'arial 12 bold',bd =2,relief="groove", bg="#001112",fg="green")
        destinationText.place(x=25,y=90,width= 450,height=30)
        def Text2(event):
            download_Path.set("")
            destinationText["bg"] = "black"
        destinationText.bind("<Button>",Text2)

        browse_B = Button(f,text="Browse",cursor= "hand2",command=Browse,bd =2,relief= "groove", width=10,bg="#001100",fg="green", font = 'arial 12 bold')
        browse_B.place(x=400,y=130,width= 75,height=30)

        Download_B = Button(f,text="Download",cursor= "hand2", command=Download,bd =2,relief= "groove", width=20,bg="#001100",fg="green", font = 'arial 12 bold')
        Download_B.place(x=200,y=200,width= 100,height=30)
        
        def home():
            frame.pack_forget()
            app = Fu.WebUtility(root)
        homeLabel = Button(frame,text = 'Home' ,bg = "#001112", fg = "green",cursor= "hand2",bd =2,relief= "groove",command=home, font = 'arial 12 bold')
        homeLabel.place(x = 400, y =450,width=100)
        
    