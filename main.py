# This project is based on a Medium article which I saw and wanted to try for myself.
# https://medium.com/wiki-flood/python-project-convert-speech-to-text-and-text-to-speech-8065972e5e58

from gtts import gTTS
import speech_recognition as sr

def text_to_speech():
    text = input("Enter the text: ")
    tts = gTTS(text)
    tts.save("output.mp3")

    print("Please find the output in output.mo3 file")


def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Error: {e}")


while True:
    print("Select an option:")
    print("1. text to speech")
    print("2. speech to text")
    print("3. Exit")
    
    choice = input("choice (1/2/3): ")

    if choice == '1':
        text_to_speech()
    elif choice == '2':
        speech_to_text()
    elif choice == '3':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select a valid option.")