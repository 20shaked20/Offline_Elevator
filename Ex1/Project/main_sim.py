"""
@authors: "Shaked & Yonathan"
date: Nov 9
"""
import threading
import csv

"""
this is a timer thread test learning
"""

file_calls = "D:\Programming\Python\Offline_Elevator\Ex1\data\Ex1_input\Ex1_Calls\Calls_a.csv"
dict_calls = []
with open(file_calls, "r") as f:
    calls = csv.reader(f)
    for row in calls:
        dict_calls.append(row)


def calls_timer():
    i = 0
    first_call = dict_calls[0][1]  # first known call time
    last_call = dict_calls[len(dict_calls) - 1][1]  # last known call time
    for row in dict_calls:
        print(dict_calls[i][1])
        i += 1


timer = threading.Timer(0.5, calls_timer())
timer.start()
print("Exit\n")

print(dict_calls[len(dict_calls) - 1][1])
