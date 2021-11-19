import csv
import tkinter as tk
from tkinter import Frame, BOTH
import Ex1.Project.Building
import pygame
import time


class ElevatorGui(Frame):

    def __init__(self, building: Ex1.Project.Building.Building):
        super().__init__()
        self.building = building
        self.pos_0 = 0
        self.pos_1 = 0
        self.root = tk.Tk()
        self.floors = self.building.max_floor - self.building.min_floor + 1
        self.canvas = tk.Canvas(self.root, width=850, height=500)
        self.root.title("Building")
        self.root.resizable(False, False)
        self.elevators_gui = []
        self.floors_gui = []
        self.calls_log = []
        self.log_modifier("/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/Project/GUI/log_b2_a.log")
        self.init_ui()
        self.floor_names()
        self.play()
        self.movement()

    def init_ui(self):
        """
        This method initializes the ui.
        i'e -> creates objects ( lines, elevators, floors... )
        """
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
            self.canvas.move(elev, x1, gap_floors * self.building.max_floor)  # init to floor 0
            self.elevators_gui.append(elev)
            x1 += x1

    def movement(self):
        animation_refresh_seconds = 0.0001
        gap = 500 / self.floors
        for call in self.calls_log:
            self.canvas.update()
            src = int(call[8])
            dest = int(call[9])
            elev_id = int(call[11])
            speed = self.building.elevators[elev_id].speed
            curr_pos = self.get_pos(elev_id)
            elev_states = self.elev_state(curr_pos, src)
            if elev_states == 1:  # goes up curr > src
                gap_src = gap * abs(src - curr_pos)
                while gap_src > 0:
                    self.canvas.update()
                    movement = speed
                    if gap_src - speed < 0:
                        movement = gap_src
                    time.sleep(animation_refresh_seconds)
                    self.canvas.move(self.elevators_gui[elev_id], 0, -movement)  # UP
                    self.keep_in_bounds(self.elevators_gui[elev_id])
                    self.canvas.update()
                    gap_src -= movement
                self.update_pos(src, elev_id)
                elev_states = self.elev_state(curr_pos, dest)
                self.canvas.update()
                if elev_states == 1:  # goes up src > dest
                    gap_dest = gap * abs(dest - curr_pos)
                    while gap_dest > 0:
                        self.canvas.update()
                        movement = speed
                        if gap_dest - speed < 0:
                            movement = gap_dest
                        time.sleep(animation_refresh_seconds)
                        self.canvas.move(self.elevators_gui[elev_id], 0, -movement)  # UP
                        self.keep_in_bounds(self.elevators_gui[elev_id])
                        self.canvas.update()
                        gap_dest -= movement
                    self.update_pos(dest, elev_id)
                else:  # goes down src > dest
                    gap_dest = gap * abs(dest - curr_pos)
                    while gap_dest > 0:
                        self.canvas.update()
                        movement = speed
                        if gap_dest + speed > 500:
                            movement = gap_dest
                        time.sleep(animation_refresh_seconds)
                        self.canvas.move(self.elevators_gui[elev_id], 0, movement)  # DOWN
                        self.keep_in_bounds(self.elevators_gui[elev_id])
                        self.canvas.update()
                        gap_dest -= movement
                    self.update_pos(dest, elev_id)

            if elev_states == -1:  # goes down curr > src
                gap_src = gap * abs(src - curr_pos)
                while gap_src > 0:
                    movement = speed
                    if gap_src + speed > 500:
                        movement = gap_src
                    time.sleep(animation_refresh_seconds)
                    self.canvas.move(self.elevators_gui[elev_id], 0, movement)  # DOWN
                    self.keep_in_bounds(self.elevators_gui[elev_id])
                    self.canvas.update()
                    gap_src -= movement
                self.update_pos(src, elev_id)
                elev_states = self.elev_state(curr_pos, dest)
                if elev_states == 1:  # goes up src > dest
                    gap_dest = gap * abs(dest - curr_pos)
                    while gap_dest > 0:
                        movement = speed
                        if gap_dest - speed < 0:
                            movement = gap_dest
                        time.sleep(animation_refresh_seconds)
                        self.canvas.move(self.elevators_gui[elev_id], 0, -movement)  # UP
                        self.keep_in_bounds(self.elevators_gui[elev_id])
                        self.canvas.update()
                        gap_dest -= movement
                    self.update_pos(dest, elev_id)
                else:  # goes down src > dest
                    gap_dest = gap * abs(dest - curr_pos)
                    while gap_dest > 0:
                        movement = speed
                        if gap_dest + speed > 500:
                            movement = gap_dest
                        time.sleep(animation_refresh_seconds)
                        self.canvas.move(self.elevators_gui[elev_id], 0, movement)  # DOWN
                        self.keep_in_bounds(self.elevators_gui[elev_id])
                        self.canvas.update()
                        gap_dest -= movement
                    self.update_pos(dest, elev_id)
            self.canvas.update()

    @classmethod
    def elev_state(cls, src, dest):
        if src < dest:
            return 1  # goes up
        else:
            return -1  # goes down

    def play(self):
        """
        This method is responsible for music background in the simulation
        """
        pygame.mixer.init()
        pygame.mixer.music.load("/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/Project/GUI/Elevator_Music.mp3")
        pygame.mixer.music.play(loops=0)

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

    def floor_names(self):
        """
        This method assigns floor names for each floor.
        """
        x = 10.0
        y = 0.0
        gap = 500 / self.floors
        for i in range(self.building.min_floor - 1, self.building.max_floor + 1):
            w = tk.Label(self.root, text="Floor " + str(self.building.max_floor + self.building.min_floor - i))
            w.place(x=x, y=y, anchor='sw')
            y += gap

    def keep_in_bounds(self, elev_obj):
        x1, y1, x2, y2 = self.canvas.coords(elev_obj)
        if y2 > 500:  # if out of bounds at bottom
            move_by = 500 - y2
            self.canvas.move(elev_obj, 0, move_by)
        if y1 < 0:
            move_by = -y1
            self.canvas.move(elev_obj, 0, move_by)

    def update_pos(self, floor, elev_id):
        if elev_id == 0:
            self.pos_0 = floor
        else:
            self.pos_1 = floor

    def get_pos(self, elev_id):
        if elev_id == 0:
            return self.pos_0
        else:
            return self.pos_1


if __name__ == '__main__':
    b = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    elevator_guix = ElevatorGui(building=Ex1.Project.Building.Building.init_dict(b))
    elevator_guix.root.mainloop()
