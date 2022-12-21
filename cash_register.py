'''
cash_register.py: simulate payment made at the cash register
By Will Colvill
10/10/2019
'''

#1. ask user to enter the amount due and amount paid
amount_due = input("Enter the amount due: ")
amount_paid = input("Enter the amount paid: ")

#2. cast the input into number
amount_due = float(amount_due)
amount_paid = float(amount_paid)

#3. calculate the change
change = amount_paid - amount_due

#4. get larget bills possible
change_in_pennies = change * 100
#4.1 any $20 bills?
twenties = change_in_pennies // 2000

#4.2 modify change_in_pennies
change_in_pennies = change_in_pennies % 2000

#4.3 any $10 bills
tens = change_in_pennies // 1000
change_in_pennies = change_in_pennies % 1000

#4.4 any $5 bills
fives = change_in_pennies // 500
change_in_pennies = change_in_pennies % 500

#4.5 any $1 bills
ones = change_in_pennies // 100
change_in_pennies = change_in_pennies % 100

#4.6 any quarters
quarters = change_in_pennies // 25
change_in_pennies = change_in_pennies % 25

#4.7 any dimes
dimes = change_in_pennies // 10
change_in_pennies = change_in_pennies % 10

#4.8 any nickels
nickels = change_in_pennies // 5
pennies = change_in_pennies % 5

#display change
print("Total Charge: $", amount_due)
print("Total Paid: $", amount_paid)
print("Change: $", change)

print("Bills in Change:")
print("20$: ", twenties)
print("10$: ", tens)
print("5$: ", fives)
print("1$:", ones)
print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
