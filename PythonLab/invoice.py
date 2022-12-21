numItems = int(input("How many items? "))
itemArray = []
total = int(0)
for i in range(numItems):
    item = input("Enter item: ")
    price = int(input("Enter price: "))
    itemArray.append("Item: " + str(item) + " Price: " + str(price))
    total += price
for i in range(numItems):
    print(itemArray[i])
print("Total: ", total)