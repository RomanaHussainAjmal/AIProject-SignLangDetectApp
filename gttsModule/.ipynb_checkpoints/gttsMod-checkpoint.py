from gtts import gTTS
import os
from playsound import playsound
from gtts import gTTS
from IPython.display import Audio
from IPython.display import display
from flask import Flask,render_template,Response, send_file

def textToSpeech(text):
    
    # Language in which the speech should be generated
    language = "en"

    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(os.path.join(os.getcwd(),'media','PredictedTxtAudio.mp3'))