import os 
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
maze_api="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"

lang='en'
openai.api_key=maze_api

while True:
    def get_audio():
        print("function started")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            said = ""

        
        said= r.recognize_google(audio)
        print(said)
        if "Maze" in said:
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=[{"role":"user","content":"said"}])
                    text = completion.choices[0].message.content
                    speech = gTTS(text=text,lang=lang,slow=False, tld="com.au")
                    speech.save("welcome1.mp3")
                    playsound.playsound("welcome1.mp3")
        return(said)   

    get_audio()