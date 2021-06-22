# import tkinter as tk
from enum import Enum
from tkinter import BOTH, Frame, Canvas, Button, Tk, Label, TOP, RIGHT, LEFT
from brute_force_sort import BruteForceSort
from sort import Sort


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.sort = BruteForceSort
        # self.sort_methods = {
        #     "Brute Force": Sorting.BRUTE_FORCE
        # }
        self.graph_origin_x = 550
        self.graph_origin_y = 950
        self.bar_width = 10
        self.frame_main = None
        self.frame_options = None
        self.title = None
        self.canvas = None

    def create_widgets(self):
        self.frame_main = Frame(self.master, bg='black')
        self.frame_main.pack(expand=True, fill=BOTH)

        self.title = Label(self.frame_main, text='Sorting Visualizer', bg="black", fg="white")
        self.title.config(font=("Times", 44))
        self.title.pack(side=TOP, pady=20)

        # Options Start
        self.frame_options = Frame(self.frame_main, bg='red', width=1000, height=100)
        self.frame_options.pack()

        self.sort_brute_force = Button(self.frame_options, text="Brute Force", fg="red",
                              command=lambda: self.set_sort(BruteForceSort))
        self.sort_brute_force.pack(side=LEFT)
        self.sort_brute_force1 = Button(self.frame_options, text="QUIT2", fg="red",
                              command=lambda: self.set_sort(BruteForceSort))
        self.sort_brute_force1.pack(side=LEFT)
        self.sort_brute_force1 = Button(self.frame_options, text="QUIT3", fg="red",
                              command=lambda: self.set_sort(BruteForceSort))
        self.sort_brute_force1.pack(side=LEFT)
        # Options End

        self.canvas = Canvas(self.frame_main, bg='black', width=1000, height=600)
        self.canvas.pack()

        self.build_visualizer()

    def set_sort(self, sort):
        self.sort = sort

    def build_visualizer(self):
        # element_bar = self.canvas.create_rectangle(1, 1, 50, 50)
        # element_bar.pack()
        self.canvas.create_rectangle(50 + 10, 550 - 10, 50 + 10 + self.bar_width, 100, fill='blue')
        # self.canvas.create_rectangle(550 - 10, 950, 550, 950 + 100, fill='blue')


class Sorting(Enum):
    DEFAULT = -1
    BRUTE_FORCE = 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
