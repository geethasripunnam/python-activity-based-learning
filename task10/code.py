orders = []

n = int(input("Enter number of orders: "))

for i in range(n):
    print("\nOrder", i + 1)

    oid = input("Order ID: ")
    product = input("Product name: ")
    stock = int(input("Available stock: "))
    quantity = int(input("Order quantity: "))
    priority = input("Priority (High/Medium/Low): ")

    orders.append({
        "id": oid,
        "product": product,
        "stock": stock,
        "quantity": quantity,
        "priority": priority
    })

priority_order = {"High": 1, "Medium": 2, "Low": 3}

orders.sort(
    key=lambda x: priority_order.get(x["priority"], 4)
)

print("\n--- WAREHOUSE ORDER REPORT ---")

for order in orders:
    stock = order["stock"]
    quantity = order["quantity"]

    fulfilled = min(stock, quantity)
    outstanding = quantity - fulfilled
    remaining = stock - fulfilled

    if outstanding == 0:
        status = "Fully Fulfilled"
    elif fulfilled > 0:
        status = "Partially Fulfilled"
    else:
        status = "Not Fulfilled"

    print("\nOrder ID:", order["id"])
    print("Product:", order["product"])
    print("Priority:", order["priority"])
    print("Ordered Quantity:", quantity)
    print("Fulfilled Quantity:", fulfilled)
    print("Outstanding Quantity:", outstanding)
    print("Remaining Stock:", remaining)
    print("Status:", status)
