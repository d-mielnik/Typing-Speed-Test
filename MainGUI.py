from tkinter import *
import ParagraphTest
import SentenceTests



def call_SentenceTests():
    SentenceTests.TypeSpeedGUI()
    return


def call_ParagraphTest():
    ParagraphTest.TypeSpeedGUI()
    return


if __name__ == "__main__":
    root = Tk()
    root.title('Typing Speed Application')
    root.minsize(800, 600)
    button_1 = Button(root, text='Sentence Test', font=("Courier New", 14), width='20', height='20', command=call_SentenceTests)
    button_1.pack()
    button_2 = Button(root, text='Paragraph Test', font=("Courier New", 14), width='20', height='20', command=call_ParagraphTest)
    button_2.pack()
    root.mainloop()
