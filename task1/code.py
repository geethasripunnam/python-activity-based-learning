n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    fee = input("Fee paid (yes/no): ").lower()
    attendance = float(input("Enter attendance: "))
    marks = float(input("Enter internal marks: "))
    record = input("Eligibility record valid (yes/no): ").lower()

    reasons = []

    if fee != "yes":
        reasons.append("Fee Not Paid")

    if attendance < 75:
        reasons.append("Low Attendance")

    if marks < 40:
        reasons.append("Low Internal Marks")

    if record != "yes":
        reasons.append("Eligibility Record Missing")

    print("\nStudent Name:", name)

    if len(reasons) == 0:
        print("Status: Eligible for Examination")
    else:
        print("Status: Not Eligible")
        print("Outstanding Conditions:")
        for reason in reasons:
            print("-", reason)

print("\nUniversity Fee and Eligibility Audit Completed")

