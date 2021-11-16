"""
@authors: "Shaked & Yonatan"
date: Nov 5
"""
# import csv

import Building
import elevator
import Comparisons


def create_elev(elev_id: int):
    """
    right now im not using it, maybe later.
    :param elev_id: elev_ID
    :return: an object representing elevator
    """
    elev = elevator.Elevator(building.elevators[elev_id].id, building.elevators[elev_id].speed,
                             building.elevators[elev_id].minFloor,
                             building.elevators[elev_id].maxFloor, building.elevators[elev_id].closeTime,
                             building.elevators[elev_id].openTime,
                             building.elevators[elev_id].startTime, building.elevators[
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
    dest = int(call[3])
    idle = Comparisons.closestIdle(call, all_elevators)  # can return false
    on_way = Comparisons.closestOnTheWay(call, all_elevators)  # can return false
    busy = Comparisons.closestBusy(call, all_elevators)  # MUST return an elev object

    if idle is False and on_way is False:
        all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
        all_elevators[busy.id].last_assigned = call
        busy.elev_pos = call[3]
        updateState(busy, src, dest)
        return busy.id


    if idle is False:
        if Comparisons.arriveTimeOnWay(on_way, call) < Comparisons.arriveTimeBusy(busy, call):
            all_elevators[on_way.id].prev_assigned = all_elevators[on_way.id].last_assigned
            all_elevators[on_way.id].last_assigned = call
            on_way.elev_pos = call[3]
            updateState(on_way, src, dest)
            return on_way.id
        else:
            all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
            all_elevators[busy.id].last_assigned = call
            busy.elev_pos = call[3]
            updateState(busy, src, dest)
            return busy.id

    if on_way is False:
        if Comparisons.arriveTimeIdle(idle, call) < Comparisons.arriveTimeBusy(busy, call):
            all_elevators[idle.id].prev_assigned = all_elevators[idle.id].last_assigned
            all_elevators[idle.id].last_assigned = call
            idle.elev_pos = call[3]
            updateState(idle, src, dest)
            return idle.id
        else:
            all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
            all_elevators[busy.id].last_assigned = call
            busy.elev_pos = call[3]
            updateState(busy, src, dest)
            return busy.id

    busy_time = Comparisons.arriveTimeBusy(busy, call)
    idle_time = Comparisons.arriveTimeIdle(idle, call)
    on_way_time = Comparisons.arriveTimeOnWay(on_way, call)
    best_time = min(busy_time, idle_time, on_way_time)
    if best_time == idle_time:
        return idle.id
    if best_time == on_way_time:
        return on_way.id
    if best_time == busy_time:
        return busy.id


def updateState(elev, src, dest):
    if src < dest:
        elev.state = 1
    else:
        elev.state = -1


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
    file_in = r"C:\Users\yonar\PycharmProjects\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\Calls_b.csv"
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
