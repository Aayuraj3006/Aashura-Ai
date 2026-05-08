import pyttsx3
import speech_recognition as sr
import eel

# Initialize engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 190)


def speak(text):
    engine.say(text)
    engine.runAndWait()


@eel.expose
def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        eel.DisplayMessage("Listening...")()

        r.pause_threshold = 0.8

        r.energy_threshold = 300

        r.adjust_for_ambient_noise(source, duration=0.5)

        audio = r.listen(
            source,
            timeout=None,
            phrase_time_limit=15
        )

    try:

        print("Recognizing...")

        eel.DisplayMessage("Recognizing...")()

        query = r.recognize_google(
            audio,
            language='en-in'
        )

        print(f"User said: {query}")

        eel.DisplayMessage(f"{query}")()

        speak(query)

        eel.ShowHood()()

        return query.lower()

    except Exception as e:

        print(e)

        eel.DisplayMessage("Say that again please...")()

        return ""