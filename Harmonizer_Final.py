import tkinter as tk

from tkinter import ttk

from pydub import AudioSegment

import pyrubberband as pyrb

import soundfile as sf

import numpy as np

from collections import defaultdict

 

interval_ratios = defaultdict(float)

 

interval_ratios["minor second"] = 16/15

interval_ratios["major second"] = 9/8

interval_ratios["minor third"] = 6/5

interval_ratios["major third"] = 5/4

interval_ratios["perfect fourth"] = 4/3

interval_ratios["augmented fourth"] = 7/5

interval_ratios["perfect fifth"] = 3/2

interval_ratios["minor sixth"] = 8/5

interval_ratios["major sixth"] = 5/3

interval_ratios["minor seventh"] = 9/5

interval_ratios["major seventh"] = 15/8

interval_ratios["octave"] = 2

 

def harmonize_audio():

    interval = interval_var.get()

    if interval not in interval_ratios:

        print("Invalid interval")

        return

    audio = AudioSegment.from_file("input.wav", format="wav")

    audio_arr = np.array(audio.get_array_of_samples(), dtype=np.float32)

    ratio = interval_ratios[interval]

    harmonized_audio = pyrb.time_stretch(audio_arr, audio.frame_rate, ratio)

    sf.write("harmonized.wav", harmonized_audio, audio.frame_rate)

 

root = tk.Tk()

root.title("Audio Harmonizer")

 

interval_var = tk.StringVar()

interval_options = list(interval_ratios.keys())

 

interval_menu = ttk.Combobox(root, textvariable=interval_var)

interval_menu['values'] = interval_options

interval_menu.current(0)

interval_menu.pack()

 

harmonize_button = tk.Button(root, text="Harmonize Audio", command=harmonize_audio)

harmonize_button.pack()

 

root.mainloop()
