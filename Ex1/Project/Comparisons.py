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

@classmethod
def floorDiff(cls, floor1, floor2):
    return abs(floor1 - floor2)


@classmethod
def distanceFromElev(cls, elev: elevator, floor: int):
    curr = elev.pos
    return abs(curr - floor)


def distanceAsTimeFromElev(cls, elev: elevator, floor: int):
    return distanceFromElev(cls, elev, floor) * (getSpeed(elev) + getFloorTime(elev))


@classmethod
def getLastCall(cls, elev: elevator):
    return elev.last_assigned  # return tuple in the form: (time,src,dest)


"""
returns literal closest elevator whether its 'busy' or not
"""


@classmethod
def getClosest(cls, all_elevators, floor: int):
    closest = all_elevators.elevators[0]
    for elev in all_elevators:
        if distanceAsTimeFromElev(cls, elev, floor) < distanceAsTimeFromElev(cls, closest, floor):
            closest = elev
    return closest.id


@classmethod
def isIdle(cls, elev: elevator, call):
    x = floorDiff(elev.last_assigned[2], elev.last_assigned[3])
    x = x * (getSpeed(elev) + getFloorTime(elev))
    return elev.last_assigned[1] + x < call[1]  # return last call time + arrival time < current call


@classmethod
def isOnTheWay(cls, floor: int, floor2: int, elev: elevator):
    return False


@classmethod
def getTimeToDest(cls, elev: elevator):
    return distanceAsTimeFromElev(elev, elev.last_assigned[2]) * (getSpeed(elev) + getFloorTime(elev))


def getSpeed(elev: elevator):
    return elev.speed


def getFloorTime(elev: elevator):
    return elev.closeTime + elev.openTime + elev.startTime + elev.stopTime


# TODO:
def closestIdle(src):
    return None


def closestOnTheWay(src):
    return None


def closestBusy(src):
    return None


def arriveTimeOnWay(on_way, src):
    return None


def arriveTimeIdle(on_way, src):
    return None


def arriveTimeBusy(busy, src):
    return None