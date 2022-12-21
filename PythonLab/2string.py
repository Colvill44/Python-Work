# Write a Python program which receives a string and returns a new string with the first 2 and the last 2 chars from a given string. If the string length is less than 2, print out an appropriate message to the user.
from re import X


def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

x = input('Enter a string: ')
x = string_both_ends(x)
print(x)