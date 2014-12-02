import urllib2
from HTMLParser import HTMLParser
import os

def convertURL( url ):
    newURL = "http://inspirefwtx.weebly.com/uploads/" + url
    newURL = newURL[0:-4] + "_orig.jpg"
    return newURL

def saveToFile( imgUrl, imgCaption ):
    dayNum = "20" # used to create a new folder for each day of pics, recommended to change
    dirpath = "images/" + dayNum
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    img_file_name = dirpath + "/" + imgUrl.split('/')[-1]
    txt_file_name = img_file_name.split('.')[0] + ".txt"
    u = urllib2.urlopen(imgUrl)
    while True:
        buffer = u.read()
        if not buffer:
            break

        f = open(img_file_name, 'wb')
        f.write(buffer)
        f.close()
    
    f2 = open(txt_file_name, 'wb')
    h = HTMLParser()
    f2.write(h.unescape(imgCaption))
    f2.close
