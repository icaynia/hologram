try:
    import requests
except ImportError as err:
    messagebox.showerror("모듈 없음", "requests 모듈을 설치해주세요")

def sendGifImage(url = "", filePath = ""):
    if(url == "" or filePath == ""):
        return -1
    image = {'image' :('image.gif', open(filePath, 'rb'), 'image/gif', {'Exprice': 0})}

    r = requests.post(url,files = image)

def sendUrlLink(url = "", urlLink = ""):
    if(url == "" or filePath == ""):
        return -1
    youtubeUrl = {'url': urlLink}
    r =requests.post(url, youtubeUrl)