"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""

import json
import csv

from elevator import Elevator


class Building(object):

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
        This method builds a dictionary from json file while creating the elevator objects.
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
        This method creates a dictionary of elevator calls using the Calls.csv file
        :param file_loc2: String representing a file location
        :return: a dictionary of elevator calls
        """
        dict_calls = []
        with open(file_loc2, "r") as f:
            calls = csv.reader(f)
            for row in calls:
                dict_calls.append(row)
        return dict_calls

    @classmethod
    def create_csv(cls, file_in: str, route: str, file_out: str, elev_choices):
        dict_in = []
        dict_route = []
        with open(file_in, 'r') as f:
            writer_in = csv.reader(f)
            for row in writer_in:
                dict_in.append(row)

        with open(routes, 'w') as f2:
            writer_route = csv.writer(f2)
            for index in elev_choices:
                x = elev_choices[index]  # i don't want list.
                dict_route.append(x)

        print("DICT_ROUTE:")
        print(dict_route)
        print("input:")
        print(dict_in)
        i = 0
        for row in dict_in:
            dict_in[i][5] = dict_route[i]  # places the right elevator.. :D
            i += 1
        print("output:")
        print(dict_in)

        with open(file_out, 'w') as f3:
            writer_out = csv.writer(f3)
            for row in dict_in:
                writer_out.writerow(row)


# CSV creation > > ?
# TODO: fix the line gap


file_in = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
file_out = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/output.csv"
routes = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/route.csv"
