"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""
import csv

from Building import Building
from elevator import Elevator
from comparators import Comparators


# TODO : make a better algorithm ->
#   1. pickup more callers on the way if they are already there.
#   2. implement routing system for elevators
#   3. consider using up/down somehow?..

def create_elev(id: int):
    """
    right now im not using it, maybe later.
    :param id: elev_ID
    :return: an object representing elevator
    """
    elev = Elevator(building.elevators[id].id, building.elevators[id].speed, building.elevators[id].minFloor,
                    building.elevators[id].maxFloor, building.elevators[id].closeTime,
                    building.elevators[id].openTime,
                    building.elevators[id].startTime, building.elevators[
                        id].stopTime)  # elevator creation, need to create as many as we want, can use list? :)
    return elev


def allocate_elev(call, all_elevators, elev_route):
    """
    This methods allocates the best elevator to a call.
    :param elev_route:
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """
    # TODO:
    #       fix this function to have a routing system maybe or check elevators in better way.
    #       Right now it only sends the fastest elevator and sometimes close ones, i need to fix it.

    # src = int(call[2])
    destination = int(call[3])
    # closest = Comparators.find_closest(src, all_elevators)
    elev_curr = all_elevators[0]
    # elev_curr.go_to(src)  # goes directly to source, picks him up
    elev_curr.go_to(destination)  # and then goes directly to destination, removes the caller.
    index = Comparators.best_elev(call, all_elevators)
    return index


def all_calls(elevators, d_calls, elev_routes):
    """
    This methods starts the simulation for all the elevators calls.
    :param elev_routes:
    :param d_calls: all the calls in the Calls.csv file
    :param elevators: list representing all the elevator in the building
    :return: the list 'elev_choices' to be merged with the csv output file.
    """
    elev_choices = []
    for calls in d_calls:
        elev_choices.append(allocate_elev(call=calls, all_elevators=elevators, elev_route=elev_routes))
    return elev_choices


if __name__ == '__main__':
    # LOADING THE CSV FILE :
    file_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\Calls_d.csv"
    dict_calls = []
    dict_calls = Building.init_calls(file_loc2=file_in)
    # print(dict_calls)
    # print(dict_calls[0][1])  # time access
    # print(dict_calls[0][2])  # src access
    # print(dict_calls[0][3])  # destination access
    # print(dict_calls[0][4])  # state access

    # LOADING THE JSON FILE : working example
    Json_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Buildings\B5.json"
    building = Building.init_dict(file_loc1=Json_in)
    elev_choice = []  # elevators allocation
    elev_route = [[], []]  # route of current elevator.
    all_elevs = building.elevators  # all elevators as a list.
    elev_choice = all_calls(all_elevs, dict_calls, elev_route)

    print("Elev Choices:")
    print(elev_choice)

    file_out = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\output.csv"
    Building.csv_output(file_in, file_out, elev_choice)
