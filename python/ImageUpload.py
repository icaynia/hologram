import ftplib
def sendImage(ImageName):
    print(ImageName)
    ftpName = ftplib.FTP(host = "hologram.icaynia.com", user = "ww_ghaha12", passwd= "tktk8899")
    ftpName.cwd('/')
    ftpName.storbinary("STOR asldkfj.jpg", open(ImageName,"rb"))