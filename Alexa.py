from datetime import date
import speech_recognition as sr     # used for recognizing our speech
import pyttsx3      # used for alexa to talk to you
import pywhatkit        # used for searching the web browser for our internet-based commands
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()      # listen and recognize our voice through recognizer

engine = pyttsx3.init()
voices = engine.getProperty('voices')       # calling all the voices from python speech to text
engine.setProperty('voice' , voices[1].id)      # calling the female voice with id 1

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:     # using microphone as a source of our command
            print("Speak now!!")
            voice = listener.listen(source)     # calling sr to listen to this source
            command = listener.recognize_google(voice)      # passing the audio to google and google converts the speech to text
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa' , '')
                print(command)

    except:
        pass
    return command


def run_alexa():        # for alexa to take command from user
    command = take_command()
    print(command)
    if 'play' in command:       # function plays song
        song = command.replace('play' , '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)        # playonyt : play on youtube
    
    elif 'time' in command:     # function tells time
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)

    elif 'tell me about' in command:        # function tells information
        person = command.replace('tell me about' , '')
        info = wikipedia.summary(person , 1)
        print(info)
        talk(info)
    
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)

    else:
        print("Can you repeat again?!")

while True:
    run_alexa()