# Import necessary modules
#-------------------------
import bson
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize pyttsx3 for speech synthesis
#----------------------------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #1 for female voice, 0 for male voice.

# Function to make the assistant speak
#--------------------------------------
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of day
#----------------------------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Pyyra, your virtual assistant. How can I help you today?")

# Function to listen to the user's command
#-----------------------------------------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pyra Listening...")
        r.pause_threshold = 1  # Wait time before recognizing the speech
        audio = r.listen(source)

    try:
        print("Pyra Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I couldn't catch that. Please repeat.")
        speak("Sorry, I couldn't catch that. Please repeat.")
        return "None"  # Return "None" when there's an issue
    return query

# Function to search on Google
#-----------------------------
def searchBrowser(query):
    search_query = query.replace('search for', '').strip()  # Clean up the query
    speak(f"Searching for {search_query} on browser")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")

# Main function
#--------------
if __name__ == "__main__":
    wishMe()  # Greet the user
    while True:
        query = takeCommand().lower()  # Take command and convert to lowercase
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are many results for this topic. Please be more specific.")
            except Exception as e:
                speak("Sorry, I couldn't retrieve information from Wikipedia.")

        elif 'hello' in query:
            speak("Hello! How can I assist you today?")

        elif 'open notepad' in query:
            speak("Opening Notepad")
            notepad_path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepad_path)
            
        elif 'search for' in query:
            searchBrowser(query)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        
        elif 'play music' in query:
            speak("Playing music")
            music_dir = r"D:\Python Project\song"  # Update the music folder path
            try:
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
            except Exception as e:
                speak("Sorry, I couldn't find music files in the specified directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'the date' in query:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'close the program' in query:
            speak("Closing the program. Goodbye!")
            break