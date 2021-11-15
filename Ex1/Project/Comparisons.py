"""
@authors: "Shaked & Yonatan"
date: Nov 12
"""

import Building
import elevator


# call[1]  # time access
# call[2]  # src access
# call[3]  # destination access
# call[4]  # state access


def floorDiff(floor1, floor2):
    return abs(floor1 - floor2)


def distanceFromElev(elev: elevator, floor: int):
    curr = elev.pos
    return abs(curr - floor)


def distanceAsTimeFromElev(elev: elevator, floor: int):
    return distanceFromElev(elev, floor) * (getSpeed(elev) + getFloorTime(elev))


def getLastCall(elev: elevator):
    return elev.last_assigned  # return tuple in the form: (time,src,dest)


def isIdle(elev: elevator, call):
    x = floorDiff(elev.last_assigned[2], elev.last_assigned[3])
    x = x * (getSpeed(elev) + getFloorTime(elev))
    return elev.last_assigned[1] + x < call[1]  # return last call time + arrival time < current call


def getTimeToDest(elev: elevator):
    return distanceAsTimeFromElev(elev, elev.last_assigned[2]) * (getSpeed(elev) + getFloorTime(elev))


# TODO: this function should return how many floors were passed since the elevator's last
def getCurr(elev, curr_time):
    # suggestion: (curr_time - elev.last_assigned[1]) -> multiply or divide by -> elev.speed
    pass


def getTimeFromCurr(elev: elevator, floor: int, curr_time):
    curr = elev.last_assigned[2] + getCurr(elev, curr_time)
    floors = floorDiff(curr, floor)
    return floors * (getSpeed(elev) + getFloorTime(elev))


def getSpeed(elev: elevator):
    return elev.speed


def getFloorTime(elev: elevator):
    return elev.closeTime + elev.openTime + elev.startTime + elev.stopTime


def closestIdle(call, all_elev):
    closest: elevator = all_elev[0]
    for elev in all_elev:
        if isIdle(elev, call):
            if arriveTimeIdle(elev, call) < arriveTimeIdle(closest, call):
                closest = elev
    return closest


# TODO: figure out logic for this boolean, by considering current call time and elevator's last assigned call
def isOnWay(elev, call):
    pass


def theoreticalTime(elev: elevator, floor1: int, floor2: int):
    """
    calculates time that would take elev to move from floor1 to floor 2
    :param elev: elevator for which calculation is done
    :param floor1: floor represented as an int
    :param floor2: floor represented as an int
    :return: time in double
    """
    floors = floorDiff(floor1, floor2)
    return floors * (getSpeed(elev) + getFloorTime(elev))


def closestOnTheWay(call, all_elev):
    closest: elevator = all_elev[0]
    for elev in all_elev:
        if isOnWay(elev, call):
            if arriveTimeOnWay(elev, call) < arriveTimeOnWay(closest, call):
                closest = elev
    return closest


def closestBusy(call, all_elev):
    closest: elevator = all_elev[0]
    for elev in all_elev:
        if isIdle(elev, call) is False:
            if arriveTimeBusy(elev, call) < arriveTimeBusy(closest, call):
                closest = elev
    return closest


# time from curr if applicable
def arriveTimeOnWay(elev, call):
    return getTimeFromCurr(elev, call[2], call[1])


# time from curr if applicable
def arriveTimeIdle(elev, call):
    return theoreticalTime(elev, elev.pos, call[2])


# time from current to dest then from dest to src
def arriveTimeBusy(elev, call):
    return getTimeFromCurr(elev, elev.last_assigned[3], call[1]) + theoreticalTime(elev, elev.last_assigned[3], call[2])
