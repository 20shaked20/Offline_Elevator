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


def allocate_elev(call, all_elevators):
    """
    This methods allocates the best elevator to a call.
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """
    # TODO:
    #      Try consider up/down/idle cases

    best_elev_id = Comparators.best_elev(call, all_elevators)
    curr_elev = all_elevators[best_elev_id]
    Comparators.src_in_route(call, curr_elev)
    return best_elev_id


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


if __name__ == '__main__':
    # LOADING THE CSV FILE :
    file_in = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/Calls_d.csv"
    dict_calls = []
    dict_calls = Building.init_calls(file_loc2=file_in)

    # LOADING THE JSON FILE : working example
    Json_in = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B5.json"
    building = Building.init_dict(file_loc1=Json_in)
    elev_choice = []  # elevators allocation
    all_elevs = building.elevators  # all elevators as a list.
    elev_choice = all_calls(all_elevs, dict_calls)

    print("Elev Choices:")
    print(elev_choice)

    # CREATING CSV OUTPUT FILE:
    file_out = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/output.csv"
    Building.csv_output(file_in, file_out, elev_choice)



"""
def create_elev(id: int):
    
    right now im not using it, maybe later.
    :param id: elev_ID
    :return: an object representing elevator

    elev = Elevator(building.elevators[id].id, building.elevators[id].speed, building.elevators[id].minFloor,
                    building.elevators[id].maxFloor, building.elevators[id].closeTime,
                    building.elevators[id].openTime,
                    building.elevators[id].startTime, building.elevators[
                        id].stopTime)  # elevator creation, need to create as many as we want, can use list? :)
    return elev
"""