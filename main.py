import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"You said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return ""
def speak(response):
    engine.say(response)
    engine.runAndWait()


while True:
    query = listen().lower()

    if "hello" in query:
        speak("Hello! How can I assist you?")

    elif "goodbye" in query:
        speak("Goodbye! Have a nice day!")
        break

    else:
        speak("Sorry, I don't understand. Can you please repeat?")
