import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice" , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")     

    speak("hello i am sahil how may i help you")  

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please......")
        return "None"
    
    return query 

if __name__== "__main__":
    greetings()
    while True:
        query = takecommand().lower()
        
        if ("wikipedia" in query):
            speak("searchimg wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wekipedia")
            print(results)
            speak(results)

    
        elif ('open youtube' in query):
            webbrowser.open("youtube.com")


        elif ('open google' in query):
            webbrowser.open("google.com")
      

        elif ('open stackoverflow' in query):
            webbrowser.open("stackoverflow.com")

        elif ('the time' in query):
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir, the time is {strTime}")
 
        elif ('play' in query) and (('song' in query) or ('music' in query)):
            music_dir = 'E:\\song'
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[0]))
                
        elif (('start' in query) or ('launch' in query)) and ('vs code' in query):
            os.system('code')

        elif (('stop' in query) or ('close' in query)):
            pyttsx3.speak("have a good day sir")
            break    