
################################################################################################
# Problem 5
# Coffee
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
################################################################################################
""" 
Find all students who include a kind of coffee in their beverages 
Print the result as a list of strings "First Last (beverage)"
Idea is similar to tea, for "coffee" or "espresso" or "brew" or "mocha"
"""

# Do you want a helper function for coffee, like you had for tea? 
# Write one here

# created a helper function
def coffee(beverage):
    beverage = beverage.lower()             
    return "coffee" in beverage or "mocha" in beverage or "brew" in beverage or "espresso" in beverage

# -- Write your code here ---
lst = []
for student in all_student_data:
    # if coffee contains student's favorite beverage lowercased, append their first name, last name, and favorite beverage.
    if coffee(student[INDEX_BEVERAGE].lower()):
        lst.append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_BEVERAGE]})")
        pass
print(lst)

################################################################################################
# Problem 5 COMPLETE
################################################################################################