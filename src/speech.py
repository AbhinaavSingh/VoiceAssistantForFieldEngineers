import speech_recognition as sr
from gtts import gTTS
from io import BytesIO
import pyglet
from time import sleep
import os
import requests
requests.packages.urllib3.disable_warnings() 
#export PYTHONWARNINGS="ignore:Unverified HTTPS request"



r = sr.Recognizer()
m = sr.Microphone()


def returnSpeech():
    repeat=True
    value = "bye"
    while repeat==True:
        repeat = False
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognizing speec
            value = r.recognize_google(audio)

            if str is bytes:  
                print(u"You said {}".format(value).encode("utf-8"))
            else:  
                print("You said {}".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
            repeat = False
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    return value

def say(stuff):
    tts = gTTS(stuff, lang='en')
    tts.save("D:/Fizz/test1.mp3")
    music = pyglet.media.load("D:/Fizz/test1.mp3", streaming=False)
    music.play()
    sleep(music.duration) #prevent from killing
    os.remove("D:/Fizz/test1.mp3") #remove temporary file

try:
    ttsGreet = gTTS("Hello Abhinaav..... and, how may I help you today?", lang='en')
    ttsGreet.save("D:/Fizz/greeting.mp3")
    music = pyglet.media.load("D:/Fizz/greeting.mp3", streaming=False)
    music.play()
    sleep(music.duration) 
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    repeat=True
    while repeat==True:
        if "product" in returnSpeech():
            say("Which product would you like to know about")
            repeat=False;
        else:
            say("It is not a service I provide at this moment. I feel like crying now.")
    productName = returnSpeech();    
    repeat=True
    while repeat==True:
        say("Okay. what information would you like about "+productName+". Step by step guide, Basic description, or, active issues related to this device")
        command = returnSpeech();
        if "description" in command:
            os.system("py prodDescByName.py "+productName)
        elif "issues" in command:
            os.system("py prodIssues.py "+productName)
        elif "guide" in command:
            say("There is no guide present at the moment. Kindly wait till after this presentation .. hahahaha")
        say("Is there anything else you would like to know about" + productName)
        if "nothing" in returnSpeech():
            repeat=False;
            say("Thank you, my dear Field Engineer. Tata.")			
			
except KeyboardInterrupt:
    pass
