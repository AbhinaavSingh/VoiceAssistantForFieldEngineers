import dataset
import sys
from gtts import gTTS
from io import BytesIO
import pyglet
from time import sleep
import os
import requests
requests.packages.urllib3.disable_warnings() 

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
argList = sys.argv;
argList.pop(0)
argList = (" ".join(argList)).lower()


db = dataset.connect('sqlite:///D:\ProductInfo.db')

table = db['ProdNameDesc']
#table.insert(dict(ID=2, Name="prod2",DESC="Second Product"))

product1 = table.find_one(Name=str(argList))['DESC']


tts = gTTS(product1, lang='en')
tts.save("D:/Fizz/desc.mp3")
music = pyglet.media.load("D:/Fizz/desc.mp3", streaming=False)
music.play()
sleep(music.duration) #prevent from killing
os.remove("D:/Fizz/desc.mp3") #remove temporary file