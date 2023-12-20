import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
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
    speak('hello sir. i am zary, how mey i help you')

    # if hour > 1 and hour <= 7:
    #     speak("During Qur'an recitation time")

    # elif hour >= 7.30 and hour <= 8:
    #     speak("its almost office start.")

    # elif hour >12.30 and hour <= 3.30:
    #     speak("Zohor namaj time")

    # elif hour >= 4 and hour <= 5:
    #     speak("Zohor namaj time")

    # else:
    #     speak("its sleping time")




# take command from microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizig...")
        query = r.recognize_google(audio, language="en-US")
        print(f"You said: {query}\n ")
    except Exception as e:
        print("Sorry i did not get you 😔 😔...")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
            speak("anything else sir")

            if "yes" in query:
                webbrowser.open("https://www.youtube.com/results?search_query=",query)

        elif "wikipedia" in query:
            speak("searching from wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia..")
            print("Result")
            speak(results)

        elif "play audio" in query:
            audio_file = "D:\\Favorite\\Gajal"
            audio = os.listdir(audio_file)
            print(audio)
            os.startfile(os.path.join(audio_file,audio [0]))

        elif "stop the program" in query or "close the program" in query:
            speak("thank you sir.")
            break

        else:
            pass