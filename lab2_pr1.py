
################################################################################################
# Problem 1
# Metadata (data about data)
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
# Question 1 print the number of students in this dataset (needs to be calculated)

# initialize x
x = 0
for student in all_student_data:
	# if the student's first name is NOT empty, add one
	if student[INDEX_FIRST]	!= "":
		x += 1
	continue
# print total number of students in the dataset
print(x)

# Question 2 print the number of questions each student was asked (needs to be calculated)

# initialize z
z = 0
# for a random variable in questions add one (it will iterate through questions, data[0])
for y in questions:
       z += 1
# print total questions each student was asked
print(z)

################################################################################################
# Problem 1 COMPLETE
################################################################################################