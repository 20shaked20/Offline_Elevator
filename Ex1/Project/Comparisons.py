"""
@authors: "Shaked & Yonatan"
date: Nov 12
"""
# import Building
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
    return distanceFromElev(elev, floor) / getSpeed(elev) + getFloorTime(elev)


def getLastCall(elev: elevator):
    return elev.last_assigned  # return tuple in the form: (time,src,dest)


def isIdle(elev: elevator, call):
    x = floorDiff(elev.last_assigned[2], elev.last_assigned[3])
    x = x / getSpeed(elev) + getFloorTime(elev)
    if float(elev.last_assigned[1]) + x <= float(call[1]):
        elev.elev_state = 0
        return True
    else:
        return False
    # return last call time + arrival time < current call


def getTimeToDest(elev: elevator):
    return distanceAsTimeFromElev(elev, elev.last_assigned[2]) / getSpeed(elev) + getFloorTime(elev)


def getCurr(elev: elevator, call):
    """
    this function returns the theoretical location of the elevator, based on the current call's time
    and the previous calls time.
    :param elev: the elevator for which this calculation is done
    :param call: the current call that is being evaluated
    :return: floors passed since last assigned call and current call (which is being evaluated)
    """
    if isIdle(elev, call):
        return elev.elev_pos
    time_diff = float(call[1]) - float(elev.last_assigned[1])
    x = time_diff / getSpeed(elev)
    return int(elev.last_assigned[2]) + int(x + elev.closeTime + elev.startTime)
    # TODO: consider using x + elev.close_time + elev.start_time


def getTimeFromCurr(elev: elevator, floor: int, call):
    curr = getCurr(elev, call)
    floors = floorDiff(curr, floor)
    return floors / getSpeed(elev) + getFloorTime(elev)


def getSpeed(elev: elevator):
    return elev.speed


def getFloorTime(elev: elevator):
    return elev.closeTime + elev.openTime + elev.startTime + elev.stopTime


def isOnWay(elev, call):
    if isIdle(elev, call):
        return False
    call_dir = getDirection(call)
    elev_dir = elev.elev_state
    if elev_dir != call_dir:
        return False
    curr = getCurr(elev, call)
    if call_dir == 1:
        if curr > call[2]:
            return False
    if call_dir == -1:
        if curr < call[2]:
            return False
    return True


def getDirection(call):
    if call[2] < call[3]:
        return 1
    else:
        return -1


def theoreticalTime(elev: elevator, floor1: int, floor2: int):
    """
    calculates time that would take elev to move from floor1 to floor 2
    :param elev: elevator for which calculation is done
    :param floor1: floor represented as an int
    :param floor2: floor represented as an int
    :return: time in double
    """
    floors = floorDiff(floor1, floor2)
    return floors / getSpeed(elev) + getFloorTime(elev)


def closestIdle(call, all_elev):
    closest: elevator = all_elev[0]
    changed = False
    for elev in all_elev:
        if isIdle(elev, call):
            time_elev = arriveTimeIdle(elev, call)
            time_closest = arriveTimeIdle(closest, call)
            if time_elev < time_closest:
                closest = elev
                changed = True
    if changed is False:
        if isIdle(closest, call) is False:
            return False
    return closest


def closestOnTheWay(call, all_elev):
    closest: elevator = all_elev[0]
    changed = False
    for elev in all_elev:
        if isOnWay(elev, call):
            if arriveTimeOnWay(elev, call) < arriveTimeOnWay(closest, call):
                closest = elev
                changed = True
    if changed is False:
        if isOnWay(closest, call) is False:
            return False
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
    return getTimeFromCurr(elev, call[2], call)


# time from curr if applicable
def arriveTimeIdle(elev, call):
    return theoreticalTime(elev, elev.elev_pos, call[2])


# time from current to dest then from dest to src
def arriveTimeBusy(elev, call):
    return getTimeFromCurr(elev, elev.last_assigned[3], call) + theoreticalTime(elev, elev.last_assigned[3],
                                                                                call[2])
