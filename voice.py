import pyttsx3
import subprocess

engine=pyttsx3.init()
engine.setProperty(
    'voice',
    'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\
    TTS_MS_RU-RU_IRINA_11.0'
    ) 
      
'''
DOCSTRING: With cross-platform program"ffmpeg",
    command "subprocess.run([ffmpeg ...])" this function
    convertsthe mp3 file format to ogg, for correct transmission
    to TelegramBot.
INPUT:mp3_file(mp3).
OUTPUT:out_file(ogg).
''' 
  
def text_to_file(text):    
    mp3_file=f"data/temp.mp3"
    out_file=f"data/temp.ogg"
    engine.save_to_file(text,mp3_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg",'-i',mp3_file ,'-acodec','libopus',out_file ,'-y'])
    return out_file
      