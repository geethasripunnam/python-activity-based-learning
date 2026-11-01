1. Problem Statement
Develop a Python program to monitor hospital resources such as bed occupancy, available staff and medical equipment across different wards. Identify resource shortages and prioritize wards according to their resource requirements.
2. Algorithm
1. Start the program.
2. Read the number of hospital wards.
3. Enter ward name, total beds, occupied beds, available staff and equipment.
4. Calculate available beds.
5. Check bed availability.
6. Check whether available staff are sufficient.
7. Check equipment availability.
8. Identify resource shortages.
9. Assign priority to wards with resource shortages.
10. Display ward-wise resource reports.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-


4. Python Source Code
wards = []n = int(input("Enter number of wards: "))for i in range(n):    print("\nWard", i + 1)    name = input("Ward name: ")    total_beds = int(input("Total beds: "))    occupied = int(input("Occupied beds: "))    staff = int(input("Available staff: "))    equipment = int(input("Available equipment: "))    available = total_beds - occupied    shortages = []    if available == 0:        shortages.append("No Beds Available")    if staff == 0:        shortages.append("Staff Shortage")    if equipment == 0:        shortages.append("Equipment Shortage")    if shortages:        priority = "HIGH"    else:        priority = "NORMAL"    wards.append((name, available, staff,                  equipment, priority, shortages))wards.sort(key=lambda x: x[4] != "HIGH")



5. Sample Input
Enter number of wards: 3

Ward 1
Ward name: General
Total beds: 50
Occupied beds: 40
Available staff: 10
Available equipment: 5

Ward 2
Ward name: ICU
Total beds: 20
Occupied beds: 20
Available staff: 0
Available equipment: 2

Ward 3
Ward name: Emergency
Total beds: 30
Occupied beds: 25
Available staff: 5
Available equipment: 0


6. Sample Output
--- HOSPITAL RESOURCE REPORT ---

Ward: ICU
Available Beds: 0
Available Staff: 0
Available Equipment: 2
Priority: HIGH
Shortages: No Beds Available, Staff Shortage

Ward: Emergency
Available Beds: 5
Available Staff: 5
Available Equipment: 0
Priority: HIGH
Shortages: Equipment Shortage

Ward: General
Available Beds: 10
Available Staff: 10
Available Equipment: 5
Priority: NORMAL
Shortages: None
