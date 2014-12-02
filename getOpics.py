from bs4 import BeautifulSoup
import requests
import re
import json
from helper import convertURL, saveToFile

# Set URL to pull images - Must manually change this everytime... boo
url="http://inspirefwtx.weebly.com/blog/our-last-day"

# Set Soup
response = requests.get(url)
soup = BeautifulSoup(response.text)

# Get images list
imgList = soup.find_all(text=re.compile("images:")) # Get image list
imgString = str(imgList) # Cast into a string from bs4.element.ResultSet
startIndex = imgString.index("images:") # find start of images
endIndex = imgString.index("}]})") # find end of images 

# Convert list into JSON and convert to Dictionary
imgData = '{"images"' + imgString[startIndex+6:endIndex+3]
imgDict = json.loads(imgData)

# Loop through and update all URLs
for i in imgDict['images']:
    i['url'] = convertURL(i['url'])

# Save images and captions to disk
for i in imgDict['images']:
    saveToFile(i['url'], i['caption'])
