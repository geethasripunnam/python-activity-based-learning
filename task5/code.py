participants = []
duplicates = []

n = int(input("Enter number of participants: "))

for i in range(n):
    print("\nParticipant", i + 1)

    pid = input("Enter participant ID: ")
    fee = float(input("Enter registration fee: "))

    if pid in [p[0] for p in participants]:
        duplicates.append(pid)
    else:
        participants.append((pid, fee))

sponsorship = float(input("\nEnter sponsorship amount: "))
expenses = float(input("Enter total expenses: "))

registration_income = sum(p[1] for p in participants)

total_income = registration_income + sponsorship
balance = total_income - expenses

print("\n--- FESTIVAL FINANCIAL AUDIT ---")

print("Valid Participants:", len(participants))
print("Registration Income: Rs.", registration_income)
print("Sponsorship: Rs.", sponsorship)
print("Total Income: Rs.", total_income)
print("Total Expenses: Rs.", expenses)
print("Final Balance: Rs.", balance)

print("Duplicate IDs:", duplicates)

if balance >= 0:
    print("Financial Status: Profit")
else:
    print("Financial Status: Loss")
