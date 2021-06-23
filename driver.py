from tkinter import Tk

from gui import GUI
import threading


def main():

    root = Tk()
    app = GUI(master=root)
    app.mainloop()

if __name__ == '__main__':
    main()
