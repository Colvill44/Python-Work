'''
numbers.py : sorts a group of numbers submitted by a user and provides a max min and average of them

by: Will Colvill

11/19/19
'''

# Define Variables
total = 0
total_numbers = 0
max = float('-inf')
min = float('inf')

# Create while statement and produce min and max
while True:
    number = input("Enter a number or press enter to exit!: ")
    if number == "":
        break
    else:
        num = int(number)
        total += num
        total_numbers += 1
        if num > max:
            max = num
        if num < min:
            min = num

# Calculate average and display data
average = total / total_numbers
print("Max:", max)
print("Min:", min)
print("Average:", average)
