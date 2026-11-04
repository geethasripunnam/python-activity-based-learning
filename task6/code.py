print("SMART ELECTRICITY BILLING SYSTEM")

n = int(input("Enter number of apartments: "))
apartments = []

for i in range(n):
    print("\nApartment", i + 1)
    name = input("Enter apartment name: ")
    units = int(input("Enter electricity units: "))

    if units <= 100:
        charge = units * 2
    elif units <= 200:
        charge = 100 * 2 + (units - 100) * 3
    else:
        charge = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    total = charge + fixed

    if units < 100:
        rebate = total * 0.10
    else:
        rebate = 0

    bill = total - rebate

    expected = float(input("Enter previous calculated bill: "))

    if abs(expected - bill) > 0.01:
        status = "Discrepancy Found"
    else:
        status = "No Discrepancy"

    apartments.append([name, units, bill, status])

print("\n--- ELECTRICITY BILL REPORT ---")

for apt in apartments:
    print("\nApartment:", apt[0])
    print("Units Consumed:", apt[1])
    print("Final Bill: Rs.", round(apt[2], 2))
    print("Billing Status:", apt[3])

apartments.sort(key=lambda x: x[1], reverse=True)

print("\n--- CONSUMPTION RANKING ---")

for i, apt in enumerate(apartments, 1):
    print(i, apt[0], "-", apt[1], "units")
