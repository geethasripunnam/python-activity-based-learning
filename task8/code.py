orders = []

n = int(input("Enter number of orders: "))

for i in range(n):
    print("\nEnter Order", i + 1)

    product = input("Product name: ")
    stock = int(input("Available stock: "))
    quantity = int(input("Order quantity: "))
    priority = input("Priority (High/Medium/Low): ")

    orders.append([product, stock, quantity, priority])

orders.sort(key=lambda x: 
    {"High": 1, "Medium": 2, "Low": 3}.get(x[3], 4))

print("\n--- Warehouse Order Report ---")

for order in orders:
    product = order[0]
    stock = order[1]
    quantity = order[2]
    priority = order[3]

    fulfilled = min(stock, quantity)
    outstanding = quantity - fulfilled

    print("\nProduct:", product)
    print("Priority:", priority)
    print("Ordered Quantity:", quantity)
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", outstanding)

    if outstanding == 0:
        print("Status: Complete")
    else:
        print("Status: Partial")

print("\nWarehouse Order Processing Completed")
