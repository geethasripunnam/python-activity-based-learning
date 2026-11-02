packages = []
vehicles = {}

n = int(input("Enter number of packages: "))

for i in range(n):
    print("\nPackage", i + 1)

    pid = input("Enter package ID: ")
    weight = float(input("Enter package weight: "))
    zone = input("Enter destination zone: ")
    priority = int(input("Enter priority (1-High, 2-Low): "))

    packages.append((pid, weight, zone, priority))

v = int(input("\nEnter number of vehicles: "))

for i in range(v):
    vid = input("Enter vehicle ID: ")
    capacity = float(input("Enter vehicle capacity: "))
    vehicles[vid] = [capacity, []]

packages.sort(key=lambda x: x[3])

undispatched = []

for pid, weight, zone, priority in packages:
    allocated = False

    for vid in vehicles:
        if vehicles[vid][0] >= weight:
            vehicles[vid][0] -= weight
            vehicles[vid][1].append(pid)
            allocated = True
            break

    if not allocated:
        undispatched.append(pid)

print("\nVehicle-wise Allocation")

for vid, data in vehicles.items():
    print(vid, "Packages:", data[1])
    print("Remaining Capacity:", data[0])

print("\nUndispatched Packages:")

if undispatched:
    for pid in undispatched:
        print(pid)
else:
    print("All packages dispatched")

print("\nDispatch Planning Completed")


