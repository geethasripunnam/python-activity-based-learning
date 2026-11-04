wards = []

n = int(input("Enter number of wards: "))

for i in range(n):
    print("\nEnter details for Ward", i + 1)

    name = input("Ward name: ")
    total_beds = int(input("Total beds: "))
    occupied = int(input("Occupied beds: "))
    staff = int(input("Available staff: "))
    equipment = int(input("Available equipment: "))
    required_equipment = int(input("Required equipment: "))

    available = total_beds - occupied

    wards.append([
        name, total_beds, occupied,
        available, staff, equipment,
        required_equipment
    ])

print("\n--- Hospital Resource Report ---")

for ward in wards:
    name = ward[0]
    available = ward[3]
    staff = ward[4]
    equipment = ward[5]
    required = ward[6]

    print("\nWard:", name)
    print("Available Beds:", available)
    print("Available Staff:", staff)

    shortage = []

    if available < 2:
        shortage.append("Bed shortage")

    if staff < 3:
        shortage.append("Staff shortage")

    if equipment < required:
        shortage.append("Equipment shortage")

    if shortage:
        print("Shortages:", ", ".join(shortage))
        print("Priority: HIGH")
    else:
        print("Resource Status: Sufficient")
        print("Priority: NORMAL")

print("\nHospital Resource Analysis Completed")
