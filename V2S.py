"""
speech_text_converter class, converts audio to str and vice versa

uses Google Speech Recognition API to convert speech to text
and Google Text To Speech to convert text to speech
"""

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

class speech_text_converter(sr.Recognizer):
    """
    Converts audio to string and vice versa

    instance attributes:
        recognizer [sr.Recognizer]: recognizer object from speech recognition library
        audio_player [BytesIO]
    """

    def __init__(self):
        """
        Initialises object attribute recognizer
        """
        super().__init__()
        self.dynamic_energy_threshold = True
        self.pause_threshold = 0.5


    def speech_to_text(self):
        """
        Returns the predicted text from GPT

        Listens to user audio input and sends an API request to Google
        Speech Recognition API, and returns the output from the API

        If UnknownValueError, it would print error message and
        continues the program.
        If RequestError, it would print error message and
        exits the program.
        """
        with sr.Microphone() as mic:
            print('listening...')
            audio = self.listen(mic)
        try:
            return self.recognize_google(audio)

        except sr.UnknownValueError:
            print('Not sure what you said back there...')

        except sr.RequestError:
            print('Cannot connect to Google Speech Recognition')
            exit()


    def text_to_speech(self,text):
        """
        Converts the text to audio file and plays it

        Stores the audio tempararily as audio.mp3 in root dir
        If error occurs, prints 'No reply...'

        text [str]: text to be converted to audio and played
        """
        try:
            # cvt text 2 speech
            speaker = gTTS(text=text, lang='en', slow=False)
            # play the audio
            audio_file = os.path.dirname(__file__) + '\\audio.mp3'
            speaker.save(audio_file)
            playsound(audio_file)
            os.remove(audio_file)

        except:
            print('No reply...')



