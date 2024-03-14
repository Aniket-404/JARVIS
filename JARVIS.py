import pyttsx3 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import speech_recognition as sr
from os import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am JARVIS Sir. How may I help you")   

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:  
        print("Say that again please...",e)
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kamble.aniket.ak47@gmail.com', 'aniket2633')
    server.sendmail('deepak.kamble09@ymail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif 'who are you' in query:
            speak("sir i am JARVIS an Artificial Inteligence designed by Robert Downey JR.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"Sir, the time is {strTime}")

        elif 'quit' in query or 'bye' in query:
            speak("Quitting sir. Have a nice day")
            sys.exit(0)
        
        elif 'open youtube' in query:
            speak("opening youtube,sir")
            webbrowser.open("youtube.com")

        elif 'open instagram' in query:
            speak("opening youtube,sir")
            webbrowser.open("instagram.com")     
            
        elif 'open google' in query:
            speak("opening google sir")
            webbrowser.open("google.com")

        elif 'open yahoo' in query:
            webbrowser.open("yahoo.com")
    
        elif 'open whatsapp' in query:
            speak("opening whatsapp,sir")
            whatsappPath = "C:\\Users\\kambl\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath)
            
        elif 'open sonic' in query:
            dolbyPath = "C:\\Users\\kambl\\Desktop\\Sonic Studio 3"
            os.startfile(dolbyPath)

        elif 'show my photos' in query:
            speak("here are your photos,sir")
            photosPath = "C:\\Users\\kambl\\Pictures\\Aniket"
            os.startfile(photosPath)
            
        elif 'show all photos' in query:
            speak("showing all photos,sir")
            allphotosPath = "C:\\Users\\kambl\\Pictures"
            os.startfile(allphotosPath)
            
        elif 'play movies' in query:
            speak("here are your movies. Enjoy sir")
            moviesPath = "F:\\Movies"
            os.startfile(moviesPath)
            
        elif 'show my videos' in query:
            speak("here are your videos,sir")
            myvideosPath = "C:\\Users\\kambl\\Pictures\\Aniket\\Videos"
            os.startfile(myvideosPath)
            
        elif 'show all videos' in query:
            speak("showing all videos,sir")
            videosPath = "C:\\Users\\kambl\\Videos"
            os.startfile(videosPath)
            
        elif 'open chrome' in query:
            speak("opening chrome,sir")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
            
        elif 'play music' in query:
            speak("enjoy your music,sir")
            music_dir = "C:\\Users\\kambl\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif 'play songs' in query:
            speak("playing your favorite songs sir")
            spotifyPath = "C:\\Users\\kambl\\AppData\\Roaming\\Spotify\\Spotify.exe" 
            os.startfile(spotifyPath)
            
        elif 'open excel' in query:
            speak("opening excel sir")
            excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
            os.startfile(excelPath)

        elif 'open word' in query:
            speak("opening word sir")
            wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(wordPath)

        elif 'open powerpoint' in query:
            speak("opeing powerpoint sir")
            powerpointPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint"
            os.startfile(powerpointPath)
        
        elif 'open premiere pro' in query:
            speak("opeing premiere pro sir")
            premierePath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2020\\Adobe Premiere Pro.exe"
            os.startfile(premierePath)

        elif 'open after effects' in query:
            speak("opening after effects sir")
            aePath = "C:\\Program Files\\Adobe\\Adobe After Effects 2020\\Support Files\\AfterFX.exe"
            os.startfile(aePath)

        elif 'open media encoder' in query:
            speak("opening media encoder sir")
            mePath = "C:\\Program Files\\Adobe\\Adobe Premiere Pro 2021\\Adobe Premiere Pro.exe"
            os.startfile(mePath)

        elif 'open discord' in query:
            speak("opening discord sir")
            discordPath = "C:\\Users\\kambl\\AppData\\Local\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(discordPath)

        elif 'open blender' in query:
            speak("opening blender sir")
            blenderPath = "C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
            os.startfile(blenderPath)

        elif 'open photoshop' in query:
            speak("opening photoshop sir")
            photoshopPath = "C:\\Program Files\Adobe\\Adobe Photoshop 2021\\Photoshop.exe"
            os.startfile(photoshopPath)

        elif 'open illustrator' in query:
            speak("opening illustrator sir")
            illustratorPath = "C:\\Program Files\\Adobe\\Adobe Illustrator 2021\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(illustratorPath)

        elif 'play NFS' in query:
            speak("need for speed is ready to play sir")
            nfsPath = "D:\\R.G. Catalyst\\Need for Speed - Most Wanted\\NFS13.exe"
            os.startfile(nfsPath)     
            