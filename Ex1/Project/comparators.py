"""
@authors: "Shaked & Yonathan"
date: Nov 9
"""
import sys


class Comparators:

    @classmethod
    def in_route(cls, call, curr_elevator):
        """
        this method finds if a certain call is on_route for our current elevator call.
        :param call: a single call (s,d,time..)
        :param curr_elevator: elevator for which this is calculated
        :return: True/False depends if its on route or not.
        """
        src = int(call[2])
        destination = int(call[3])

        if Comparators.src_in_route(call, curr_elevator):
            if curr_elevator.elev_des < destination:  # if the new destination is smaller, then update it
                curr_elevator.set_des(destination)
            curr_elevator.go_to(src)  # send it to next src then.

    @classmethod
    def src_in_route(cls, call, curr_elevator):
        """
        checks whether src of a call is in elevator route
        :param call: current call
        :param curr_elevator: elevator for which this is calculated
        :return: True or False
        """
        src = int(call[2])
        call_dir = Comparators.get_call_dir(call)
        if call_dir == 1:
            return curr_elevator.elev_pos < src < curr_elevator.elev_des
        else:  # assumes dir is 1 or -1 for UP or DOWN
            return curr_elevator.elev_pos > src > curr_elevator.elev_des

    @classmethod
    def get_call_dir(cls, call):
        """
        returns current call direction based on call source and destination
        :param call: current call
        :return: 1 or -1 representing UP or DOWN respectively
        """
        if call[2] < call[3]:
            return 1
        else:
            return -1

    @classmethod
    def get_elev_dir(cls, curr_elevator):
        """
        returns current elevator direction based on call source and destination
        :param curr_elevator: elevator for which this is calculated
        :return: 1 or -1 representing UP or DOWN respectively
        """
        if curr_elevator.elev_pos < curr_elevator.elev_des:
            return 1
        else:
            return -1

    @classmethod
    def best_time_to_src(cls, call, all_elevators):
        """
        This method finds the best elevator in the building to reach a destination floor in given time.
        :param call: a single call (s,d,time..)
        :param all_elevators: all elevators in the building
        :return: best time to source elevator id
        """
        destination = int(call[3])
        best_time = sys.maxsize
        elev_id = 0
        for curr_elev in all_elevators:
            floor_time = curr_elev.openTime + curr_elev.stopTime + curr_elev.closeTime + curr_elev.startTime
            floor_size = abs(curr_elev.elev_pos - destination)
            if best_time > floor_size / curr_elev.speed + floor_time:
                best_time = floor_size / curr_elev.speed + floor_time
                elev_id = curr_elev.id

        return elev_id

    @classmethod
    def best_elev(cls, call, all_elevators):
        """
        This method gets a call, all elevators and checks which is the best elevator using the methods above
        :param call: a single call (s,d,time..)
        :param all_elevators: all elevators in the building
        :return: id of the best elevator.
        """

        best_time = Comparators.best_time_to_src(call, all_elevators)
        return best_time


# UNUSED METHODS:
"""

    @classmethod
    def find_closest(cls, call, all_elevators):
        
        This method finds the closest elevator to a src, regardless of it's current destination
        :param call: object representing a call
        :param all_elevators: all the elevators that are in the building
        :return:  ID of the closest elevator.
        
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
"""
