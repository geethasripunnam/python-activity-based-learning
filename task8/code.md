1. Problem Statement
Develop a Python program to calculate electricity bills for multiple apartments using progressive tariffs, fixed charges and rebates. Identify billing discrepancies and rank apartments according to electricity consumption.
2. Algorithm
1. Start the program.
2. Read the number of apartments.
3. Enter apartment number and electricity units.
4. Calculate charges using progressive tariff rates:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
5. Add a fixed charge of ₹50.
6. Apply a rebate of ₹20 if consumption is below 100 units.
7. Calculate the final bill.
8. Check whether the bill has any discrepancy.
9. Sort apartments based on electricity consumption.
10. Display apartment-wise bills and rankings.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-



4. Python Source Code
apartments = []n = int(input("Enter number of apartments: "))for i in range(n):    print("\nApartment", i + 1)    number = input("Apartment number: ")    units = float(input("Electricity units: "))    if units <= 100:        charge = units * 2    elif units <= 200:        charge = 200 + (units - 100) * 3    else:        charge = 500 + (units - 200) * 5    fixed = 50    rebate = 20 if units < 100 else 0    bill = charge + fixed - rebate    apartments.append((number, units, bill))apartments.sort(key=lambda x: x[1], reverse=True)print("\n--- ELECTRICITY BILL REPORT ---")for rank, a in enumerate(apartments, 1):    print("\nRank:", rank)    print("Apartment:", a[0])    print("Units:", a[1])    print("Final Bill: Rs.", a[2])



5. Sample Input
Enter number of apartments: 3

Apartment 1
Apartment number: A101
Electricity units: 80

Apartment 2
Apartment number: A102
Electricity units: 150

Apartment 3
Apartment number: A103
Electricity units: 250


6. Sample Output
--- ELECTRICITY BILL REPORT ---

Rank: 1
Apartment: A103
Units: 250.0
Final Bill: Rs. 800.0

Rank: 2
Apartment: A102
Units: 150.0
Final Bill: Rs. 500.0

Rank: 3
Apartment: A101
Units: 80.0
Final Bill: Rs. 190.0

Highest Consumption Apartment: A103
