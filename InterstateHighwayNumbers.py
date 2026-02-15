# Program name: InterstateHighwayNumbers.py
# Author: Elijah Batchelor
# Date: 2/14/2026
# Program description: This program takes an input of an possible interstate number.
#                      It will tell you if the interstate number goes from north to south,
#                      east to west. Any number above 100 will show you an auxiliary of the
#                      interstate. Any numbers that end with 00 is not a valid interstate number

highway_number = int(input())

if(highway_number == 0):
    print("0 is not a valid interstate highway number.")
if(highway_number > 0 and highway_number < 100):
    interstate = highway_number % 2
    if(interstate == 0):
        print(f"I-{highway_number} is primary, going east/west.")
    else:
        print(f"I-{highway_number} is primary, going north/south.")

if(highway_number >= 100 and highway_number <= 999):
    auxiliary = highway_number % 100
    interstate = highway_number % 2
    if(auxiliary == 0):
        print(f"{highway_number} is not a valid interstate highway number.")
    elif(interstate == 0):
        print(f"I-{highway_number} is auxiliary, serving I-{auxiliary}, going east/west.")
    else:
        print(f"I-{highway_number} is auxiliary, serving I-{auxiliary}, going north/south.")

if(highway_number >= 1000):
    print(f"{highway_number} is not a valid interstate highway number.")


# Challenges and thought process:
# This is similar to the ExactChange.py program. Just had to think about how to get 
# the auxiliary and interstate to show up in the same block of code. Had to add 
# the interstate variable to the auxiliary part of the code. Which then allowed me 
# to be able to provide odd or even numbers.
