import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import os

def pop_up_message(message):
    window = tk.Tk()
    msg = tk.Label(window,text= message)
    msg.pack()
def wav_to_mp3(wav_file):
    # Load the wav file
    audio = AudioSegment.from_wav(wav_file)

    # Output filename for mp3 file
    mp3_file = os.path.splitext(wav_file)[0] + ".mp3"

    # Export as mp3
    audio.export(mp3_file, format="mp3")
    pop_up_message(f"Conversion completed: {mp3_file}")


def file_choose():
    file_path = filedialog.askopenfilename()
    if (file_path):
        wav_to_mp3(file_path)


root = tk.Tk()
root.title("Waw to mp3 Converter")

file_label = tk.Label(root, text="choose your wav file")
file_label.pack()
file_choice_button = tk.Button(root, text = "Open", command=file_choose)
file_choice_button.pack()



root.mainloop()