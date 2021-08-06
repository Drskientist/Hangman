from tkinter import *
from tkinter import messagebox
from random import choice
from Engine import Settings
from Images import Images
db = True


class Window(Frame):
    def __init__(self, master, geometry=None):
        if geometry is None:
            geometry = (200, 200)
        Frame.__init__(self, master)
        self.master = master
        self.width = geometry[0]
        self.height = geometry[1]
        self.widgetList = []
        self.heightBuffers = {
            'game menu': 100
        }
        root.geometry(f'{self.width}x{self.height}')

    def add(self, widget):
        self.widgetList.append(widget)

    def changeSize(self, xBuffer=None, yBuffer=None, sBuffer=None):
        if xBuffer is None:
            xBuffer = 0
        if yBuffer is None:
            yBuffer = 0
        if sBuffer is not None:
            yBuffer = self.heightBuffers.get(sBuffer)
        root.geometry(f'{self.width+xBuffer}x{self.height+yBuffer}')

    def changeFrame(self, Buffer=None, txt=None):
        for widget in self.widgetList:
            widget.destroy()
        if Buffer is not None:
            self.changeSize(sBuffer=Buffer)
        if txt is not None:
            title.configure(text=txt)

    def message(self, Title, Text):
        messagebox.showinfo(Title, Text)


def changeTries():
    if -1 < settings.tries < 7:
        settings.tries += 1
    else:
        print('Opps, got lost :(')
        print(settings.tries)
    if settings.tries >= 7:
        settings.tries = 0
    gameMenu()


def gameMenu():
    window.changeFrame(txt='Hangman')
    window.changeSize(sBuffer='game menu')

    hangman = Label(root, text=Images[f'hm{settings.tries}'])
    tryBtn = Button(root, text='Try', command=changeTries)

    window.add(hangman)
    window.add(tryBtn)

    hangman.pack(side=TOP, pady=10)
    tryBtn.pack(side=TOP)


def assignWord():
    window.changeFrame(txt='Type Word')

    wordEntry = Entry(root, textvariable=settings.word)
    pBtn = Button(root, text='Play Game', command=gameMenu)

    window.add(wordEntry)
    window.add(pBtn)

    wordEntry.pack(side=TOP)
    pBtn.pack(side=TOP, pady=10)


def chkOriginal():
    if settings.isOriginal.get():
        window.message('Message', 'Please Pass Computer to Executioner\n\nIf you are The Executioner, Press OK to'
                                  ' Continue')
        assignWord()
    else:
        with open('newText.txt', 'r') as file:
            uberString = file.read()
        uberList = uberString.split('\n')
        settings.word.set(choice(uberList))
        gameMenu()


def makeSetts():
    window.changeFrame(txt='Settings')
    window.changeSize(50)

    btn1 = Radiobutton(root, text='Make My Own Word', var=settings.isOriginal, value=True)
    btn2 = Radiobutton(root, text='Assign Random Word', var=settings.isOriginal, value=False)
    saveBtn = Button(root, text='Save', command=chkOriginal)

    window.add(btn1)
    window.add(btn2)
    window.add(saveBtn)

    btn1.pack(side=TOP)
    btn2.pack(side=TOP)
    saveBtn.pack(side=TOP)


def mainMenu():
    window.changeFrame(txt='Hangman')

    plyBtn = Button(root, text='Play', command=makeSetts)
    cls = Button(root, text='Close', command=root.destroy)

    window.add(plyBtn)
    window.add(cls)

    plyBtn.pack(side=TOP, pady=10)
    cls.pack(side=TOP)


if __name__ == '__main__':
    root = Tk()
    window = Window(root, (100, 120))
    settings = Settings()
    root.wm_title('Hangman')

    title = Label(root)
    title.pack(side=TOP, pady=10)

    mainMenu()

    root.mainloop()
