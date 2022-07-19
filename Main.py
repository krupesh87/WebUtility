import tkinter as tk
import tkinter.font as tkFont
from tkinter import Label,messagebox
from tkinter import *
import YtDown as Yt
import WebBlock as WB
import PassGen as PG
import InstaDown as IG
import easygui as eg


class WebUtility:
    def __init__(self, root):
        root.title("WebUtils App")

        f = Frame(root,bg= "#001112")
        f.pack(expand =True,fill=BOTH)

        Title=tk.Label(f)
        Title["bg"] = "#001112"
        ft = tkFont.Font(family='Times',size=43)
        Title["font"] = ft
        Title["fg"] = "green"
        Title["justify"] = "left"
        Title["text"] = " Web Utility"
        Title.place(x=210,y=70,width=458,height=100)

        def YTDBcmd():
            f.pack_forget()
            app = Yt.YtDown(root)
        YTDB=tk.Button(f)
        YTDB["bg"] = "#001112"
        YTDB["cursor"] = "hand2"        
        ft = tkFont.Font(family='Times',size=18)
        YTDB["font"] = ft
        YTDB["fg"] = "green"
        YTDB["justify"] = "center"
        YTDB["text"] = "YouTube Video \n Downloader"
        YTDB["relief"] = "groove"
        YTDB.place(x=70,y=250,width=300,height=103)
        YTDB["command"] = YTDBcmd

        Password = "Ap492"
        def PGBcmd():
            if eg.enterbox("Enter Password to access") == Password:
                f.pack_forget()
                app = PG.PassGen(root)
            else:
                messagebox.showinfo("Wrong Password","Enter a Valid password Try again")
        PGB=tk.Button(f)
        PGB["bg"] = "#001112"
        PGB["cursor"] = "hand2"
        ft = tkFont.Font(family='Times',size=18)
        PGB["font"] = ft
        PGB["fg"] = "green"
        PGB["justify"] = "center"
        PGB["relief"] = "groove"
        PGB["text"] = "Password \nGenerator"
        PGB.place(x=400,y=250,width=200,height=103)
        PGB["command"] = PGBcmd

        SGB=tk.Label(f)
        SGB["bg"] = "#001112"
        SGB["relief"] = "groove"
        SGB["text"] = ""
        SGB.place(x=630,y=250,width=200,height=103)

        AGB=tk.Label(f)
        AGB["bg"] = "#001112"
        AGB["relief"] = "groove"
        AGB["text"] = ""
        AGB.place(x=70,y=373,width=200,height=103)
        
        def IPDBcmd():
            f.pack_forget()
            app = IG.InstaDown(root)
        IPDB=tk.Button(f)
        IPDB["bg"] = "#001112"
        IPDB["cursor"] = "hand2"
        ft = tkFont.Font(family='Times',size=18)
        IPDB["font"] = ft
        IPDB["fg"] = "green"
        IPDB["justify"] = "center"
        IPDB["relief"] = "groove"
        IPDB["text"] = "Instagram Photo \n Downloader "
        IPDB.place(x=300,y=373,width=300,height=103)
        IPDB["command"] = IPDBcmd


        def WBBcmd():
            f.pack_forget()
            app = WB.WebBlock(root)
        WBB=tk.Button(f)
        WBB["bg"] = "#001112"
        WBB["cursor"] = "hand2"
        ft = tkFont.Font(family='Times',size=18)
        WBB["font"] = ft
        WBB["fg"] = "green"
        WBB["justify"] = "center"
        WBB["relief"] = "groove"
        WBB["text"] = "Website Blocker"
        WBB.place(x=630,y=373,width=200,height=103)
        WBB["command"] = WBBcmd

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x550+300+100")
    # root.iconbitmap('img/browser.ico')
    img = PhotoImage(file='C:/ANKIT/Ankit python/WebUtils/img/browser2.png')
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.resizable(0,0)
    app = WebUtility(root)
    root.mainloop()
