from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window=Tk()
        self.window.title("Quizzler")
        # self.window.geometry("500×500")
        self.window.config(fg=THEME_COLOR)


        self.window.mainloop()

