import tkinter as tk
from playsound import playsound

def play_audio():
    playsound("Downloads/Mohammad-Hesam-Avale-Sal-320.mp3")

root = tk.Tk()
root.geometry("500x200")
play_button = tk.Button(root, text="Play Sound", command=play_audio)
play_button.pack()

root.mainloop()
