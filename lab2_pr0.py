################################################################################################
# Problem 0
# Practice with output
# Scroll for questions
################################################################################################

# Get the CSV module
import csv

# A function! It has a function name ("read_data"), and parameter ("data_path")
# It has a return value, so it **returns** data as a list of lists
def read_data(data_path): 
	"""
	Read the data from the file at data_path
	and return it as a list of lists
	"""

	# Open the data file
	data_file = open(data_path, mode='r', encoding='utf-8', errors='ignore')
	data = csv.reader(data_file, delimiter="\t")

	# Cast the data to a list before returning
	return list(data)

# Useful constants:
# The indices of all answers
# Can by used to access data like:
# my_desc = student[INDEX_DESCRIPTION]
INDEX_FIRST = 0
INDEX_LAST = 1
INDEX_PRONOUNS = 2
INDEX_DESCRIPTION = 3
INDEX_YEAR = 4
INDEX_MAJOR = 5
INDEX_IDEAL_MAJOR = 6
INDEX_BEVERAGE = 7
INDEX_EMOJI_FAV = 8
INDEX_LIVE_WHERE = 9
INDEX_LIVE_WITH = 10
INDEX_BIRTHDAY = 11
INDEX_FOOD = 12
INDEX_FUN_THING = 13
INDEX_LAT_NORTH = 14
INDEX_LAT_SOUTH = 15
INDEX_COOL_THING = 16
INDEX_THING_TO_MAKE = 17 
INDEX_STUDY_TIME = 18 
INDEX_STUDY_GOOD_AT = 19
INDEX_STUDY_HELP_WITH = 20 

# Get student data
data_path = "cs150data-w24.tsv"

data = read_data(data_path)

# The questions are the first row of data
questions = data[0]

# We can get just get the students by taking a slice
all_student_data = data[1:]


################################################################################################
# Questions
################################################################################################
# QUESTION 1 print names 
""" 
For each student in the data, 
print their name and year as the f string
  f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_YEAR]})"

all_student_data: a list-of-lists representing student data
"""

# Update the following code so that it prints the student's name and year in the format listed above
# Print all entries, even if fist name or last name is empty
# This loop iterates over every student (list of answers) 
# in the data (list of lists)
for student in all_student_data:
        # "pass" doesn't do anything, 
        # but for-loops always need at least one line in their body
        # You can comment it out when you have a print statement in this loop
        
        # prints student's first name, last name, and year
        print(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_YEAR]})")
        pass



# QUESTION 2 print majors
""" 
For each student in the data, 
print "first name last name (real major): ideal major"

all_student_data: a list-of-lists representing student data
"""     
 
# Print out the student's names, real, and fake majors
for student in all_student_data:
        print(f"{student[INDEX_FIRST]} {student[INDEX_LAST]} ({student[INDEX_MAJOR]}) {student[INDEX_IDEAL_MAJOR]}") 
        pass

# QUESTION 3 print cool things
""" 
For each student in the data, 
print three lines
f"{student[INDEX_FIRST]} {student[INDEX_LAST]}"
f"\t{student[INDEX_COOL_THING].strip()}
f"\t{student[INDEX_THING_TO_MAKE].strip()}"
(.strip() removes extra whitespace, which Google sheets leaves in sometimes)

Only print the second two lines if the student has an answer for them
        ie: student[INDEX_COOL_THING].strip() != ""

all_student_data: a list-of-lists representing student data
"""
        
# Print out the name, the cool thing, and a thing to make 
# for each student that has that information
for student in all_student_data:
        # print student's name
        print(f"{student[INDEX_FIRST]} {student[INDEX_LAST]}")
        # if the student's cool thing and a thing to make is not empty, print the following lines
        if student[INDEX_COOL_THING].strip() != "" or student[INDEX_THING_TO_MAKE].strip() != "":
                print(f"\t{student[INDEX_COOL_THING].strip()}")
                print(f"\t{student[INDEX_THING_TO_MAKE].strip()}")
        pass

# QUESTION 4 make a list of emoji and print it  
''' Only add emoji if emoji entry is not empty '''
emoji_list = [] # Make a list of all emoji in the class

for student in all_student_data:
        # if the emoji list is not empty, append the student's favorite emoji to emoji_list
        if student[INDEX_EMOJI_FAV] != "":
                emoji_list.append(student[INDEX_EMOJI_FAV])
        pass
# print emoji_list
print(emoji_list)

# QUESTION 5 print study partners
# For each student who wants a study group, print their name and when
# Then indent with a tab and print what they are good at, and want help with
"""
for student in all_student_data:
        
        # todo: create all these variables

        if student_has_study_data:
                print("") # make a new line
                print(f"{firstname} {lastname}, {times}")
                print(f"\t{goodAt}")
                print(f"\t{helpWith}")
""" 

for student in all_student_data:
    # setting variables
    student_has_study_data = student[INDEX_STUDY_TIME] != ""
    firstname = student[INDEX_FIRST]
    lastname = student[INDEX_LAST]
    times = student[INDEX_STUDY_TIME]
    goodAt = student[INDEX_STUDY_GOOD_AT] != ""
    helpWith = student[INDEX_STUDY_HELP_WITH] != ""
    if student_has_study_data != "" and goodAt != "" and helpWith != "":
        print("") # make a new line
        print(f"{firstname} {lastname}, {times}") # print student's name when wanted time
        print(f"\t{goodAt}") # tab and print what they're good at
        print(f"\t{helpWith}") # tab what they want help with
        continue
    
################################################################################################
# Problem 0 COMPLETE
################################################################################################
