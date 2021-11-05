"""
@authors: "Shaked & Yonathan"
date: Nov 5
"""

import json
import csv

'''
Algorithm input examples :

    1. Calls.csv: Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv
    2. Building.json: Ex1/data/Ex1_input/Ex1_Buildings/B1.json - contains Elevator info
    3. Output.csv: to be filled by us 

Algorithm output examples Elevator: 

    1. Ex1/data/Ex1_Calls_case_2_.csv

# TODO: collect input from cmd - to be explained later by staff

'''
# READING AND WRITING THE ELEVATOR ROUTE TO OUTPUT :
file_in = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv"
file_out = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/Calls_x.csv"
routes = "/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Calls/route.csv"

dict_in = []
dict_route = []
with open(file_in, 'r') as f:
    bla = csv.reader(f)
    for row in bla:
        dict_in.append(row)

with open(routes, 'r') as f2:
    bla2 = csv.reader(f2)
    for row in bla2:
        x = row[0]  # i don't want list.
        print(x)
        dict_route.append(x)

print(dict_route)
print(dict_in)
i = 0
for row in dict_in:
    x = dict_route[i]
    dict_in[i][5] = dict_route[i]  # places the right elevator.. :D
    i += 1
print(dict_in)

with open(file_out, 'w') as f3:
    bla3 = csv.writer(f3)
    for row in dict_in:
        bla3.writerow(row)


# JSON:
# f = open("/Users/Shaked/PycharmProjects/Offline_Elevator/Ex1/data/Ex1_input/Ex1_Buildings/B1.json")
