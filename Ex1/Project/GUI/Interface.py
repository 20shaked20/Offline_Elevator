import csv
import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH
import Ex1.Project.Building
import pygame
import time
import timer  # my own timer, credits to : Elad sezanayev


class elevator_gui(Frame):

    def __init__(self, building: Ex1.Project.Building.Building):
        super().__init__()
        self.building = building
        self.root = Tk()
        self.root.geometry("850x500")
        self.floors = self.building.max_floor - self.building.min_floor
        self.canvas = Canvas(self.root)
        self.root.title("Building")
        self.elevators_gui = []
        # self.timer = timer.Timer()  # timer builder
        self.floors_gui = []
        self.calls_log = []
        self.log_modifier("/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/Project/GUI/log_b2_a.log")
        self.init_ui()
        self.play()
        self.create_window()
        # self.movement()

    def init_ui(self):
        self.pack(fill=BOTH, expand=1)

        # FLOORS:
        gap_floors = 500 / self.floors
        horozintal = 500
        for i in range(0, self.floors):
            self.floors_gui.append(self.canvas.create_line(80, horozintal, 850, horozintal))
            horozintal -= gap_floors

        # ELEVATORS SIDINGS:
        elevators = len(self.building.elevators)
        gap_elevators = 850 / elevators
        width = gap_elevators
        self.canvas.create_line(80, 500, 80, 0)
        for i in range(0, elevators):
            self.canvas.create_line(width, 500, width, 0, dash=(4, 2))
            width += gap_elevators

        self.canvas.pack(fill=BOTH, expand=1)

        # ELEVATOR OBJECTS:
        x1 = 550 / elevators
        for i in range(0, elevators):
            elev = (self.canvas.create_rectangle(35, 35, 10, 5, fill="magenta"))
            self.canvas.move(elev, x1, 460)
            print(x1)
            self.elevators_gui.append(elev)
            x1 += x1

    # print(self.calls_log[1][14])  # start time
    # print(self.calls_log[1][7])  # end time
    # print(self.calls_log[1][8])  # src floor
    # print(self.calls_log[1][9])  # dest floor
    # print(self.calls_log[1][11])  # elev_id

    def movement(self, root):
        pass

    def play(self):
        pygame.mixer.init()
        # pygame.mixer.music.load("/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/Project/GUI/Elevator_Music.mp3")
        # pygame.mixer.music.play(loops=0)

    def log_modifier(self, file_loc: str):

        """
        This method modifies a log file.
        :param file_loc: getting a log file location.
        :return: modified log to my own usage
        """
        with open(file_loc, 'r') as f:
            writer_in = csv.reader(f)
            for row in writer_in:
                if row[1] == 'Elev' and row[3] == '  arrived at dest':
                    self.calls_log.append(row)

        with open(file_loc, 'w', newline='') as f3:
            writer_out = csv.writer(f3)
            for row in self.calls_log:
                writer_out.writerow(row)

    def create_window(self):
        # floor names:
        floors = self.floors
        x = 10.0
        y = 0.0
        gap = 500 / floors
        for i in range(0, 13):
            w = tk.Label(self.root, text="Floor " + str(12 - i))
            w.place(x=x, y=y, anchor='sw')
            y += gap - 1.75
        # self.root.resizable(False, False)

        # MOVEMENT:
        animation_refresh_seconds = 0.05
        i = 0
        for x in range(0,30):
            self.root.update()
            time.sleep(animation_refresh_seconds)
            self.canvas.move(self.elevators_gui[0], 0, i)
            self.canvas.move(self.elevators_gui[1], 0, i)
            i -= 1

        # for call in self.calls_log:
        #     x = 0
        #     y = 500 / 12 * int(call[8])
        #     if call[11] == 0:  # elev_0
        #         self.canvas.move(elevator_gui[0], 275, y)
        #         time.sleep(animation_refresh_seconds)
        #         elev_pos = self.canvas.coords(elevator_gui[0])
        #     if call[11] == 1:  # elev_1
        #         self.canvas.move(elevator_gui[0], 550, y)
        #         time.sleep(animation_refresh_seconds)
        #         elev_pos = self.canvas.coords(elevator_gui[1])
        self.root.mainloop()


if __name__ == '__main__':
    b = "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    c = "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Calls/output_b2_a.csv"
    elevator_guix = elevator_gui(building=Ex1.Project.Building.Building.init_dict(b))
    # elevator_guix.create_window()
