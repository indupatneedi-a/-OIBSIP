import datetime
import webbrowser
from urllib.parse import quote_plus

import pyttsx3
import speech_recognition as sr

# Setup: text-to-speech engine and speech recognizer
engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    """Print the text and say it out loud."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen through the microphone and return what was said as lowercase text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
        except sr.WaitTimeoutError:
            return ""

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please repeat.")
    except sr.RequestError:
        speak("Sorry, I cannot reach the speech service. Check your internet connection.")
    return ""


def handle_command(command):
    """Respond to the command. Returns False when the assistant should stop."""
    if any(word in command for word in ["hello", "hi", "hey"]):
        speak("Hello! How can I help you today?")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "date" in command or "today" in command:
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    elif "search" in command:
        query = command.replace("search for", "").replace("search", "").strip()
        if query:
            speak(f"Searching the web for {query}")
            webbrowser.open("https://www.google.com/search?q=" + quote_plus(query))
        else:
            speak("What would you like me to search for?")

    elif any(word in command for word in ["exit", "stop", "bye", "quit"]):
        speak("Goodbye! Have a great day.")
        return False

    elif command:
        speak("Sorry, I can only greet you, tell the time, tell the date, or search the web.")

    return True


def main():
    speak("Hi, I am your voice assistant. You can say hello, ask the time or date, or say search followed by a topic.")
    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)


if __name__ == "__main__":
    main()
