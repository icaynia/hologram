import ftplib
def sendImage(ftpHost, ftpUser, FtpPasswd, ImageName):
    try: 
        ftpName = ftplib.FTP(host = ftpHost, user = ftpUser, passwd= FtpPasswd)
        ftpName.cwd('/')
        ftpName.storbinary("STOR image", open(ImageName,"rb"))
        ftpName.close()
    except FileNotFoundError as err:
        return -1