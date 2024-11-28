import os
from pydub import AudioSegment

#This code converts all WAV files that are in the same directory

def wav_to_mp3(wav_file):
    audio = AudioSegment.from_wav(wav_file)
    mp3_file = os.path.splitext(wav_file)[0] + ".mp3"
    
    audio.export(mp3_file, format="mp3")
    print(f"Conversion completed: {mp3_file}")

directory = os.getcwd()

for filename in os.listdir(directory):
    if filename.endswith(".wav") or filename.endswith("WAV"):
        wav_file = os.path.join(directory, filename)
        wav_to_mp3(wav_file)
