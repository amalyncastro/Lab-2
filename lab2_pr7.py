
################################################################################################
# Problem 7
# Per year enrollment
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
For every graduation year (make it an integer), count the number of students graduating in that year
using a dictionary.
Print the dictionary.
student[4]
"""
	
count = {} # Use dictionary
for student in all_student_data:
        # getting student's graduation year
        year = student[INDEX_YEAR]

        # Write your code here

        # check if year is empty, and skip if it is
        if year == "":
                continue

        # convert year to integer
        year = int(year)
        
        # check if year is already in count (dictionary)
        if year in count:
                # if so, add one to that year
                count[year] += 1
        else:
                # if no, add the year to the count = 1
                count[year] = 1
print(count) # Print dictionary

################################################################################################
# Problem 7 complete
################################################################################################