import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter.constants import *
try:
    from PIL import Image
    from PIL import ImageTk #gif 및 jpg bmp 파일을 읽을 수 있다.
    import RequestHologram
except ImportError as err :
    messagebox.showerror("error", "please, install PIL module and request module")
    exit()

ip = "http://192.168.123.189:3000/upload"

class HologramImageUpload:
    def __init__ (self):
        self.root = tkinter.Tk()
        self.root.title("ImageUploader")
        self.label = tkinter.Label(self.root, text = "", width=50, height = 20)
        self.label.pack(side = TOP)
        self.fileOpenButton = tkinter.Button(self.root, text = "UPLoadImage", command = self.OpenFile)
        self.fileOpenButton.pack(side = tkinter.constants.LEFT, anchor = SW)
        self.urlLinkInput = tkinter.Entry(self.root)
        self.urlLinkInput.pack(side = tkinter.constants.LEFT, anchor = SW)
        self.sendUrlLinkButton = tkinter.Button(self.root, text = "urlLinkSend", command = self.sendUrlLink)
        self.sendUrlLinkButton.pack(side = tkinter.constants.LEFT, anchor = SW)
        self.urlLinkInput.bind("<Key-Return>", self.sendUrlLink)
        self.root.mainloop()
    def OpenFile(self):
        self.FilePath = filedialog.askopenfilename(filetypes = [("gif files", ".gif")])
        if(self.FilePath == ""): 
            return 
        try: 
            self.image=Image.open(self.FilePath) 
        except: 
            messagebox.showerror("error","failed to open the image") 
        else: 
            self.pixel=self.image.load() 
            self.label.image=ImageTk.PhotoImage(self.image)
            tkinter.Label.__init__(self.label, self.root, image = self.label.image, bd = 0)
            self.label.pack(side = tkinter.constants.TOP)
            RequestHologram.sendGifImage(ip, self.FilePath)

    def urlLinkInput_Return(self, event):
        self.sendUrlLink()
    def urlLinkInputButton_Clicked(self):
        self.sendUrlLink()
    def sendUrlLink(self):
        self.urlLink = str(self.urlLinkInput.get())
        if(self.urlLInk == ""):
            return 
        RequestHologram.sendUrlLink(ip, self.urlLink)


Client = HologramImageUpload()