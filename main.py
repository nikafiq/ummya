import os
import pyocr
from picprocessor import *

#linking OCR program path
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

#creating empty list
fannum =[]
playerlist = []

#read linked images and return it as text
def imgocr(img):
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img, lang="jpn", builder=builder)
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace(' ', '')
    return text

# Extracting fan number from text
def fan_num(text):
    p = re.compile('[0-9]+')
    num = p.findall(text)
    num2 = []
    for i in range(len(num)):
        if len(num[i]) >= 7:
            num2.append(num[i])
    return  num2

# Extracting player list from text
def player_list(text):
    player = text.split("\n")
    playerlist = []
    if len(player) == 7:
        for i in range(0, len(player), 4):
            playerlist.append(player[i])
    elif len(player) == 6:
        for i in range(0, len(player), 3):
            playerlist.append(player[i])
    else:
        for i in range(0, len(player), 5):
            playerlist.append(player[i])
    return playerlist

def list_fan():
    global fannum, playerlist
    for i in glob.iglob("pic/crop/*.png"):
        img = Image.open(i)
        text = imgocr(img)
        num = fan_num(text)
        player = player_list(text)
        for x in num:
            fannum.append(x)
        for x in player:
            playerlist.append(x)
        #print(num)
        #print(player)
        #return player, num

ss_crop()
list_fan()
print(playerlist)
print(fannum)



#with open('text.txt','w') as txt:
#    txt.write(text)

#with open('num.txt','w') as txt:
#    for item in num:
#        txt.write("%s\n" % item)
