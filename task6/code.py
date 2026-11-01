records = []
valid_records = []
errors = []
ids = set()

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    sid = input("Student ID: ")
    name = input("Student Name: ")
    marks = input("Marks: ")
    attendance = input("Attendance: ")
    course = input("Course: ")

    record = (sid, name, marks, attendance, course)
    records.append(record)

    reasons = []

    if sid in ids:
        reasons.append("Duplicate ID")
    else:
        ids.add(sid)

    if not all([sid, name, marks, attendance, course]):
        reasons.append("Missing Value")

    try:
        m = float(marks)
        a = float(attendance)

        if m < 0 or m > 100:
            reasons.append("Invalid Marks")

        if a < 0 or a > 100:
            reasons.append("Invalid Attendance")

    except ValueError:
        reasons.append("Invalid Numeric Data")

    if reasons:
        errors.append((sid, reasons))
    else:
        valid_records.append(record)

print("\n--- VALID STUDENT RECORDS ---")

for r in valid_records:
    print(r)

print("\n--- INCONSISTENT RECORDS ---")

for sid, reason in errors:
    print(sid, ":", ", ".join(reason))

print("\nTotal Records:", len(records))
print("Valid Records:", len(valid_records))
print("Invalid Records:", len(errors))
