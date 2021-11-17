from tkinter import *
from tkinter.ttk import *
from Building import Building


class gui_elevator:

    def __init__(self, building: Building, file_name: str):
        self.building = building
        self.elevators_gui = []
        self.floors_gui = []
        self.window = Tk()
        self.canvas = Canvas(self.window)
        self.window.geometry("800x500")
        self.draw_floors()
        self.draw_elevators()

    def draw_floors(self):
        floors = self.building.max_floor - self.building.min_floor
        gap = int(800 / floors)
        # x1,y1,x2,y2#
        for i in range(0, floors):
            self.canvas.create_line(5, 300, 20, 300)
            #   self.floors_gui.append(curr_line)

    def draw_elevators(self):
        pass


if __name__ == '__main__':
    b = "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
    gui_elevator = gui_elevator(Building.init_dict(b), "")
    print(gui_elevator.floors_gui)
    mainloop()
