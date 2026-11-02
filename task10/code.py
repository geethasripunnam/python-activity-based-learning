students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance: "))
    income = float(input("Enter family income: "))

    students.append(name)

    if marks >= 75 and attendance >= 75 and income <= 250000:
        eligible.append((name, marks))
    else:
        print(name, "is Not Eligible")

eligible.sort(key=lambda x: x[1], reverse=True)

quota = int(input("\nEnter scholarship quota: "))

selected = eligible[:quota]

print("\nSelected Scholarship Students:")

if selected:
    for student in selected:
        print(student[0], "-", student[1], "Marks")
else:
    print("No students selected")

print("\nTotal Eligible Students:", len(eligible))
print("Total Selected Students:", len(selected))

