# Program name: ProfessorTestManager.py
# Author: Elijah Batchelor
# Date: 1/28/2026
# Program description:
#       This program is intended to receive student name and test score.
#       Once test score is received it is calculated and averaged out between the 
#       three test score. Once that is calculated then it display the average score
#       and displays the student name with a random number between 23 and 2024.
#       With a goodbye message.
# Input:
#       Student names and test grades
#
# Output:
#       Average of test score, Student name and random number generated with it
#       and other printed messages


import random
import string

print("******Professor's Test Management Program******")
# Enter students name
print("Enter the student's name: ", end="")
student_name = input()

# Enter all three exam scores
print("Enter test 1 score : ", end="")
test1 = int(input())
print("Enter test 2 score : ", end="")
test2 = int(input())
print("Enter test 3 score : ", end="")
test3 = int(input())

# Calculate the average of test score
average = (test1 + test2 + test3) / 3

# Display student info
print("---Student report---")
print("Average Exam Score: ", f"{average:.5f}")
print("Student Identifier: ", end="")
print(student_name, end="")
print(random.randrange(23, 2025))
# Generate random number between 23 and 2024
rand = random.randrange(23, 2025)
print(f"Student Identifier: {student_name}{rand}")
print(f"Student Identifier: {student_name}{random.randrange(23,2025)}")
print("Results saved for Professor’s recordkeeping. Have a great day grading!")

# Output:
# ******Professor's Test Management Program******
# Enter the student's name: Elijah
# Enter test 1 score : 73.6
# Enter test 2 score : 84.6
# Enter test 3 score : 89.8
# ---Student report---
# Average Exam Score:  82.66667
# Student Identifier: Elijah1020
# Results saved for Professor’s recordkeeping. Have a great day grading!