from tkinter import *


class Settings:
    def __init__(self):
        self.isOriginal = BooleanVar()
        self.word = StringVar()
        self.dbtries = IntVar()
        self.dbtries.set(0)
        self.tries = 0
        self.displayWord = []
        self.wordMap = []
        self.guesses = []
