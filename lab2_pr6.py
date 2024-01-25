
################################################################################################
# Problem 6
# South of Milwaukee
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
Find each student who has only travelled SOUTH of the Milwaukee border (42.5 degrees N)
For each one that you find, append
        f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student_lat}°)" to a list
and print that list

Skip any student with an empty value ("")   
"""

MILWAUKEE_LAT = 42.5
southern_students = []
for student in data:
        # variable contains student's data of lat_north
        student_lat = student[INDEX_LAT_NORTH]
        # Be sure to compare floats to floats
        # rather than floats to strings

        # if student_lat contains any of these, skip
        if student_lat == "" or "°" in student_lat or any(char.isalpha() for char in student_lat):
                continue

        # takes student_lat, splits, and takes everything before the comma and removes any spaces in the process
        student_lat = student_lat.split(",")[0].strip()

        # cast the string to a float
        student_lat = float(student_lat)

        # if the student's is less than or equal to milkwaukee's lat, append their first names, last name, and their latitude into southern_students
        if student_lat <= MILWAUKEE_LAT:
                southern_students.append(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student_lat}°)")
        continue
# print the list
print(southern_students)
        # Can we compare the Milwuakee Latitude to this students northernmost latitude?
        # Uncomment this to see what type of data we have
        # print(type(student_lat), type(MILWAUKEE_LAT)) # error
        # Like before, we need to *cast* the string to a float: 
        # student_lat = float(student_lat)
        # Try it! You'll get an error
        # Some students have no answer or "°" in their answer, so you need an "if" statement
        # Only cast and do a comparison if they have an answer that can be converted to a float

        # Open the spreadsheet and look at the data again.
        # List the cases that you need to consider:
        #    empty string or string of spaces - eliminate them from consideration
        #    names of places (Austria, Evanston, IL) - eliminate them from consideration
        #    two numbers are listed (only the first should be considered)
        #    name of the place and latitude separated by comma (only the value should be considered)
        #    ° symbol is present
        # Essentially our approach is to eliminate cases where we can't infer latitude programmatically
        # And deal with others
        # String methods .isalpha(), .isnumeric(), .replace(), .find(), .split() might be useful here
        # Loop control statement "continue" might also be useful

################################################################################################
# Problem 6 COMPLETE
################################################################################################
