import os
import speech_recognition as sr
import playsound
from gtts import gTTS


def speak_to_me(text):
    tts = gTTS(text=text, lang='en') 
    filename = 'f_voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


def get_audio_from_me():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


speak_to_me('Hello I`m the voice in your head')
my_text = get_audio_from_me()

if "hello" in my_text:
    speak_to_me("hello how are you")
else:
    speak_to_me("I don`t understand try again please")
