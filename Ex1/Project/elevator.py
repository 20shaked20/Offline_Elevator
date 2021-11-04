__author__ = "Shaked & Yonathan"

import json


class Elevator:

    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        '''
        :param _id: the id of the elevator
        :param _speed: the speed of the elevator
        :param _minFloor: minimum floor elevator can reach
        :param _maxFloor: maximum floor elevator can reach
        :param _closeTime: how long it takes for elevator to close doors
        :param _openTime: how long it takes for elevator to open doors
        :param _startTime: how long it takes the elevator to start moving from idle state
        :param _stopTime: how long it takes the elevator to stop from moving state
        '''
