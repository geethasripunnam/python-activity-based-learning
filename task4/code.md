1. Problem Statement
Develop a Python program to process courier package weights, destination zones, vehicle capacities and delivery priorities. Allocate packages to suitable vehicles based on their capacity and identify packages that cannot be dispatched.
2. Algorithm
1. Start the program.
2. Read the number of packages and vehicles.
3. Enter package ID, weight, destination zone and priority.
4. Enter vehicle ID, destination zone and capacity.
5. Sort packages according to priority.
6. Check destination zone and vehicle capacity.
7. Allocate packages to suitable vehicles.
8. Update the remaining vehicle capacity.
9. Identify packages that cannot be dispatched.
10. Display the dispatch report.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-





4. Python Source Code
packages = []vehicles = []n = int(input("Enter number of packages: "))for i in range(n):    print("\nPackage", i + 1)    pid = input("Package ID: ")    weight = float(input("Weight: "))    zone = input("Destination zone: ")    priority = int(input("Priority (1=High): "))    packages.append([pid, weight, zone, priority])m = int(input("\nEnter number of vehicles: "))for i in range(m):    print("\nVehicle", i + 1)    vid = input("Vehicle ID: ")    zone = input("Destination zone: ")    capacity = float(input("Capacity: "))    vehicles.append([vid, zone, capacity, []])packages.sort(key=lambda x: x[3])not_dispatched = []for p in packages:    allocated = False    for v in vehicles:        if v[1] == p[2] and v[2] >= p[1]:



5. Sample Input
Enter number of packages: 3

Package 1
Package ID: P101
Weight: 20
Destination zone: A
Priority: 2

Package 2
Package ID: P102
Weight: 40
Destination zone: B
Priority: 1

Package 3
Package ID: P103
Weight: 60
Destination zone: A
Priority: 1

Enter number of vehicles: 2

Vehicle 1
Vehicle ID: V1
Destination zone: A
Capacity: 50

Vehicle 2
Vehicle ID: V2
Destination zone: B
Capacity: 50


6. Sample Output
--- DISPATCH REPORT ---

Vehicle: V1
Zone: A
Packages: ['P101']
Remaining Capacity: 30.0

Vehicle: V2
Zone: B
Packages: ['P102']
Remaining Capacity: 10.0

Not Dispatched Packages: ['P103']
