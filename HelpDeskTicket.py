# Program name: HelpDeskTicket.py
# Author: Elijah Batchelor
# Date: 2/15/2026
# Program description: This program represents a helpdesk ticket system. We get our input
#                      then we process that information through if-else statements. We then
#                      set each ticket a priorty level only if there is a keyword that is used
#                      in the message sent from user. Then a menu will display an option menu

import math

# Get inputs
room_temp = input("Enter temperature: ")
room_temp = room_temp.strip() # get rid of empty space in string

flt_temp = float(room_temp) # changes string to float value

location = input("Enter location: ")
location = location.strip() # gets rid of empty space in string

message = input("Enter a brief description: ")
message = message.strip() # gets rid of empty space in string

if message == "":
    print("Error: Helpdesk message cannot be empty.")
    exit() # if statement to check if message is empty then ends the program

# validation of entry
issue = input("Does this issue affect a class right now? y or n? ")
issue = issue.strip().lower()
if issue not in ("y", "n"):
    print("Invalid input.")
    exit() # if statement to check if y or n was answered and if not then ends program

hours = input("Is this after hours? y or n? ")
hours = hours.strip().lower()
if hours not in ("y", "n"):
    print("Invalid input.")
    exit() # if statement to check if y or n was answered and if not then ends program

# Normalizing message
normal_message = message.lower() # setting message to lower case

# If-else statement to check for key words and setting normal_message to a category
if any(word in normal_message for word in ["fire", "smoke", "gas", "injury", "threat"]):
    category = "Safety"
elif any(word in normal_message for word in ["wifi", "login", "password", "canvas", "printer"]):
    category = "IT"
elif any(word in normal_message for word in ["heat", "ac", "temperature", "hot", "cold", "broken"]):
    category = "Facilities"
else:
    category = "General"

# Temperature assessment
temp_assessment = "N/A"

# If statement first to check if we are in Facilities category
# second if-else statement to check temperature
if category == "Facilities":
    if math.isclose(flt_temp, 22.0, abs_tol=0.25):
        temp_assessment = "Normal" # using math.isclose() to prevent binary number return for float value. Ranges from 21.75 and 22.25
    elif flt_temp <= 18.0:
        temp_assessment = "Too cold" # checks if anything under 18.0 and returns too cold
    elif flt_temp >= 26.0:
        temp_assessment = "Too hot" # checks if anything above 26.0 and returns too hot
    else:
        temp_assessment = "Slightly off" # returns if there is any value between 18.0 - 21.75 and 22.25 - 26.0

# Priorty Logic
# If-else statement that runs through priority of safety, facilities and IT
if category == "Safety":
    priority = "P1"

elif category == "Facilities":
    if flt_temp <= 18.0 or flt_temp >= 26.0:
        priority = "P1"
    elif issue == "y":
        priority = "P2"
    else:
        priority = "P3"

elif category == "IT":
    if issue == "y" and ("wifi" in normal_message or "canvas" in normal_message):
        priority = "P2"
    else:
        priority = "P3"

else:
    priority = "P3"

# Menu

print("=== Helpdesk Ticket Menu ===")
print("1. View normalized ticket text")
print("2. View detected category")
print("3. View temperature assessment")
print("4. View final ticket priority")

choice = input("Enter choice (1-4): ").strip() # choice variable to pick between 1-4

if choice == "1":
    print(normal_message)

elif choice == "2":
    print(f"Location: {location}")
    print(f"Category: {category}")

elif choice == "3":
    print(f"Temperature assessment: {temp_assessment}")

elif choice == "4":
    print(f"Location: {location}")
    print(f"Category: {category}")
    print(f"Priority: {priority}")

else:
    print("Invalid menu option.")
