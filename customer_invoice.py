'''
customer_invoice.py : Create a customer invoice through user input data

by Will Colvill

11/19/2019
'''

# keep a running total and define invoice as a string
total = 0
invoice = ''

# create the while statement and its conditions for storing the data
while True:
    new_items = input("Do you have more items? If not press enter to exit: ")
    if new_items == "":
        break
    else:
        item = input("What is the item?: ")
        quantity = int(input("How many of this item did you purchase?: "))
        price = float(input("How much does a single one of these cost?: "))
        item_total = float(quantity * price)
        invoice += ('%-15s' % item + '%-15s' % format(price, '.2f') + '%-15s' % quantity + '%10s' % format(item_total, '.2f'))
        invoice += "\n"
        total += item_total

# print the information
print("-------------------------INVOICE-----------------------")
print('Item           Price          Quantity       Item Total')
print(invoice)
print('Total Cost: $', format(total, '.2f'))
