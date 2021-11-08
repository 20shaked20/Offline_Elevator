"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""

elev_pos = 0
elev_state = 0  # 0  = idle, 1 = UP , -1 = DOWN


class Elevator(object):

    def __init__(self, _id: int, _speed: int, _minFloor: int, _maxFloor: int, _closeTime: int, _openTime: int,
                 _startTime: int, _stopTime: int) -> object:
        """
        :param _id: the id of the elevator
        :param _speed: the speed of the elevator
        :param _minFloor: minimum floor elevator can reach
        :param _maxFloor: maximum floor elevator can reach
        :param _closeTime: how long it takes for elevator to close doors
        :param _openTime: how long it takes for elevator to open doors
        :param _startTime: how long it takes the elevator to start moving from idle state
        :param _stopTime: how long it takes the elevator to stop from moving state
        """
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime

    @classmethod
    def from_dict(cls, data_dict):
        """
        :param data_dict: gets an elevator dictionary from Building.py
        :return: returns the data as an object (elevator)
        """
        return cls(**data_dict)

    @staticmethod
    def go_to(new_pos):
        """
        this method simply tells the elevator where to go next. i'e will be used to check positions.
        :param new_pos: Integer representing a floor the elevator to go.
        """
        global elev_pos
        elev_pos = new_pos

    @staticmethod
    def get_pos():
        """
        :return: the elevator current position.
        """
        return elev_pos

    @staticmethod
    def set_state(new_state):
        """
        Right now im not sure this will be useful, im just implementing in case of need.
        :param new_state: gets the new state for our elevator
        """
        global elev_state
        elev_state = new_state

    @staticmethod
    def get_state():
        """
        :return: the elevator current state -> 0 IDLE, 1 UP , -1 DOWN
        """
        return elev_state
