"""
@authors: "Shaked & Yonathan"
date: Nov 9
"""
import Building
import elevator

'''

Algorithm input examples :

    1. Calls.csv: Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv
    2. Building.json: Ex1/data/Ex1_input/Ex1_Buildings/B1.json - contains Elevator info
    3. Output.csv: to be filled by us 

Algorithm output examples Elevator: 

    1. Ex1/data/Ex1_Calls_case_2_.csv

# TODO: collect input from cmd - to be explained later by staff

'''
# LOADING THE CSV FILE :
file_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv"
dict_calls = []
dict_calls = Building.Building.init_calls(file_loc2=file_in)
# print(dict_calls)
# print(dict_calls[0][1])  # time access
# print(dict_calls[0][2])  # src access
# print(dict_calls[0][3])  # destination access
# print(dict_calls[0][4])  # state access

# LOADING THE JSON FILE : working example
file2_in = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Buildings\B2.json"
dict_b = Building.Building.init_dict(file_loc1=file2_in)
print(dict_b.elevators[1].__dict__)
# print(dict_b.elevators[1].speed)

x = elevator.Elevator(dict_b.elevators[1].id, dict_b.elevators[1].speed, dict_b.elevators[1].minFloor,
                      dict_b.elevators[1].maxFloor, dict_b.elevators[1].closeTime, dict_b.elevators[1].openTime,
                      dict_b.elevators[1].startTime, dict_b.elevators[
                          1].stopTime)  # elevator creation, need to create as many as we want, can use list? :)
