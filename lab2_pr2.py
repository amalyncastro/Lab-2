
################################################################################################
# Problem 2
# Noodles
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
# Question
################################################################################################
""" 
Print the integer number of students who like noodle/noodles restaurants 
People spelled noodles lots of different ways, so print the count where
where "noodle" appears anywhere in the answer, capitalized or not

Steps: start a counter "count" at 0
* Go through each student in the data ("for student in data")
* Get their favorite restaurant (INDEX_FOOD) and store it in a string variable "restaurant"
* Make that variable lowercase  "restaurant = restaurant.lower()"
* See if "noodles" appears in that string 
        * You can do this in Python with ' "noodle" in restaurant'
* If so, add 1 to the count
* Print the final count

all_student_data: a list-of-lists representing student data

print:  an integer of the number of students with "noodle" in their favorite restaurant name
"""

# intialize count
count = 0
for student in all_student_data:
	# restaurant lowercases all student's favorite food data
	restaurant = student[INDEX_FOOD].lower()
	# if the work "noodle" appears in restaurant, add one to count
	if "noodle" in restaurant:
		count += 1
	continue
# print the final count
print(count)

################################################################################################
# Problem 2 COMPLETE
################################################################################################