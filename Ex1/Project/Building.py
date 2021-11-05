"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""

import json
# TODO: use for reading from csv files later.
import csv

from elevator import Elevator

FILE = ""


class Building:

    def __init__(self, elevators, min_floor, max_floor):
        self.elevators = elevators
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.__author__ = "Shaked & Yonathan"

    @classmethod
    def init_dict(cls, file_loc: str):
        with open(file_loc, "r") as f:
            dict_b = json.load(f)
            min_floor = dict_b["_minFloor"]
            max_floor = dict_b["_maxFloor"]
            elevators = [Elevator.from_dict(_elevator) for _elevator in dict_b["_elevators"]]
        return cls(elevators, min_floor, max_floor)


# Test_Check:
file = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
x = Building.init_dict(file_loc=file)
print(x.elevators[1].__dict__)
print(x.elevators[1].id)
