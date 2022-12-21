'''
workshop.py : Calculates the total cost of an out of town workshop
By: Will Colvill
10/22/2019
'''

#1. Ask user to input the fee, days to stay, logdging fee, and transportation fee
registration_fee = input("How much is the registration fee?")
number_of_days = input("How many days will you be staying?")
daily_lodging_fee = input("What is the daily lodging fee?")
transportation_fee = input("How much is the transportation fee?")

#2. Convert the fees into integers/floats
registration_fee = float(registration_fee)
number_of_days = int(number_of_days)
daily_lodging_fee = float(daily_lodging_fee)
transportation_fee = float(transportation_fee)

#3. Calculate the total daily lodging fee
final_lodging_fee = daily_lodging_fee * number_of_days

#4. Calculate total cost of trip
total_cost = final_lodging_fee + registration_fee + transportation_fee

#5. Output the information
print("The total cost of the workshop if you stay for", number_of_days, "days is $", format(total_cost, ",.2f"))
