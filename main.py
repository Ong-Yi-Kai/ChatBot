"""
Script to run chatbot

choice of model varies from Large, Medium and Small
Model's weights stored in dir 'model'
"""

from chatbot import chatBot
from V2S import speech_text_converter
import keyboard

MODEL_DIR = 'model/large'

mybot = chatBot(MODEL_DIR)
tts_cvt = speech_text_converter()


if __name__ == '__main__':
    response_count = 0
    while response_count < 10:
        print('-'*50)
        # retrieve user input
        user_input = tts_cvt.speech_to_text()
        print(f'User>> {user_input}')

        # generate response
        output = mybot.generate_response(user_input)
        print(f'Chatbot >>{output}')

        # cvt to speech
        tts_cvt.text_to_speech(output)

        # exit
        if keyboard.is_pressed('esc'):
            print('Terminating...')
            break

        response_count += 1
