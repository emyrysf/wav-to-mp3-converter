import os
from pydub import AudioSegment

# Function to convert wav to mp3
def wav_to_mp3(wav_file):
    # Load the wav file
    audio = AudioSegment.from_wav(wav_file)
    
    # Output filename for mp3 file
    mp3_file = os.path.splitext(wav_file)[0] + ".mp3"
    
    # Export as mp3
    audio.export(mp3_file, format="mp3")
    print(f"Conversion completed: {mp3_file}")

# Directory where the script is located
directory = os.getcwd()

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".wav") or filename.endswith("WAV"):
        wav_file = os.path.join(directory, filename)
        # Convert wav to mp3
        wav_to_mp3(wav_file)