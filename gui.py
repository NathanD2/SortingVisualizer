import random
import threading
import time
from tkinter import BOTH, Frame, Canvas, Button, ttk, Label, TOP, LEFT
from brute_force_sort import BruteForceSort
from selection_sort import SelectionSort
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort


class GUI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.sorting_algorithm = BruteForceSort()
        self.graph_max_y = 600
        self.graph_max_x = 1000
        self.lower_value_range = 1
        self.upper_value_range = 100

        self.sort_methods = ["Brute Force", "Selection Sort", "Bubble Sort", "Insertion Sort"]
        self.delay = 0.005  # Seconds
        self.num_of_values = 50
        self.stop_sort = False

        self.bar_width = None
        self.frame_main = None
        self.frame_options = None
        self.sort_combo_box = None
        self.title = None
        self.canvas = None
        self.sort_button = None
        self.randomize_data_button = None
        self.data_set = []
        self.highlighted_bars = []
        self.data_set_copy = None
        self.stop_sort_button = None

        self.create_widgets()

    def create_widgets(self):
        self.frame_main = Frame(self.master, bg='black')
        self.frame_main.pack(expand=True, fill=BOTH)

        self.title = Label(self.frame_main, text='Sorting Visualizer', bg="black", fg="white")
        self.title.config(font=("Times", 44))
        self.title.pack(side=TOP, pady=20)

        # Options Start
        self.frame_options = Frame(self.frame_main, bg='black', width=1000, height=100)
        self.frame_options.pack()

        self.sort_combo_box = ttk.Combobox(self.frame_options, values=self.sort_methods, width=25)
        self.sort_combo_box.set("Brute Force")
        self.sort_combo_box.pack(side=LEFT)
        self.sort_button = Button(self.frame_options, text="Sort", fg="black",
                                  command=lambda: self.sort(), padx=5)
        self.sort_button.pack(side=LEFT)
        self.randomize_data_button = Button(self.frame_options, text="Randomize Data", fg="black",
                                            command=lambda: self.randomize_data(), padx=5)
        self.randomize_data_button.pack(side=LEFT)
        self.stop_sort_button = Button(self.frame_options, text="Stop Sort", fg="red",
                                command=self.stop_sorting)
        self.stop_sort_button.pack(side=LEFT)

        # Options End

        self.canvas = Canvas(self.frame_main, bg='black', width=1000, height=600)
        self.canvas.pack()

        self.generate_data_set()
        self.build_visualizer()

    def sort(self):
        print("Sort")
        if self.stop_sort:
            self.stop_sorting()
            self.stop_sort = False
        if self.sort_combo_box.get() in self.sort_methods:
            self.set_sorting_algorithm()
            threading.Thread(target=self.sort_helper).start()


    def sort_helper(self):
        for iteration in self.sorting_algorithm.sort(self.data_set):
            if self.stop_sort:
                print("stopping after randomie?")
                self.stop_sort = False
                break
            if isinstance(iteration, tuple):
                self.build_visualizer(iteration)
            else:
                time.sleep(self.delay)
                self.data_set = iteration
                self.build_visualizer()
            time.sleep(self.delay)

        self.data_set_copy = None
        self.build_visualizer()
        self.stop_sort = False

    def set_sorting_algorithm(self):
        if self.sort_combo_box.get() == "Brute Force":
            self.sorting_algorithm = BruteForceSort()
        elif self.sort_combo_box.get() == "Selection Sort":
            self.sorting_algorithm = SelectionSort()
        elif self.sort_combo_box.get() == "Bubble Sort":
            self.sorting_algorithm = BubbleSort()
        elif self.sort_combo_box.get() == "Insertion Sort":
            self.sorting_algorithm = InsertionSort()
        else:
            self.sorting_algorithm = BruteForceSort()

    def build_visualizer(self, index_focus: tuple = None):
        self.bar_width = self.calculate_bar_width()

        if self.data_set_copy is None:
            # Render whole plot
            index = 0
            for element in self.data_set:
                self.canvas.create_rectangle(index * self.bar_width, self.graph_max_y - (element * 6),
                                             (index * self.bar_width) + self.bar_width, self.graph_max_y, fill='white',
                                             tags=f"rect{index}")
                index += 1
            self.data_set_copy = self.data_set.copy()
        else:
            if index_focus is not None:
                # Render highlighted values in red
                for element_index in index_focus:
                    if element_index not in self.highlighted_bars:
                        self.canvas.delete(f"rect{element_index}")
                        self.highlighted_bars.append(element_index)
                        self.canvas.create_rectangle(element_index * self.bar_width,
                                                     self.graph_max_y - (self.data_set[element_index] * 6),
                                                     (element_index * self.bar_width) + self.bar_width, self.graph_max_y,
                                                     fill='red',
                                                     tags=f"rect{element_index}")
            else:
                # Change red highlighted bars to white
                for index in self.highlighted_bars:
                    self.canvas.delete(f"rect{index}")
                    self.canvas.create_rectangle(index * self.bar_width,
                                                 self.graph_max_y - (self.data_set[index] * 6),
                                                 (index * self.bar_width) + self.bar_width,
                                                 self.graph_max_y,
                                                 fill='white',
                                                 tags=f"rect{index}")
                self.data_set_copy = self.data_set.copy()
                self.highlighted_bars.clear()

            self.data_set_copy = self.data_set.copy()

    def generate_data_set(self):
        self.data_set.clear()

        for value in range(0, self.num_of_values):
            self.data_set.append(random.randrange(self.lower_value_range, self.upper_value_range))
        print(self.data_set)

    def calculate_bar_width(self):
        return self.graph_max_x / self.num_of_values

    def randomize_data(self):
        self.stop_sorting()
        self.generate_data_set()
        self.data_set_copy = None
        self.canvas.delete("all")  # Clears canvas
        self.build_visualizer()

    def stop_sorting(self):

        print("stop btn")
        self.stop_sort = True
        self.data_set_copy = None
