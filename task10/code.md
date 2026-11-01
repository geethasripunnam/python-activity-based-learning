. Problem Statement
Develop a Python program to manage warehouse orders using product demand, available stock, order quantities and priority categories. Determine whether each order can be fulfilled completely or partially and calculate the outstanding quantities.
2. Algorithm
1. Start the program.
2. Read the number of orders.
3. Enter order ID, product name, available stock, order quantity and priority.
4. Sort orders according to priority.
5. Compare available stock with order quantity.
6. If stock is sufficient, fulfil the complete order.
7. Otherwise, fulfil the available quantity.
8. Calculate outstanding quantity.
9. Update the remaining stock.
10. Display the order fulfilment report.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid



4. Python Source Code
orders = []n = int(input("Enter number of orders: "))for i in range(n):    print("\nOrder", i + 1)    oid = input("Order ID: ")    product = input("Product name: ")    stock = int(input("Available stock: "))    quantity = int(input("Order quantity: "))    priority = input("Priority (High/Medium/Low): ")    orders.append({        "id": oid,        "product": product,        "stock": stock,        "quantity": quantity,        "priority": priority    })priority_order = {"High": 1, "Medium": 2, "Low": 3}orders.sort(    key=lambda x: priority_order.get(x["priority"], 4))print("\n--- WAREHOUSE ORDER REPORT ---")for order in orders:    stock = order["stock"]    quantity = order["quantity"]    fulfilled = min(stock, quantity)    outstanding = quantity - fulfilled



5. Sample Input
Enter number of orders: 3

Order 1
Order ID: O101
Product name: Laptop
Available stock: 10
Order quantity: 8
Priority: High

Order 2
Order ID: O102
Product name: Mouse
Available stock: 5
Order quantity: 10
Priority: Medium

Order 3
Order ID: O103
Product name: Keyboard
Available stock: 0
Order quantity: 6
Priority: Low


6. Sample Output
--- WAREHOUSE ORDER REPORT ---

Order ID: O101
Product: Laptop
Priority: High
Ordered Quantity: 8
Fulfilled Quantity: 8
Outstanding Quantity: 0
Remaining Stock: 2
Status: Fully Fulfilled

Order ID: O102
Product: Mouse
Priority: Medium
Ordered Quantity: 10
Fulfilled Quantity: 5
Outstanding Quantity: 5
Remaining Stock: 0
Status: Partially Fulfilled

Order ID: O103
Product: Keyboard
