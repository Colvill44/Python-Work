from collections import Counter
# Write a Python program which receives two dictionaries and combine them by adding values for common keys
one = {'a': 100, 'b': 200, 'c': 300}
two = {'a': 300, 'b': 200, 'd': 400}
three = Counter(one) + Counter(two)
print(three)