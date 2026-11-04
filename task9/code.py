

routes = int(input("Enter number of bus routes: "))
days = int(input("Enter number of days: "))

data = []

for i in range(routes):
    print("\nRoute", i + 1)
    name = input("Enter route name: ")
    capacity = int(input("Enter bus capacity: "))

    total_passengers = 0
    total_time = 0
    total_fuel = 0

    for j in range(days):
        print("Day", j + 1)
        passengers = int(input("Enter passengers: "))
        time = float(input("Enter journey time: "))
        fuel = float(input("Enter fuel used: "))

        total_passengers += passengers
        total_time += time
        total_fuel += fuel

    avg_passengers = total_passengers / days
    avg_time = total_time / days

    if total_fuel > 0:
        efficiency = total_passengers / total_fuel
    else:
        efficiency = 0

    if avg_passengers > capacity:
        status = "Overloaded"
    else:
        status = "Normal"

    data.append((name, avg_passengers,
                 avg_time, efficiency, status))

print("\n--- BUS ROUTE PERFORMANCE REPORT ---")

for r in data:
    print("\nRoute:", r[0])
    print("Average Passengers:", r[1])
    print("Average Journey Time:", r[2])
    print("Fuel Efficiency:", round(r[3], 2))
    print("Status:", r[4])

print("\n--- OPERATING EFFICIENCY RANKING ---")

ranking = sorted(data, key=lambda x: x[3], reverse=True)

for r in ranking:
    print(r[0], "Efficiency:", round(r[3], 2))

print("\n--- OVERLOADED ROUTES ---")

for r in data:
    if r[4] == "Overloaded":
        print(r[0])

