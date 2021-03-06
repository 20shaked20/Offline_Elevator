"""
@authors: "Shaked & Yonatan"
date: Nov 12
"""
from Ex1.Project import elevator


def floor_diff(floor1, floor2):
    """
    :param floor1: represents a floor in the building
    :param floor2: represents a floor in the building
    :return: the distance between both floors
    """
    return abs(int(floor1) - int(floor2))


def distance_from_elev(elev: elevator, floor: int):
    """
    :param elev: represents an elevator
    :param floor: represents a floor in the building
    :return: the distance between current elevator position to a floor.
    """
    curr = elev.pos
    return abs(curr - floor)


def distance_as_time_from_elev(elev: elevator, floor: int):
    """
    :param elev: represents an elevator
    :param floor: represents a floor in the building
    :return: how long it will take to reach that floor.
    """
    return distance_from_elev(elev, floor) / get_speed(elev) + get_floor_time(elev)


def get_last_call(elev: elevator):
    """
    :param elev: represents an elevator
    :return: tuple in the form: (time,src,dest)
    """
    return elev.last_assigned


def is_idle(elev: elevator, call):
    """
    :param elev: represents an elevator
    :param call: represents a call in the building
    :return: if the elevator is idle or not.
    """
    x = floor_diff(elev.last_assigned[2], elev.last_assigned[3])
    x = x / get_speed(elev) + get_floor_time(elev)
    if float(elev.last_assigned[1]) + x <= float(call[1]):
        elev.elev_state = 0
        return True
    else:
        return False


def get_time_to_dest(elev: elevator):
    """
    :param elev: represents an elevator
    :return: time it will take the elevator to reach a destination floor.
    """
    return distance_as_time_from_elev(elev, elev.last_assigned[2]) / get_speed(elev) + get_floor_time(elev)


def get_curr(elev: elevator, call):
    """
    this function returns the theoretical location of the elevator, based on the current call's time
    and the previous calls time.
    :param elev: the elevator for which this calculation is done
    :param call: the current call that is being evaluated
    :return: floors passed since last assigned call and current call (which is being evaluated)
    """
    if is_idle(elev, call):
        return elev.elev_pos
    time_diff = float(call[1]) - float(elev.last_assigned[1])
    x = time_diff / get_speed(elev)
    return int(elev.last_assigned[2]) + int(x + elev.closeTime + elev.startTime)


def get_time_from_curr(elev: elevator, floor: int, call):
    """
    :param elev: represents an elevator
    :param floor: represents a floor in the building
    :param call: represents a call in the building
    :return: the time it will take to reach a floor from current position
    """
    curr = get_curr(elev, call)
    floors = floor_diff(curr, floor)
    return floors / get_speed(elev) + get_floor_time(elev)


def get_speed(elev: elevator):
    """
    :param elev: represents an elevator
    :return: speed of current elevator
    """
    return float(elev.speed)


def get_floor_time(elev: elevator):
    """
    :param elev: represents an elevator
    :return: a simple floor time calculation
    """
    return elev.closeTime + elev.openTime + elev.startTime + elev.stopTime


def is_on_way(elev, call):
    """
    :param elev: represents an elevator
    :param call: represents a call in the building
    :return: if the call is on the way of current elevator.
    """
    if is_idle(elev, call):
        return False
    call_dir = get_direction(call)
    elev_dir = elev.elev_state
    if elev_dir != call_dir:
        return False
    curr = get_curr(elev, call)
    if call_dir == 1:
        if curr > call[2]:
            return False
    if call_dir == -1:
        if curr < call[2]:
            return False
    return True


def get_direction(call):
    """
    :param call: represents a call
    :return: what direction is the elevator going UP = 1, DOWN = -1
    """
    if call[2] < call[3]:
        return 1
    else:
        return -1


def theoretical_time(elev: elevator, floor1: int, floor2: int):
    """
    calculates time that would take elev to move from floor1 to floor 2
    :param elev: elevator for which calculation is done
    :param floor1: floor represented as an int
    :param floor2: floor represented as an int
    :return: time in double
    """
    floors = floor_diff(floor1, floor2)
    return floors / get_speed(elev) + get_floor_time(elev)


def closest_idle(call, all_elev):
    """
    :param call: represents a call in the building
    :param all_elev: list that contains all the elevators.
    :return: the closest idle elevator.
    """
    closest: elevator = all_elev[0]
    changed = False
    for elev in all_elev:
        if is_idle(elev, call):
            time_elev = arriveTimeIdle(elev, call)
            time_closest = arriveTimeIdle(closest, call)
            if time_elev < time_closest:
                closest = elev
                changed = True
    if changed is False:
        if is_idle(closest, call) is False:
            return False
    return closest


def closest_on_the_way(call, all_elev):
    """
    :param call: represents a call in the building
    :param all_elev: list that contains all the elevators.
    :return: closest elevator that is on its way.
    """
    closest: elevator = all_elev[0]
    changed = False
    for elev in all_elev:
        if is_on_way(elev, call):
            if arriveTimeOnWay(elev, call) < arriveTimeOnWay(closest, call):
                closest = elev
                changed = True
    if changed is False:
        if is_on_way(closest, call) is False:
            return False
    return closest


def closest_busy(call, all_elev):
    """
    :param call: represents a call in the building
    :param all_elev: list that contains all the elevators
    :return: closest elevator that is 'busy'.
    """
    closest: elevator = all_elev[0]
    for elev in all_elev:
        if is_idle(elev, call) is False:
            if arriveTimeBusy(elev, call) < arriveTimeBusy(closest, call):
                closest = elev
    return closest


# time from curr if applicable
def arriveTimeOnWay(elev, call):
    return get_time_from_curr(elev, call[2], call)


# time from curr if applicable
def arriveTimeIdle(elev, call):
    return theoretical_time(elev, elev.elev_pos, call[2])


# time from current to dest then from dest to src
def arriveTimeBusy(elev, call):
    return get_time_from_curr(elev, elev.last_assigned[3], call) + theoretical_time(elev, elev.last_assigned[3],
                                                                                    call[2])
