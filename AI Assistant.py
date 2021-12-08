import datetime
import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)


def speak(sound):
    engine.say(sound)
    engine.runAndWait()


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        speak('Good Morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak('I am your AI Assistant. How can I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing ....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing ....')
        command = r.recognize_google(audio)
        print(f"user told:{command}\n")

    except Exception:
        print('say that again please...')
        return 'None'
    return command


greetMe()

while True:
    command = takeCommand().lower()
    # Logic for executing tasks based on the query
    if 'information' and 'about' in command:
        speak('Searching in wikipedia...')
        command = command.replace('wikipedia', '')
        result = wikipedia.summary(command, sentences=2)
        print(result)
        speak(result)

    elif 'open youtube' in command:
        webbrowser.open('youtube.com')
    elif 'open google' in command:
        webbrowser.open('google.com')
    elif 'open stackoverflow' in command:
        webbrowser.open('stackoverflow.com')

    elif 'play music' in command:
        music_dir = r'C:\Users\Xalem\Downloads\Music'
        music = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, music[0]))

    elif 'time' in command:
        Time = datetime.datetime.now().strftime('%I:%M %p')
        print(Time)
        speak(f'The time is {Time}')

    elif 'open terminal' in command:
        path = r'C:\Users\Xalem\AppData\Local\Microsoft\WindowsApps\wt.exe'
        os.startfile(path)

    elif 'can you hear me' in command:
        speak('Definitely, I can hear you , you are loud and clear')

    elif 'hold on' in command:
        speak('Alright, your wish is my command')
