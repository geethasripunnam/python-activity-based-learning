print("UNIVERSITY EXAMINATION RESULT MODERATION")

n = int(input("Enter number of students: "))
s = int(input("Enter number of subjects: "))

for i in range(n):
    name = input("\nEnter student name: ")
    original = []
    moderated = []

    for j in range(s):
        mark = int(input("Enter subject marks: "))
        original.append(mark)

        if 35 <= mark < 40:
            new_mark = mark + 5
        else:
            new_mark = mark

        if new_mark > 100:
            new_mark = 100

        moderated.append(new_mark)

    old_total = sum(original)
    new_total = sum(moderated)

    print("\nStudent Name:", name)
    print("Original Marks:", original)
    print("Moderated Marks:", moderated)
    print("Original Total:", old_total)
    print("Moderated Total:", new_total)

    if all(mark >= 40 for mark in original):
        print("Original Result: PASS")
    else:
        print("Original Result: FAIL")

    if all(mark >= 40 for mark in moderated):
        print("Moderated Result: PASS")
    else:
        print("Moderated Result: FAIL")
