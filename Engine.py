from tkinter import *


class Settings:
    def __init__(self):
        self.isOriginal = BooleanVar()
        self.word = StringVar()
        self.tries = 0
        self.displayWord = []
        self.wordMap = []
        self.guesses = []