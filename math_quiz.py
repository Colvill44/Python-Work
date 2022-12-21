'''
math_quiz.py : Create an addition and subtraction math quiz with 3 levels of difficulty and display the results.

By: Will Colvill

11/21/19
'''

import random

# make a function to display my introduction
def display_intro():
    title = "***** Math Quiz *****"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

# make a function to display the properties menu
def display_prop_menu():
    menu_list = ["1. Addition", "2. Subtraction"]
    print(menu_list[0])
    print(menu_list[1])

# make a function to display the difficulty menu
def display_diff_menu():
    menu_list = ["1. Easy", "2. Intermediate", "3. Hard",]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])

# make a function to separate each problem and section
def display_separator():
    print("-" * 21)

# make a function to get users property choice
def get_user_prop_input():
    user_prop_input = int(input("Enter selection: "))
    while user_prop_input > 2 or user_prop_input <= 0:
        print("Invalid input.")
        user_prop_input = int(input("Try another entry: "))
    else:
        return user_prop_input

# make a function to get users difficulty choice
def get_user_diff_input():
    user_diff_input = int(input("Enter selection: "))
    while user_diff_input > 3 or user_diff_input <= 0:
        print("Invalid input.")
        user_diff_input = int(input("Try another entry: "))
    else:
        return user_diff_input

# make a function to get the users answer
def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

# make a function to check to see if the answer is correct/incorrect
def check_solution(user_solution, solution):
    if user_solution == solution:
        print("Correct.")
        return 1
    else:
        print("Incorrect.")
        return 0

# make a function to generate a problem based on the users preferences and call for users answer and users correctness
def prop_menu_option(user_diff_input, user_prop_input):
    if user_diff_input is 1:
        number_one = random.randrange(1,9)
        number_two = random.randrange(1,9)
        if user_prop_input is 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count
        elif user_prop_input is 2:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count
    elif user_diff_input is 2:
        number_one = random.randrange(10,99)
        number_two = random.randrange(10,99)
        if user_prop_input is 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count
        elif user_prop_input is 2:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count
    elif user_diff_input is 3:
        number_one = random.randrange(100,999)
        number_two = random.randrange(100,999)
        if user_prop_input is 1:
            problem = str(number_one) + " + " + str(number_two)
            solution = number_one + number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count
        elif user_prop_input is 2:
            problem = str(number_one) + " - " + str(number_two)
            solution = number_one - number_two
            user_solution = get_user_solution(problem)
            count = check_solution(user_solution, solution)
            return count

# make a function to display the results of the user
def display_result(count):
    if count > 0:
        result = (count / 10) * 100
    if count == 0:
        result = 0
    print("You answered", count, "questions correct out of 10.")
    print("You scored a", result, "%")

def display_diff_and_prop(user_prop_input, user_diff_input):
    if user_prop_input is 1:
        property = "Addition"
        if user_diff_input is 1:
            difficulty = "Easy"
        elif user_diff_input is 2:
            difficulty = "Intermediate"
        elif user_diff_input is 3:
            difficulty = "Hard"
    else:
        property = "Subtraction"
        if user_diff_input is 1:
            difficulty = "Easy"
        elif user_diff_input is 2:
            difficulty = "Intermediate"
        elif user_diff_input is 3:
            difficulty = "Hard"
    print("Thanks for taking the", difficulty, property, "Test. Here are your results: ")

# genereate a main function to order and perform the different functions of the program
def main():
    display_intro()
    display_prop_menu()
    display_separator()
    user_prop_input = get_user_prop_input()
    display_diff_menu()
    display_separator()
    user_diff_input = get_user_diff_input()
    total_count = 0
    right_ans = 0
    while total_count <= 9:
        display_separator()
        count = prop_menu_option(user_diff_input, user_prop_input)
        total_count += 1
        if count == 1:
            right_ans += 1
    display_separator()
    display_diff_and_prop(user_diff_input, user_prop_input)
    display_result(right_ans)

# run the main function
main()
