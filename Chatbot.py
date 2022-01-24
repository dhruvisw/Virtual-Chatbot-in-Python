import pyttsx3      #text to speech module
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as wt
import spotipy
import os
import smtplib


engine = pyttsx3.init('sapi5')      #Speech Application Programming Interface (allow the use of speech recognition and speech synthesis within Windows applications)
voices = engine.getProperty('voices')
#print(voices[1].id)           #when u run, computer shows that it has 2 voices (1M [0] - David, 1F [1] - Zira)
engine.setProperty('voice', voices[1].id)       #sets voice of your engine

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis! Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1        #pause_threshold gives time to speak (1sec)
        r.energy_threshold = 300        #minimum audio energy to consider for recording
        audio = r.listen(source)

    try:
        print("Recognizing....")            #recogninzing the audio typed
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

#def sendEmail(to, content):
    #server = smtplib.SMTP("smtp.gmail.com", 587)
    #server.ehlo()
    #server.starttls()
    #server.login('---@gmail.com', 'i@3o:')
    #server.sendmail('---@gmail.com', to, content)
    #server.close()


if __name__ == "__main__":
    #speak("Aishani")
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks  based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia, ")
            speak(result)

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open youtube and play" in query:
            wt.playonyt(query)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "text" in query:
            if 'dad' in query:
                numb = '+91----------34'
                speak("Whats the message for dad")
                mess = takeCommand()
                print(takeCommand())
                hour = datetime.datetime.now().hour
                min = datetime.datetime.now().min
                wt.sendwhatmsg(phone_no=numb, message=mess, time_hour= int(hour), time_min=int(min))

            if 'mom' in query:
                numb = '+91-----------21'
                speak("Whats the message for mom")
                mess = takeCommand()
                print(takeCommand())
                hour = datetime.datetime.now().hour
                min = datetime.datetime.now().min
                wt.sendwhatmsg(phone_no=numb, message=mess, time_hour= int(hour), time_min=int(min))


        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")          #time in string
            speak(f"The time is {strTime}")

        elif "Open dev c plus plus" in query:
            path = "C:\Program Files (x86)\Dev-Cpp\devcpp.exe"
            os.startfile(path)

        elif "create a list" in query:
            l1 = []
            speak("What should I add to the list? ")
            a = takeCommand()
            l1.append(a)
            speak("Done")
        elif "read my list" in query:
            speak(l1)


        #elif "send email" in query:
         #   try:
          #      speak("What should i send? ")
           #     content = takeCommand()
            #    to = 'nanavkar@gmail.com'
             #   sendEmail(to, content)
              #  speak("Email has been sent. ")
           # except Exception as e:
            #    print(e)
             #   speak("Sorry I couldnt send the email")

        elif "stop" in query:
            break
#open youtube and play a song
#open google
#open dev c
#what is the time
#send whatsapp msg
#mail
#wikipedia
#creates a list and reads it


    # music
    # reminder
    #send email