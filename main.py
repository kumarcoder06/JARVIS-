import speech_recognition as sr
import webbrowser
import pyttsx3               #to speak jarvise
import musicLibrary  
import datetime
from gtts import gTTS
import os
from playsound import playsound

def speak_hinglish(text):
    tts = gTTS(text=text, lang='hi', slow=False)  # 'hi' = Hindi
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")


recognizer = sr.Recognizer()     # recognizer to recognize what we will speak
engine = pyttsx3.init()
def speak_hinglish(text):
    engine.say(text)
    engine.runAndWait()

 
def processCommand(c):
    if "open google" in c.lower():
        speak_hinglish("Sir....google open kar rahaa huu......")
        webbrowser.open("https://google.com")

    elif "open youtube" in c.lower():
       speak_hinglish("Sir....youtube open kar rahaa huu......")
       webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c.lower():
        speak_hinglish("Sir....Facebook open kar rahaa huu......")
        webbrowser.open("https://facebook.com")

    elif "open flipkart" in c.lower():
        speak_hinglish("Sir... Flipkart open kar rahaa huu...")
        webbrowser.open("https://www.flipkart.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        speak_hinglish("Sir... music play kar rahaa huu...")
        link = musicLibrary.music[song]
        if link:
            webbrowser.open(link)
        else:
            speak_hinglish("Sorry sir, ye song library mein nahi mila.")
    
    elif "tell me time" in c.lower():
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        speak_hinglish(f"The time is {time_now}")

    elif "search" in c.lower():
        while True:
            speak_hinglish("Sir...kya search karnaa hai")
            with sr.Microphone() as source:

                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                    query = recognizer.recognize_google(audio)
                    url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(url)
                    speak_hinglish(f"Searching for {query} on Google.")
                except sr.WaitTimeoutError:
                    speak_hinglish("Aapne kuch search nhi kiyaa hai")
                    # break
                except Exception as e:
                    speak_hinglish("Sorry sir, samajh nahi paaya.")
                    print(f"Error: {e}")

            speak_hinglish("Sir....Kuch or search krnaaa hai")
            with sr.Microphone() as source:
                try:
                    audio = recognizer.listen(source,timeout=5, phrase_time_limit=6)
                    response = recognizer.recognize_google(audio)
                    if "no" in response:
                        speak_hinglish("Theek hai sir, search mode band kar raha hoon.")
                        break
                    elif "yes" in response:
                        continue
                    else:
                        speak_hinglish("Main samajh nahi paaya sir, isliye search band kar raha hoon.")
                        break
                except:
                    speak_hinglish("Kuch response nahi mila sir, search mode band kar raha hoon.")
                    break

if __name__== "__main__":
    speak_hinglish("Hello sir..... , I am jarvis ")

    while True:
        r = sr.Recognizer()
        print("recognizing")
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source) 

            command = r.recognize_google(audio)

            if(command.lower() == "jarvis"):
                speak_hinglish(" yes sir...")

                # Listen for command

                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source) 
            command = r.recognize_google(audio)
            processCommand(command)

        except Exception as e:
            print("error;{0}".format(e)) 


      