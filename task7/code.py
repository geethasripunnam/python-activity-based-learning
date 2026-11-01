n = int(input("Enter number of students: "))
subjects = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("\nEnter student name: ")

    original = []
    moderated = []

    for j in range(subjects):
        mark = float(input("Enter subject mark: "))
        original.append(mark)

        if mark < 40 and mark >= 35:
            mark = min(mark + (40 - mark), 100)

        moderated.append(mark)

    original_total = sum(original)
    moderated_total = sum(moderated)

    if all(mark >= 40 for mark in moderated):
        result = "PASS"
    else:
        result = "FAIL"

    print("\n--- RESULT REPORT ---")
    print("Student:", name)
    print("Original Marks:", original)
    print("Moderated Marks:", moderated)
    print("Original Total:", original_total)
    print("Moderated Total:", moderated_total)
    print("Final Result:", result)
