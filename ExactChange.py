# Program name: ExactChange.py
# Author: Elijah Batchelor
# Date: 2/14/2026
# Program description: This program receives an input from user of money amount
#                      then this program uses if-else statements to give exact change
#                      while giving the fewest coins in return

change_amount = int(input())

if(change_amount == 0):
    print("No change")
if(change_amount >= 100):
    dollar = change_amount // 100
    if(dollar > 1):
        print(f"{dollar} Dollars")
    else:
        print(f"{dollar} Dollar")

change_amount = change_amount % 100

if(change_amount >= 25):
    quarter = change_amount // 25
    if(quarter > 1):
        print(f"{quarter} Quarters")
    else:
        print(f"{quarter} Quarter")

change_amount = change_amount % 25

if(change_amount >= 10):
    dime = change_amount // 10
    if(dime > 1):
        print(f"{dime} Dimes")
    else:
        print(f"{dime} Dime")

change_amount = change_amount % 10

if(change_amount >= 5):
    nickel = change_amount // 5
    if(nickel > 1):
        print(f"{nickel} Nickels")
    else:
        print(f"{nickel} Nickel")

change_amount = change_amount % 5

if(change_amount < 5 and change_amount != 0):
    penny = change_amount // 1
    if(penny > 1):
        print(f"{penny} Pennies")
    else:
        print(f"{penny} Penny")


# Challenges and thought process:
# Some of the challenges that I ran into in the beginning was trying to figure out
# how to seperate the quotient of the change and the remainder of the change at first
# for some reason I was thinking that you would have to set the change_amount to the 
# value of the quarters, dimes, nickel etc. I did not think that I can set the quotient
# to the value of dollar, quarter, dime etc. I orginally thought that I needed to initialize
# the value of each part of the change. But I did not since I can just divide by the coin value.
# Once I realized that you can just set the coin to the value of the quotient it was smooth
# sledding from there. Just had to make a nested if-else statement to return a singular value or
# plural value of coins.