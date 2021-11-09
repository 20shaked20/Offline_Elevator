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
building = Building.Building.init_dict(file_loc1=file2_in)


# print(dict_b.elevators[0].__dict__)
# print(dict_b.elevators[1].speed)


def create_elev(id: int):
    """
    right now im not using it, maybe later.
    :param id: elev_ID
    :return: an object representing elevator
    """
    elev = elevator.Elevator(building.elevators[id].id, building.elevators[id].speed, building.elevators[id].minFloor,
                             building.elevators[id].maxFloor, building.elevators[id].closeTime,
                             building.elevators[id].openTime,
                             building.elevators[id].startTime, building.elevators[
                                 id].stopTime)  # elevator creation, need to create as many as we want, can use list? :)
    return elev


def allocate_elev(call, all_elevators):
    """
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """
    src = int(call[2])
    closest = find_closest(src, all_elevators)
    elev_curr = all_elevators[closest]
    elev_curr.go_to(src)
    return elev_curr.id


def find_closest(src: int, all_elevators):
    """
    :param src: Integer representing a source floor
    :return:  ID of the closest elevator.
    """
    closest = all_elevators[0]
    best_dist = all_elevators[0].get_pos() - src
    for curr_elevator in all_elevators:
        if curr_elevator.get_pos() - src < best_dist:
            best_dist = curr_elevator.get_pos() - src
            closest = curr_elevator
    return closest.id


def all_calls(elevators, d_calls):
    """
    This methods starts the simulation for all the elevators calls.
    :param d_calls: all the calls in the Calls.csv file
    :param elevators: list representing all the elevator in the building
    :return: the list 'elev_choices' to be merged with the csv output file.
    """
    elev_choices = []
    for calls in d_calls:
        elev_choices.append(allocate_elev(call=calls, all_elevators=elevators))
    return elev_choices


elev_choice = []  # route for elevators allocation
all_elevs = building.elevators  # all elevators as a list.
elev_choice = all_calls(all_elevs, dict_calls)

print(elev_choice)
