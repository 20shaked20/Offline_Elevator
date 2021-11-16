"""
@authors: "Shaked & Yonathan"
date: Nov 9
"""
import sys

"""
comparators class:
"""


class Comparators:

    @classmethod
    def find_closest(cls, call, all_elevators):
        """
        This method finds the closest elevator to a src.
        :param call: object representing a call
        :param all_elevators: all the elevators that are in the building
        :return:  ID of the closest elevator.
        """
        src = int(call[2])
        destination = int(call[3])
        closest = all_elevators[0]
        best_dist = all_elevators[0].elev_pos - src
        for curr_elevator in all_elevators:
            if curr_elevator.elev_pos - src < best_dist:
                best_dist = curr_elevator.elev_pos - src
                closest = curr_elevator
        closest.set_des(destination)
        closest.go_to(src)  # sends the elevator to src. /5
        return closest.id

    @classmethod
    def in_route(cls, call, curr_elevator):
        """
        this method finds if a certain call is on_route for our current elevator call.
        :param call: a single call (s,d,time..)
        :param all_elevators: all elevators in the building
        :return: True/False depends if its on route or not.
        """
        src = int(call[2])
        destination = int(call[3])
        if curr_elevator.elev_pos < src and curr_elevator.elev_des < src:  # is between pos to destination
            if curr_elevator.elev_des < destination:  # if the new destination is smaller, then update it
                curr_elevator.set_des(destination)
            curr_elevator.go_to(src)  # send it to next src then.

    @classmethod
    def best_time_to_src(cls, call, all_elevators):
        """
        This method finds the best elevator in the building to reach a destination floor in given time.
        :param call: a single call (s,d,time..)
        :param all_elevators: all elevators in the building
        :return: best time to source elevator id
        """
        destination = int(call[3])
        total_time = 0
        id = 0
        for curr_elev in all_elevators:
            length = curr_elev.elev_pos - destination
            if total_time > length / curr_elev.speed + curr_elev.stopTime + curr_elev.startTime:
                total_time = length / curr_elev.speed + curr_elev.stopTime + curr_elev.startTime
                id = curr_elev.id

        return id

    @classmethod
    def best_elev(cls, call, all_elevators):
        """
        This method gets a call, all elevators and checks which is the best elevator using the methods above
        :param call: a single call (s,d,time..)
        :param all_elevators: all elevators in the building
        :return: id of the best elevator.
        """

        closest = Comparators.find_closest(call, all_elevators)
        best_time = Comparators.best_time_to_src(call, all_elevators)
        if closest == best_time:
            return closest  # is the same.
        else:
            return best_time
