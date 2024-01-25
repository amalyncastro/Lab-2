
################################################################################################
# Problem 9
# Your own question 
################################################################################################
import filereader  
from constants import *

# Get student data
data_path = "cs150data-w24.tsv"
data = filereader.read_data(data_path)
questions = data[0] 
all_student_data = data[1:] 

################################################################################################
# Question
# Formulate your own non-trivial question about these data, write it in the comments
# Then write a progam to answer it
# The program should use list and/or dictionary where appropriate
################################################################################################

""" 
Find all students who include "boba" in their beverages 
Print the result as a list of strings "First Last"

Create an empty list
Iterate through each student
If they like "boba" (specifically), 
        make a string containing their first and last names, and their beverage in parentheses in the format
                f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})"
        "append" that string to the list
print the list

Skip any student with an empty value ("") and not being boba.
"""

# empty list
bobalist = []

# helper function that lowercases for us
def boba(x):
    lower = x.lower()             
    return "boba" in x

# set valid list of characters
valid = {"b", "o", "b", "a"}

# iterate through all data
for student in all_student_data:

# set variable to hold beverage in all lowercased
    drinks = student[INDEX_BEVERAGE].lower()

# remove empty lists and any data that doesn't match with boba
    if drinks == "":
        continue

# if it does contain boba, append it into the list
    if boba(drinks):  
        bobalist.append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})")

# print boba list
print(bobalist)

# tests i did
'''
# if it's a different kind of boba, append it into a different section in the dictionary
    if drinks not in diffboba:
         diffboba[drinks] = []

    if any(char in valid for char in drinks):
        diffboba[drinks]

        or any(char not in valid for char in drinks
'''