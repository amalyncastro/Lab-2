
################################################################################################
# Problem 4
# Tea
################################################################################################
import filereader  
from constants import *

# Get student data
data_path = "cs150data-w24.tsv"
data = filereader.read_data(data_path)
questions = data[0] # The questions are the first row of data
all_student_data = data[1:] # We can get just get the students by taking a slice


################################################################################################
# Question
################################################################################################
""" 
Find all students who include "tea" or "chai" in their beverages 
Print the result as a list of strings "First Last"

 
Create an empty list
Iterate through each student
If they like tea, 
        make a string containing their first and last names, and their beverage in parentheses in the format
                f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})"
        "append" that string to the list
print the list
"""

# A helper function: turns a beverage string into True/False
# Its imperfect, but don't improve it for now!
def is_tea(beverage):
        beverage = beverage.upper()             
        return "CHAI" in beverage or "TEA" in beverage

# -- Write your code here ---
# bev is an empty list
bev = []
for student in all_student_data:
        # if is_tea contains student's beverage data uppercased, append their first name, last name, and their favorite beverage
        if is_tea(student[INDEX_BEVERAGE].upper()):
                bev.append((f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})"))
        pass
# print list f students who include "tea" or "chai" in their beverages
print(bev)

################################################################################################
# Problem 4 COMPLETE
################################################################################################