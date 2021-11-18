# Offline_Elevator - assignment[1]

> Made by Shaked Levi And Yonatan Ratner.

>Shaked's github https://github.com/20shaked20
>
>Yonatan's github: https://github.com/Teklar223

### Introduction
This repository is part of an assigment in an object oriented programming course at Ariel University,
Specifically the second assignment, and it is about an offline algorithm for smart elevators.

## Offline algorithm for elevator calls:
### Inputs: Calls.csv Building.json output.csv 

 - Calls.csv is a Comma Seperated Values file that contains all the calls in the building, in this format:
  ![image](https://user-images.githubusercontent.com/73063105/142376901-7b3473e9-dfc9-4f1d-ad1d-d3daea47d675.png) </br>
  where the first column is any string (does NOT have to be "Elevator call"), the 2nd is time of call, 3rd is source and 4th is destination
  the 5th column is call state, but its not implemented so just 0 is fine, and the 6th is the assigned elevator (currently -1 as a null object) </br>
- Building.json contains all the information of a building, how many floors and what elevators, in this format:
  ![image](https://user-images.githubusercontent.com/73063105/142377378-9f7b5965-0242-4557-a80b-7914f5a6ae49.png) </br>
  (naturally you can have several elevators) </br>
- output.csv is the file that the program writes onto 
  </br>
### Output: Output.csv

  - Output.csv is nearly identical to the input of Calls.csv with the only difference being in the 6th column,
    where all the numbers are at least 0 and they all represent the assigned elevator id's (each call has it's own assigned elevator) </br>
    
### Algorithm assumptions:
  - the previous call assignment to each elevator is the best one.
  - each elevator knows it's last assigned call and can tell what state it currently is based on this and the current call
  - the Building info and Calls are constants, such that their values do no change dynamically during runtime

### The cases:
  1. there are idle elevator's
  2. there are elevator's that can pick the caller on their way to their current destination
  3. there are 'busy' elevators that are'nt on the way to the caller </br>

this essentially describes all the relative positions of the elevator in regards to the current call source (there may be more, but we could not think of any relevant ones) </br>

### The algorithm:
  1. get the idle elevator that arrives fastest to the call source
  2. get the fastest to arrive elevator that the call source is in it's way
  3. get the fastest to arrive elevator that will finish it's current task and then arrive to the call source
  4. compare cases 1,2,3 against each other and assign the call to the fastest elevator to arrive to its source
  5. repeat for next call until done. </br>
  
## How to use?

  Firstly, the inputs must be specified, there are 5 building json files and 4 calls csv files provided, so currently there are 20 possible scenarios which can be run,
  and these should be specified in the Offline_Elev.py file, highlighted in red in these lines: </br>
  ![image](https://user-images.githubusercontent.com/73063105/142407895-6cb3ba59-4ebe-45eb-85b1-74f4e5164ffa.png)
 </br>
  in the image we highlighted which files are the inputs (yes, including the output.csv) which are passed along the algorithm, the files paths are relative to the Offline_elev.py file and are taken from the Ex1_input folder, we suggest that if you wish to play around with the algorithm that you first rummage this folder and have a look at the calls and buildings folders (see file Hierarchy section towards the end)
  </br>
  Alongside the assignment, a simulator is provided, after you run the algorithm with the desired building and calls combination, access the folder that the Ex1_checker_V1.2_obf.jar is located in: </br>
  ![image](https://user-images.githubusercontent.com/73063105/142407102-bae18dd4-947d-4611-b337-57b42d15e3f8.png) </br>
  this .jar file must have in the same directory both the calls.csv, output.csv and building.json files that you wish to simulate with the output that was generated from their specific combination. </br>
* NOTE: the output is saved into the testing folder!!!

### Testing
* We havent done any tests for our comparison functions, seeing as they are purely mathematical in nature, we simply checked them rigourously by hand. </br>
* As for the algorithm as a whole, it is possible to create a calls_test.csv file that will simulate a pre-meditated scenario in which we know the best elevator for every situation and check that the algorithm assigns it correctly, naturally we can also make our own building.json for the scenario

## Lessons Learned
we feel that we did decent work, hence our improvements are striving towards perfection, in areas where improvement is 'not necessary' but certaintly possible. </br>
#### Things to improve
- advanced git usage
- better commenting

#### things to keep
- good source control
- room for seperate thinking, which reduced cluttered code and improved workflow significantly
- taking care of the "dirty work" before approaching the algorithm itself, e.g: input/outut was taken care of before any code was written in the algorithm itself, this allowed us to switch our focus entirely on the algorithm once these things were done.

## File Hierarchy
![image](https://user-images.githubusercontent.com/73063105/142406389-3b342c81-0874-453e-86d6-9f61eecfcb73.png)
</br>

## External info:
- More about online offline algorithms : https://en.wikipedia.org/wiki/Online_algorithm
- More about Elevator Scheduling : https://github.com/00111000/Elevator-Scheduling-Simulator/blob/master/research-papers/Context-Aware-Elevator-Scheduling.pdf
- More about Smart Elevators : https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
- See Also                   : https://www.npr.org/templates/story/story.php?storyId=6799860
