import speech_recognition as sr
import webbrowser
import pyttsx3               #to speak jarvise
import musicLibrary   

recognizer = sr.Recognizer()     # recognizer to recognize what we will speak
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

 
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open youtube" in command.lower():
       print("Opening YouTube...")
       webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open flipkart" in c.lower():
        print("Opening Flipkart...")
        webbrowser.open("https://www.flipkart.com")
    
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)




if __name__== "__main__":
    speak("Initializing jarvis ")
    while True:
        r=sr.Recognizer()


        print("recognizing")
        try:
            with sr.Microphone() as source:
              print(" Listening...")
              audio = r.listen(source) 

            command = r.recognize_google(audio)

            if(command.lower() == "jarvis"):
                speak("yes sir")

                # Listen for command

                with sr.Microphone() as source:
                    print(" Listening...") 
                    audio = r.listen(source) 
            command = r.recognize_google(audio)

            processCommand(command)

        except Exception as e:
            print("error;{0}".format(e))
      