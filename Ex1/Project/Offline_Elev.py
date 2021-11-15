"""
@authors: "Shaked & Yonatan"
date: Nov 5
"""
import csv

import Building
import elevator
import Comparisons


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
    This methods allocates the best elevator to a call.
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """
    src = int(call[2])
    idle = Comparisons.closestIdle(call)  # can return false
    on_way = Comparisons.closestOnTheWay(call)  # can return false
    busy = Comparisons.closestBusy(call)  # MUST return an elev object

    if idle is False and on_way is False:
        all_elevators[busy].prev_assigned = all_elevators[busy].last_assigned
        all_elevators[busy].last_assigned = call
        return busy

    if idle is False:
        if Comparisons.arriveTimeOnWay(on_way, src) < Comparisons.arriveTimeBusy(busy, src):
            all_elevators[on_way].prev_assigned = all_elevators[on_way].last_assigned
            all_elevators[on_way].last_assigned = call
            return on_way
        else:
            all_elevators[busy].prev_assigned = all_elevators[busy].last_assigned
            all_elevators[busy].last_assigned = call
            return busy

    if on_way is False:
        if Comparisons.arriveTimeIdle(on_way, src) < Comparisons.arriveTimeBusy(busy, src):
            all_elevators[idle].prev_assigned = all_elevators[idle].last_assigned
            all_elevators[idle].last_assigned = call
            return idle
        else:
            all_elevators[busy].prev_assigned = all_elevators[busy].last_assigned
            all_elevators[busy].last_assigned = call
            return busy


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
    dict_calls = Building.Building.init_calls(file_loc2=file_in)
    # print(dict_calls)
    # print(dict_calls[0][1])  # time access
    # print(dict_calls[0][2])  # src access
    # print(dict_calls[0][3])  # destination access
    # print(dict_calls[0][4])  # state access

    # LOADING THE JSON FILE : working example
    Json_in = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B5.json"
    building = Building.Building.init_dict(file_loc1=Json_in)
    elev_choice = []  # route for elevators allocation
    all_elevs = building.elevators  # all elevators as a list.
    elev_choice = all_calls(all_elevs, dict_calls)

    print("Elev Choices:")
    print(elev_choice)

    file_out = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/output.csv"
    Building.Building.csv_output(file_in, file_out, elev_choice)
