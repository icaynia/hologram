import threading
try:
    import requests
except ImportError as err:
    messagebox.showerror("모듈 없음", "requests 모듈을 설치해주세요")

class SendGIFImage(threading.Thread):                          #sending gif image to server via thread
    def __init__(self, threadID, name, counter, url, filePath):
        threading.Thread.__init__(self)
        self.threadID = threadID 
        self.name = naem
        self.counter = counter
        self.url = url
        self.filePath = filePath
    def run(self):
        image = {'image' : ('image.gif', open(self.filePath, 'rb'), 'image/gif',{'Exprice : 0'})}
        r = requests.post(self.url, files = image)

class SendURLLink(threading.Thread):                          #sending youtube link to server via thread
    def __init__(self, threadID, name, counter, url, urlLink):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url
        self.urlLink = urlLink
    def run(self):
        youtubeUrl = {'url':self.urlLink}
        r = requests.post(self.url, youtubeUrl)

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