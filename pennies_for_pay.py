'''
pennies_for_pay.py :

11/7/19

By Will Colvill
'''

daily_pay = 0.01
total_pay = 0
days_to_work = int(input("How many days would you like to work?: "))

for day in range(1, days_to_work + 1):
    print("Day", day, ": $", daily_pay)
    total_pay += daily_pay
    daily_pay = daily_pay * 2

#print total
print("Your total pay after", days_to_work, "days will be $", total_pay)
