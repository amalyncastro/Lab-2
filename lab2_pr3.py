
################################################################################################
# Problem 3
# CS major
# Read the entire file
################################################################################################

# Reading data from file is common between different problems in this assignment
# Instead of copying that code over and over, we put it in a separate python file (filereader.py, check it out) 
# Similarly, constants are used many times, we also put them in a separate file (constants.py, check it out)

import filereader # (1) now we bring (import) the function for reading files into our program
from constants import * # (2) we do same for constants. There are two different ways to import and you see them here

# Get student data
data_path = "cs150data-w24.tsv"

data = filereader.read_data(data_path) # Need to put the name of the file if import is done using (1).
# If import is done using (2), no need to put the name of file in the front of a function or a constant

# The questions are the first row of data
questions = data[0]

# We can get just get the students by taking a slice
all_student_data = data[1:]

################################################################################################
# Question
################################################################################################
""" 
print the integer number of students who do have a CS major
Similar to the noodle restaurant, but now we have a helper function to call
"""

def is_CS_major(major):
        """
        A helper function
        ** assumes that the major is lower case **
        Call this function to determine if a string contains a CS major or not
        Is this a CS major, 
        or did it just include the letters "cs" in "economi[cs]]" or "physi[cs]"
        """
        if "computer science" in major:
                return True
        if "comp sci" in major:
                return True
        if major.startswith("cs"):
                return True
        if " cs" in major or "/cs" in major or "&cs" in major or ",cs" in major:
                return True
        # If none of the above, return False
        return False
        # ^ end of this function


# -- Write your code here ---

# intialize counter
counter = 0
for student in all_student_data:
    # if is_CS_major for student's major lowercased, add one to counter
    if is_CS_major(student[INDEX_MAJOR].lower()):
        counter += 1
        continue
# print counter
print(counter)

# To debug, try printing the majors, 
# or print them out only if a CS major

# debug:
for student in all_student_data:
    print(student[INDEX_MAJOR])

# only if a CS major:
    for student in all_student_data:
        if is_CS_major(student[INDEX_MAJOR].lower()):
           print(student[INDEX_MAJOR])

################################################################################################
# Problem 3 COMPLETE
################################################################################################