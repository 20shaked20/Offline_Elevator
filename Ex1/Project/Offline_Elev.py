"""
@authors: "Shaked & Yonatan"
date: Nov 5
"""
import sys

import Building
import Comparisons


def allocate_elev(call, all_elevators):
    """
    This methods allocates the best elevator to a call.
    :param call: a single call (time,s,d...)
    :param all_elevators: all the elevators that are in the building
    :return: the best elevator to send.
    """

    src = int(call[2])
    dest = int(call[3])
    idle = Comparisons.closest_idle(call, all_elevators)  # can return false
    on_way = Comparisons.closest_on_the_way(call, all_elevators)  # can return false
    busy = Comparisons.closest_busy(call, all_elevators)  # MUST return an elev object

    if idle is False and on_way is False:
        all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
        all_elevators[busy.id].last_assigned = call
        busy.elev_pos = call[3]
        update_state(busy, src, dest)
        return busy.id

    if idle is False:
        if Comparisons.arriveTimeOnWay(on_way, call) < Comparisons.arriveTimeBusy(busy, call):
            all_elevators[on_way.id].prev_assigned = all_elevators[on_way.id].last_assigned
            all_elevators[on_way.id].last_assigned = call
            on_way.elev_pos = call[3]
            update_state(on_way, src, dest)
            return on_way.id
        else:
            all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
            all_elevators[busy.id].last_assigned = call
            busy.elev_pos = call[3]
            update_state(busy, src, dest)
            return busy.id

    if on_way is False:
        if Comparisons.arriveTimeIdle(idle, call) < Comparisons.arriveTimeBusy(busy, call):
            all_elevators[idle.id].prev_assigned = all_elevators[idle.id].last_assigned
            all_elevators[idle.id].last_assigned = call
            idle.elev_pos = call[3]
            update_state(idle, src, dest)
            return idle.id
        else:
            all_elevators[busy.id].prev_assigned = all_elevators[busy.id].last_assigned
            all_elevators[busy.id].last_assigned = call
            busy.elev_pos = call[3]
            update_state(busy, src, dest)
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


def update_state(elev, src, dest):
    """
    This methods updates the up/down motion for a current elevator.
    :param elev: represents an elevator
    :param src: integer representing a src floor
    :param dest: integer representing a destination floor
    """
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


# Reading input names:
def inputs():
    """
    This method loads from command line 3 inputs.
    :return: the right one.
    """
    if len(sys.argv) == 4:
        check = {
            "Building": sys.argv[1],
            "Calls": sys.argv[2],
            "Output": sys.argv[3]
        }
    else:
        check = {
            "Building": "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Buildings/B5.json",
            "Calls": "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv",
            "Output": "/Users/Shaked/PycharmProjects/Offline_Elevator_2/Ex1/data/Ex1_input/Ex1_Calls/output.csv"
        }
    return check


if __name__ == '__main__':
    sys_inputs = inputs()
    # LOADING THE CSV FILE :
    dict_calls = []
    dict_calls = Building.Building.init_calls(file_loc2=sys_inputs["Calls"])

    # LOADING THE JSON FILE:
    building = Building.Building.init_dict(file_loc1=sys_inputs["Building"])

    elev_choice = []  # route for elevators allocation
    all_elevs = building.elevators  # all elevators as a list.
    elev_choice = all_calls(all_elevs, dict_calls)

    # WRITING THE OUTPUT:
    Building.Building.csv_output(sys_inputs["Calls"], sys_inputs["Output"], elev_choice)
