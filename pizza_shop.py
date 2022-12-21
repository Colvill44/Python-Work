'''
pizza_shop.py : Generates a pizza shop and gives you a total cost of your pizzas

By: Will Colvill

11/5/19
'''

#1 Greet the customer
print("Welcome to my Pizza Shop")

#2 User selects size
size = int(input("Please select your size: Type 1 for Large, 2 for Medium, 3 for Small: "))

#3 Determine size price
if size == 1:
    size_price = int(16)
    size_kind = "Large"
elif size == 2:
    size_price = int(12)
    size_kind = "Medium"
elif size == 3:
    size_price = int(8)
    size_kind = "Small"

#4 Select crust and set its variable
crust = int(input("Select your crust type: Type 1 for Regular, 2 for Garlic, 3 for Cheese: "))
if crust == 1:
    crust_type = str("Regular")
elif crust == 2:
    crust_type = str("Garlic")
elif crust == 3:
    crust_type = str("Cheese")

#5 Choose toppings
pepperoni = input("Would you like pepperoni? Y for yes or N for no: ")
sausage = input("Would you like sausage? Y for yes or N for no: ")
onions = input("Would you like onions? Y for yes or N for no: ")
mushrooms = input("Would you like mushrooms? Y for yes or N for no: ")

#6 Evaluate the toppings and create a list
toppings = ""
toppings_price = 0
if pepperoni == "y" or pepperoni == "Y":
    toppings += "Pepperoni, "
    toppings_price = toppings_price + .50
if sausage == "y" or sausage == "Y":
    toppings += "Sausage, "
    toppings_price = toppings_price + .50
if onions == "y" or onions == "Y":
    toppings += "Onions, "
    toppings_price = toppings_price + .50
if mushrooms == "y" or mushrooms == "Y":
    toppings += "Mushrooms,"
    toppings_price = toppings_price + .50

toppings = toppings.rstrip(",")

#7 How many pizzas to order
quantity = int(input("How many pizzas would you like to order? "))

#8 calculate total cost of the pizza
single_pizza_cost = size_price + toppings_price
total_cost = single_pizza_cost * quantity

#9 Display information
print("Customer Reciept:")
print("Pizza Size: ", size_kind)
print("Crust Type: ", crust_type)
print("Additional Toppings: ", toppings)
print("Single Pizza Cost: $", format(single_pizza_cost, ".2f"))
print("Quantity: ", quantity)
print("Total Cost: $", format(total_cost, ".2f"))
