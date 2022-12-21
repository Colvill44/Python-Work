'''
gender_percent.py : Show percentage of males and females in a class
By: Will Colvill
10/22/2019
'''

#1 Get the number of males/females
number_of_males = input("How many males are in the class?")
number_of_females = input("How many females are in the class?")

#2 Convert to integers
number_of_males = int(number_of_males)
number_of_females = int(number_of_females)

#3 Calculate total number of students
total_students = number_of_females + number_of_males

#4 Calculate percentage of each gender
male_percent = number_of_males / total_students
female_percent = number_of_females / total_students

#5 Display percentages
print("Total number of students:", total_students)
print("Percentage of Males:", format(male_percent, "%"))
print("Percentage of Females:", format(female_percent, "%"))
