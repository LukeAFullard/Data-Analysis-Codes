# From https://towardsdatascience.com/easy-speech-to-text-with-python-3df0d973b426
# Info https://cloud.google.com/speech-to-text/docs/languages
# https://pypi.org/project/SpeechRecognition/
#import library
import speech_recognition as sr
from pydub import AudioSegment
import json
import tkinter as tk
from tkinter.filedialog import askopenfilename
import math


# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Audio file as source via gui
root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw() #Prevents the Tkinter window to come up
src = askopenfilename()
root.destroy()
print(src)

sound = AudioSegment.from_mp3(src)
sound.export("MyAudio.wav", format="wav")

number_of_iterations = math.ceil(math.ceil(len(AudioSegment.from_file('MyAudio.wav'))/1000)/20)
FullText=[]


for i in range(number_of_iterations):
    print(i)
    with sr.AudioFile('MyAudio.wav') as source:
    

    

        audio_text = r.record(source, offset = i*20, duration = 20)

    
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            text = r.recognize_google(audio_text)
            FullText.append(text)
            #text = r.recognize_google(audio_text, language = "en-NZ")
            print('Converting audio transcripts into text ...')
            print(text)
     
        except:
            print('Sorry.. run again...')
    
print("Writing file...")     
write_file = open(src[0:-4] + '_Audio_Transcribed.txt', "w")
json.dump(FullText, write_file)
write_file.close()