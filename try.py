import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import keyboard




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak('assalamu alaykum')
    speak('hello sir. i am mary, how mey i help you')
# take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizig...")
        query = r.recognize_google(audio, language= "en-US")
        print(f"You said: {query}\n ")
    except Exception as e:
        print("Sorry i did not get you 😔 😔...")
        return "none"
    return query
if __name__ == "__main__":
    wishMe()
    # while True:
    query = takeCommand().lower()
    if "youtube" in query:
        speak("opening youtube")
        # webbrowser.open("youtube.com")
        speak("anything else sir")

        for i in query:
            if i == query:
                speak("ok sir")
                webbrowser.open("youtube.com")
            elif "yes search" in query:
                speak("what should i search for?")
                search = len(query[-1])
                webbrowser.open("https://www.youtube.com/results?search_query=",search)





            # if query == "youtube.com":




    elif "stop the program" or "close the program" in query:
        speak("thank you sir.")


    else:
        pass