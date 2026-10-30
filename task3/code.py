Python Source Code rooms = []floor_data = {}n = int(input("Enter number of rooms: "))for i in range(n):
  print("\nEnter room details")
  room = input("Room number: ") 
  floor = int(input("Floor number: ")) 
  electricity = float(input("Electricity units: "))
  water = float(input("Water consumption: ")) e_charge = electricity * 5 w_charge = water * 2 total = e_charge + w_charge violations = [] if electricity > 200: violations.append("High Electricity") if water > 500: violations.append("High Water Usage") rooms.append((room, floor, electricity, water, total, violations)) if floor not in floor_data: floor_data[floor] = [0, 0] floor_data[floor][0] += electricity floor_data[floor][1] += waterprint("\n--- HOSTEL BILL REPORT ---")for r in rooms: 
    print("\nRoom:", r[0])
    print("Floor:", r[1]) 
    print("Electricity:", r[2])
    print("Water:", r[3])
    print("Total Bill: Rs.", r[4]) if r[5]:
    print("Violation:", ", ".join(r[5]))
else: print("Violation: None")
  print("\n--- FLOOR-WISE CONSUMPTION ---")for floor, values in sorted(floor_data.items()):
    print("Floor:", floor)
    print("Electricity:", values[0])
    print("Water:", values[1])


