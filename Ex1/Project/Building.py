"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""

import json
import csv

from elevator import Elevator

FILE = ""


class Building:

    def __init__(self, elevators, min_floor, max_floor):
        """
        :param elevators: array of elevators inside our building
        :param min_floor: Integer representing minimum floor for the building
        :param max_floor: Integer representing maximum floor for the building
        """
        self.elevators = elevators
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.__author__ = "Shaked & Yonathan"

    @classmethod
    def init_dict(cls, file_loc1: str):
        """
        :param file_loc1: String representing a file location
        :return: Building dictionary
        """
        with open(file_loc1, "r") as f:
            dict_b = json.load(f)
            min_floor = dict_b["_minFloor"]
            max_floor = dict_b["_maxFloor"]
            elevators = [Elevator.from_dict(_elevator) for _elevator in dict_b["_elevators"]]
        return cls(elevators, min_floor, max_floor)

    @classmethod
    def init_calls(cls, file_loc2: str):
        """
        :param file_loc2: String representing a file location
        :return: a dictionary of elevator calls
        """
        dict_calls = []
        with open(file_loc2, "r") as f:
            calls = csv.reader(f)
            for row in calls:
                dict_calls.append(row)
        return dict_calls


"""
# Test_Check:
file = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B2.json"
x = Building.init_dict(file_loc1=file)
# print(x.elevators[1].__dict__)
# print(x.elevators[1].id)

file2 = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
rows = Building.init_calls(file_loc2=file2)
i = 0;
for row in rows:
    print(rows[i][2])  # prints all the srcs :D
    i += 1
"""
