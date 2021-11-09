"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""
import csv

import Building
import elevator

# LOADING THE CSV FILE :
file_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv"
dict_calls = []
dict_calls = Building.Building.init_calls(file_loc2=file_in)
# print(dict_calls)
# print(dict_calls[0][1])  # time access
# print(dict_calls[0][2])  # src access
# print(dict_calls[0][3])  # destination access
# print(dict_calls[0][4])  # state access

# LOADING THE JSON FILE : working example
file2_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Buildings\B1.json"
dict_b = Building.Building.init_dict(file_loc1=file2_in)


# print(dict_b.elevators[0].__dict__)
# print(dict_b.elevators[1].speed)

def create_elev(id: int):
    """
    :param id: elev_ID
    :return: an object representing elevator
    """
    elev = elevator.Elevator(dict_b.elevators[id].id, dict_b.elevators[id].speed, dict_b.elevators[id].minFloor,
                             dict_b.elevators[id].maxFloor, dict_b.elevators[id].closeTime,
                             dict_b.elevators[id].openTime,
                             dict_b.elevators[id].startTime, dict_b.elevators[
                                 id].stopTime)  # elevator creation, need to create as many as we want, can use list? :)
    return elev


elev_choice = [100]  # route for elevators allocation


def allocate_elev(call, all_elevators):
    """
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """


def find_closest(s, all_elevators):
    """
    :param s: Integer representing a source floor
    :return:  ID of the closest elevator.
    """
    closest = all_elevators[0]
    dist = all_elevators[0].get_pos() - s
    for x in range(len(all_elevators)):
        if all_elevators[x].get_pos() - s < dist:
            dist = all_elevators[x].get_pos() - s
            closest = all_elevators[x]
    return closest


def all_calls():
    """
    this method just starts the simulation for the calls in the dictionary
    """
    for calls in dict_calls:
        allocate_elev(call=calls)


def get_elevators(dict_building):
    """
    :param dict_building: a building dictionary
    :return: how many elevators are in the building(this way we can access them by their id
    """
    length = len(dict_building.elevators)
    elevs = [length]
    for x in range(length):
        elevs[x] = dict_building.elevators[x]
    return elevs


all_elevs = get_elevators(dict_b)
print(all_elevs[0].__dict__)
find_closest(3, all_elevs)
