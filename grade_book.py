'''
grade_book.py : Create a grade book that converts grades and documents all inputs involved

by: Will Colvill

12/10/19
'''

#create my main function
def main():
    course = input("What is the course name: ")
    teacher = input("What is the teacher's name: ")
    newClassFile(course, teacher)
    again = 1
    grade_a = 0
    grade_b = 0
    grade_c = 0
    grade_d = 0
    grade_f = 0
    while 1 == 1:
        name, grade = getStudentInfo()
        letter_grade, grade_a, grade_b, grade_c, grade_d, grade_f = gradeConverter(grade, grade_a, grade_b, grade_c, grade_d, grade_f)
        addStudentToFile(course, teacher, name, grade, letter_grade)
        again = input('Would you like to add another student to this class? (1 for yes or 2 for no): ')
        if int(again) == 1:
            continue
        else:
            break
    displayTotalGrades(grade_a, grade_b, grade_c, grade_d, grade_f, course, teacher)

# get the students information
def getStudentInfo():
    name = input("What is the student's name? ")
    grade = input("What is the number score for this student? ")
    return name, grade

# convert the students grade
def gradeConverter(grade, grade_a, grade_b, grade_c, grade_d, grade_f):
    if int(grade) >= 90:
        letter_grade = 'A'
        grade_a += 1
    elif int(grade) >= 80:
        letter_grade = 'B'
        grade_b += 1
    elif int(grade) >= 70:
        letter_grade = 'C'
        grade_c += 1
    elif int(grade) >= 60:
        letter_grade = 'D'
        grade_d += 1
    else:
        letter_grade = 'F'
        grade_f += 1
    return letter_grade, grade_a, grade_b, grade_c, grade_d, grade_f

# create the class file
def newClassFile(course, teacher):
    try:
        class_file = open(str(course) + str(teacher) + '.txt', 'a')
    except IOError:
        class_file = open(str(course) + str(teacher) + '.txt', 'x')
    class_file.write('Course: ' + str(course) + '\n' + 'Teacher: ' + teacher + '\n' + '\n')

# add students to the class file
def addStudentToFile(course, teacher, name, grade, letter_grade):
    class_file = open(str(course) + str(teacher) + '.txt', 'a')
    class_file.write('Student: ' + str(name) + '\n' + 'Grade: ' + str(grade) + '\n' + 'Letter Grade: ' + str(letter_grade) + '\n' + '\n')

# display and add the total grades to the file and in the program
def displayTotalGrades(grade_a, grade_b, grade_c, grade_d, grade_f, course, teacher):
    print('Overall Grades:' + '\n' + 'Number of As: ' + str(grade_a) + '\n' + 'Number of Bs: ' + str(grade_b) + '\n' + 'Number of Cs: ' + str(grade_c) + '\n' + 'Number of Ds: ' + str(grade_d) + '\n' + 'Number of Fs: ' + str(grade_f))
    class_file = open(str(course) + str(teacher) + '.txt', 'a')
    class_file.write('Overall Grades:' + '\n' + 'Number of As: ' + str(grade_a) + '\n' + 'Number of Bs: ' + str(grade_b) + '\n' + 'Number of Cs: ' + str(grade_c) + '\n' + 'Number of Ds: ' + str(grade_d) + '\n' + 'Number of Fs: ' + str(grade_f))

#run function
main()
