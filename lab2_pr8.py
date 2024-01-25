
################################################################################################
# Problem 8
# Birthday buddies
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
Find all the birthday buddies (pairs with same birthday) in class
Create a dictionary with date (in mm/dd format) being a key
and a list of people who share the birthday as a value.
Each entry in the value list is in "FirstName LastName" format.
(For the grading purpose, assume that the person that appears earlier in the data
spreadsheet will also appear earlier in the list.)

Print that dictionary.

Skip any student with a missing birthday.
"""

# dictionary, buddies
buddies = {}
# -- your code here --
for student in all_student_data:
       # bday set to student's birthdays
       bday = student[INDEX_BIRTHDAY]

       # key in mm/dd format
       key = bday[:5]
       
       # skip any students with empty strings or birthdays written in characters
       if bday == "" or any(char.isalpha() for char in bday):
            continue
       
       # if the key (mm/dd) is not in buddies, add it with an empty list
       if key not in buddies:
              buddies[key] = []

       # append student's name to the list of buddies for that key
       buddies[key].append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]}")

# Open data file and inspect the cases
# We need to ignore empty birthdays and birthdays that are text
# Like before, string methods .isalpha(), .isnumeric() might be useful here

# Print only the birthday buddies 
for key in buddies:
      if len(buddies[key])>1: # If several people share a birthday
              print(f"{key}: {buddies[key]}")

################################################################################################
# Problem 8 COMPLETE
################################################################################################