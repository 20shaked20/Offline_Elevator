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
    def find_closest(cls, src: int, all_elevators):
        """
        This method finds the closest elevator to a src.
        :param src: Integer representing a source floor
        :param all_elevators: all the elevators that are in the building
        :return:  ID of the closest elevator.
        """
        closest = all_elevators[0]
        best_dist = all_elevators[0].elev_pos - src
        for curr_elevator in all_elevators:
            if curr_elevator.elev_pos - src < best_dist:
                best_dist = curr_elevator.elev_pos - src
                closest = curr_elevator
        return closest.id

    @classmethod
    def on_route(cls, src: int, dest: int, curr_elev):
        """
        Gets a src and checks if its already on the route of the elevator, so it can pick him.
        :param dest: Integer representing a destination floor
        :param src: Integer representing a source floor
        :param curr_elev: the elev we're using right now.
        :return: true for in route, false for not in route.
        """
        # elev is up and src is on way
        if curr_elev.elev_pos < src and src < dest:  # and curr_elev.elev_state == 1:
            return True

        # elev down and didn't pass src floor
        if curr_elev.elev_pos > src and src > dest:  # and curr_elev.elev_state == -1:
            return True

            # is idle then available.
        if curr_elev.elev_state == 0:
            return True

        return False

    @classmethod
    def time_to_src(cls, src: int, curr_elev):
        """
        Gets a src and elev, checks how long it will take the elev to reach that src.
        :param src: a source floor
        :param curr_elev: current elevator in motion.
        :return:
        """
        dist_from_src = curr_elev.elev_pos - src
        total_time = curr_elev.stopTime  # first thing we consider hence it will stop anyway.

        if curr_elev.elev_state == 0:  # elev is idle
            total_time += curr_elev.startTime

        if curr_elev.elev_state == -1 or curr_elev.elev_state == 1:  # elev is up or down
            total_time += curr_elev.stopTime + curr_elev.startTime

        return (dist_from_src / curr_elev.speed) + total_time

    @classmethod
    def best_elev(cls, call, all_elevators):
        """
        This method gets a call and all elevators in the buildings and finds the most optimal one to send to our user.
        :param call: a call
        :param all_elevators: list of all elevators
        :return: id of best elevator.
        """
        best_elev_id = -1
        best_time_to_src = sys.maxsize  # max value there is.
        curr_elev = all_elevators[0]
        curr_time_to_src = 0
        i = 0
        src = int(call[2])
        destination = int(call[3])

        for elevator in all_elevators:  # best case
            curr_elev = all_elevators[i]
            curr_time_to_src = cls.time_to_src(src, curr_elev)
            if curr_time_to_src < best_time_to_src and cls.on_route(src, destination, curr_elev):
                best_elev_id = i
                best_time_to_src = curr_time_to_src
            i += 1

        i = 0  # reset i after first loop

        if best_elev_id == -1:  # if above case didn't happen
            for elevator in all_elevators:
                curr_elev = all_elevators[i]
                curr_time_to_src = cls.time_to_src(src, curr_elev)
                if curr_time_to_src < best_time_to_src:
                    best_elev_id = i
                    best_time_to_src = curr_time_to_src
                i += 1
        return best_elev_id
