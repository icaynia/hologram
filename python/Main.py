
import ImageUpload
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import *
import os
import time
try:
    from PIL import Image
    from PIL import ImageTk #gif 및 jpg bmp 파일을 읽을 수 있다.
except ImportError as err :
    messagebox.showerror("모듈 없음", "PIL 모듈을 설치해주세요")
try:
    import requests
except ImportError as err:
    messagebox.showerror("모듈 없음", "requests 모듈을 설치해주세요")

class HologramImageUpload:
    def __init__ (self):
        self.root = tkinter.Tk()
        self.root.title("ImageUploader")
        self.label = tkinter.Label(self.root, text = "", width=50, height = 20)
        self.label.pack()
        self.fileOpenButton = tkinter.Button(self.root, text = "UPLoadImage", command = self.OpenFile)
        self.fileOpenButton.pack(side = tkinter.constants.LEFT)
        self.urlLinkInput = tkinter.Entry(self.root)
        self.urlLinkInput.pack(side = tkinter.constants.LEFT)
        self.sendUrlLinkButton = tkinter.Button(self.root, text = "urlLinkSend", command = self.sendUrlLink)
        self.sendUrlLinkButton.pack(side = tkinter.constants.RIGHT)
        self.urlLinkInput.bind("<Key-Return>", self.sendUrlLink)
        self.root.mainloop()
    def OpenFile(self):
        self.FilePath = filedialog.askopenfilename()
        if(self.FilePath == ""): 
            return 
        try: 
            self.image=Image.open(self.FilePath) 
        except: 
            messagebox.showerror(u"오류 !","파일 열기에 실패했습니다") 
        else: 
            self.pixel=self.image.load() 
            self.label.image=ImageTk.PhotoImage(self.image)
            tkinter.Label.__init__(self.label, self.root, image = self.label.image, bd = 0)
            self.label.pack(side = tkinter.constants.TOP)
            ImageUpload.sendImage("hologram-ftp.icaynia.com","ww_ghaha12", "tktk8899", self.FilePath)

    def urlLinkInput_Return(self, event):
        sendUrlLink()
    def urlLinkInputButton_Clicked(self):
        sendUrlLink()        
    def sendUrlLink(self):
        self.urlLink = str(self.urlLinkInput.get())


Client = HologramImageUpload()