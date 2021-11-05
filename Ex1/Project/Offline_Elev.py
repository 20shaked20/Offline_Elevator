import json

'''
Algorithm input examples :

    1. Calls.csv: Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv
    2. Building.json: Ex1/data/Ex1_input/Ex1_Buildings/B1.json - contains Elevator info
    3. Output.csv: to be filled by us 

Algorithm output examples Elevator: 

    1. Ex1/data/Ex1_Calls_case_2_.csv

# TODO: collect input from cmd - to be explained later by staff

'''

f = open("/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B1.json")
B1 = json.load(f)

_minFloor = B1["_minFloor"]
_maxFloor = B1["_maxFloor"]
_elevator = B1["_elevators"][0]["_id"]
print(_minFloor)
print(_maxFloor)
print(_elevator)

f.close()

