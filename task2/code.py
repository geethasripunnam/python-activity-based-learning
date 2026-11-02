rooms = []
floors = {}

n = int(input("Enter number of rooms: "))

for i in range(n):
    print("\nRoom", i + 1)

    room = input("Enter room number: ")
    floor = int(input("Enter floor number: "))
    electricity = float(input("Electricity units: "))
    water = float(input("Water consumption in litres: "))

    e_charge = electricity * 8
    w_charge = water * 5
    total = e_charge + w_charge

    print("Total Bill: Rs.", total)

    if electricity > 200:
        print("Electricity Threshold Violated")

    if water > 500:
        print("Water Threshold Violated")

    if floor not in floors:
        floors[floor] = [0, 0]

    floors[floor][0] += electricity
    floors[floor][1] += water

    rooms.append(room)

print("\nFloor-wise Resource Utilization")

for floor, usage in floors.items():
    print("Floor:", floor)
    print("Electricity:", usage[0], "units")
    print("Water:", usage[1], "litres")

highest = max(floors, key=lambda f: floors[f][0])
print("\nHighest Electricity Usage Floor:", highest)

print("Monitoring Completed")
