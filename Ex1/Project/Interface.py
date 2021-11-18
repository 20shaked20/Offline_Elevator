import tkinter as tk
from tkinter import Tk, Canvas, Frame, BOTH
from Building import Building
import pygame


class elevator_gui(Frame):

    def __init__(self, building: Building, calls: dict):
        super().__init__()
        self.building = building
        self.elevators_gui = list()
        self.floors_gui = []
        self.calls = calls
        self.init_ui()
        self.play()

    def init_ui(self):
        self.master.title("Building")
        self.pack(fill=BOTH, expand=1)
        floors = self.building.max_floor - self.building.min_floor
        elevators = len(self.building.elevators)
        canvas = Canvas(self)
        width = 400
        horozintal = 450
        for i in range(0, elevators):
            canvas.create_line(width, 500, width, 0, dash=(4, 2))

        for i in range(0, floors):
            self.floors_gui.append(canvas.create_line(5, horozintal, 800, horozintal))
            horozintal -= 40

        canvas.pack(fill=BOTH, expand=1)
        # elevator creating:
        # x1,y1,x2,y2
        elev1 = canvas.create_rectangle(40, 40, 10, 5, fill="magenta")
        canvas.move(elev1, 200, 450)
        elev2 = canvas.create_rectangle(40, 40, 10, 5, fill="magenta")
        canvas.move(elev2, 600, 450)
        self.elevators_gui.append(elev1)
        # canvas.move(elev1, 200,-400)
        self.elevators_gui.append(elev2)

        for call in self.calls:
            curr_call = call
            elev_id = curr_call[5]
            elev_src = curr_call[2]
            elev_dest = curr_call[3]
            if elev_id == 1:
                canvas.move(elev1, 200, 400)

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load("Elevator_Music.mp3")
        pygame.mixer.music.play(loops=0)


def main():
    root = Tk()
    b = "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    c = "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Calls/output_b2_a.csv"
    elevator_gui(building=Building.init_dict(b), calls=Building.init_calls(c))
    root.geometry("800x500")
    x = 0.0
    y = 1.0
    for i in range(0, 13):
        w = tk.Label(root, text="Floor:" + str(12 - i))
        w.place(x=x, y=y, anchor='sw')
        x += 0
        y += 40
    root.mainloop()


if __name__ == '__main__':
    main()
