"""
@authors: "Shaked & Yonatan"
date: Nov 5
"""


class Elevator(object):

    def __init__(self, _id: int, _speed: int, _minFloor: int, _maxFloor: int, _closeTime: int, _openTime: int,
                 _startTime: int, _stopTime: int) -> None:
        """
        :param _id: the id of the elevator
        :param _speed: the speed of the elevator
        :param _minFloor: minimum floor elevator can reach
        :param _maxFloor: maximum floor elevator can reach
        :param _close_time: how long it takes for elevator to close doors
        :param _open_time: how long it takes for elevator to open doors
        :param _start_time: how long it takes the elevator to start moving from idle state
        :param _stop_time: how long it takes the elevator to stop from moving state
        """
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime
        self.elev_pos = 0
        self.elev_state = 0  # last relevant direction
        self.last_assigned = "elev_call", "0.0", "0", "0"  # last assigned call
        # self.prev_assigned = "elev_call", "0.0", "0", "0"
        # second last assigned call, currently not used in the algorithm.

    @classmethod
    def from_dict(cls, data_dict):
        """
        :param data_dict: gets an elevator dictionary from Building.py
        :return: returns the data as an object (elevator)
        """
        return cls(**data_dict)

    def go_to(self, new_pos):
        """
        this method simply tells the elevator where to go next. i'e will be used to check positions.
        :param new_pos: Integer representing a floor the elevator to go.
        """
        self.elev_pos = new_pos

    def set_state(self, new_state):
        """
        Right now im not sure this will be useful, im just implementing in case of need.
        :param new_state: gets the new state for our elevator
        """
        self.elev_state = new_state
