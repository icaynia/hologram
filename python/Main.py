
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

class HologramImageUpload:
    def __init__ (self):
        self.root = tkinter.Tk()
        self.root.geometry("500x500")
        self.root.title("ImageUploader")
        self.fileOpenButton = tkinter.Button(self.root, text = "UPLoadImage", command = self.OpenFile)
        self.fileOpenButton.pack()
        self.root.mainloop()
    def OpenFile(self):
        

Client = HologramImageUpload()