apartments = []

n = int(input("Enter number of apartments: "))

for i in range(n):
    print("\nApartment", i + 1)

    number = input("Apartment number: ")
    units = float(input("Electricity units: "))

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = 200 + (units - 100) * 3

    else:
        charge = 500 + (units - 200) * 5

    fixed = 50
    rebate = 20 if units < 100 else 0

    bill = charge + fixed - rebate

    apartments.append((number, units, bill))

apartments.sort(key=lambda x: x[1], reverse=True)

print("\n--- ELECTRICITY BILL REPORT ---")

for rank, a in enumerate(apartments, 1):
    print("\nRank:", rank)
    print("Apartment:", a[0])
    print("Units:", a[1])
    print("Final Bill: Rs.", a[2])

print("\nHighest Consumption Apartment:",
      apartments[0][0] if apartments else "None")
