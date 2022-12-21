'''
sort_three_numbers.py : Sorts three user generated numbers in order from least to greatest

By Will Colvill

11/5/19
'''
#1 Get numbers from user and convert them to integers
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

#2 Determine the order
if number_one > number_two and number_one > number_three:
    largest = number_one
    if number_two > number_three:
        smallest = number_three
        middle = number_two
    else:
        smallest = number_two
        middle = number_three
elif number_two > number_one and number_two > number_three:
    largest = number_two
    if number_one > number_three:
        smallest = number_three
        middle = number_one
    else:
        smallest = number_one
        middle = number_three
else:
    largest = number_three
    if number_one > number_two:
        smallest = number_two
        middle = number_one
    else:
        smallest = number_one
        middle = number_two

#3 Print Results
print("Here are the numbers in ascending order: ", smallest, ", ", middle, ", ", largest)


