wards = []

n = int(input("Enter number of wards: "))

for i in range(n):
    print("\nWard", i + 1)

    name = input("Ward name: ")
    total_beds = int(input("Total beds: "))
    occupied = int(input("Occupied beds: "))
    staff = int(input("Available staff: "))
    equipment = int(input("Available equipment: "))

    available = total_beds - occupied

    shortages = []

    if available == 0:
        shortages.append("No Beds Available")

    if staff == 0:
        shortages.append("Staff Shortage")

    if equipment == 0:
        shortages.append("Equipment Shortage")

    if shortages:
        priority = "HIGH"
    else:
        priority = "NORMAL"

    wards.append((name, available, staff,
                  equipment, priority, shortages))

wards.sort(key=lambda x: x[4] != "HIGH")

print("\n--- HOSPITAL RESOURCE REPORT ---")

for w in wards:
    print("\nWard:", w[0])
    print("Available Beds:", w[1])
    print("Available Staff:", w[2])
    print("Available Equipment:", w[3])
    print("Priority:", w[4])

    if w[5]:
        print("Shortages:", ", ".join(w[5]))
    else:
        print("Shortages: None")
