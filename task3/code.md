1. Problem Statement
Develop a Python program to analyse room-wise electricity and water consumption in a hostel. Calculate electricity and water charges, identify rooms exceeding consumption limits and compare resource utilization across different floors.
2. Algorithm
1. Start the program.
2. Read the number of hostel rooms.
3. Enter room number, floor number, electricity units and water units.
4. Calculate electricity charges at ₹5 per unit.
5. Calculate water charges at ₹2 per unit.
6. Calculate the total bill for each room.
7. Check whether electricity exceeds 200 units or water exceeds 500 litres.
8. Display threshold violations.
9. Calculate and display floor-wise resource consumption.
10. Stop the program.
3. Flowchart (Mermaid Code)






4. Python Source Code
rooms = []floor_data = {}n = int(input("Enter number of rooms: "))for i in range(n):    print("\nEnter room details")    room = input("Room number: ")    floor = int(input("Floor number: "))    electricity = float(input("Electricity units: "))    water = float(input("Water consumption: "))    e_charge = electricity * 5    w_charge = water * 2    total = e_charge + w_charge    violations = []    if electricity > 200:        violations.append("High Electricity")    if water > 500:        violations.append("High Water Usage")    rooms.append((room, floor, electricity,                  water, total, violations))    if floor not in floor_data:        floor_data[floor] = [0, 0]    floor_data[floor][0] += electricity    floor_data[floor][1] += waterprint("\n--- HOSTEL BILL REPORT ---")for r in rooms:    print("\nRoom:", r[0])    print("Floor:", r[1])    print("Electricity:", r[2])    print("Water:", r[3])    print("Total Bill: Rs.", r[4])    if r[5]:        print("Violation:", ", ".join(r[5]))    else:        print("Violation: None")print("\n--- FLOOR-WISE CONSUMPTION ---")for floor, values in sorted(floor_data.items()):    print("Floor:", floor)    print("Electricity:", values[0])    print("Water:", values[1])



5. Sample Input
Enter number of rooms: 3

Room number: 101
Floor number: 1
Electricity units: 150
Water consumption: 300

Room number: 102
Floor number: 1
Electricity units: 250
Water consumption: 400

Room number: 201
Floor number: 2
Electricity units: 180
Water consumption: 600


6. Sample Output
--- HOSTEL BILL REPORT ---

Room: 101
Floor: 1
Electricity: 150.0
Water: 300.0
Total Bill: Rs. 1350.0
Violation: None

Room: 102
Floor: 1
Electricity: 250.0
Water: 400.0
Total Bill: Rs. 2050.0
Violation: High Electricity

Room: 201
Floor: 2
Electricity: 180.0
Water: 600.0
Total Bill: Rs. 2100.0
Violation: High Water Usage

--- FLOOR-WISE CONSUMPTION ---
Floor: 1
Electricity: 400.0
Water: 700.0

Floor: 2
Electricity: 180.0
Water: 600.0
