# Write a Python program which will find all numbers between two given numbers which are divisible by 7 but are not a multiple of 5
first = input('Enter the first number: ')
second = input('Enter the second number: ')
for i in range(int(first), int(second)):
  if i % 7 == 0 and i % 5 != 0:
    print(i)