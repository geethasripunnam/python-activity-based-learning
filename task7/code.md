1. Problem Statement
Develop a Python program to process student marks across multiple subjects. Apply moderation rules by adding grace marks to students according to specified conditions. Ensure that the moderated marks do not exceed the maximum marks and compare original and moderated results.
2. Algorithm
1. Start the program.
2. Read the number of students and subjects.
3. Enter student name and subject marks.
4. Calculate the original total marks.
5. Check whether each subject mark is below the passing mark.
6. If a student is short by up to 5 marks, add grace marks.
7. Ensure moderated marks do not exceed 100.
8. Calculate moderated total marks.
9. Compare original and moderated results.
10. Display the final result.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-_r_m5_

4. Python Source Code
n = int(input("Enter number of students: "))subjects = int(input("Enter number of subjects: "))for i in range(n):    name = input("\nEnter student name: ")    original = []    moderated = []    for j in range(subjects):        mark = float(input("Enter subject mark: "))        original.append(mark)        if mark < 40 and mark >= 35:            mark = min(mark + (40 - mark), 100)        moderated.append(mark)    original_total = sum(original)    moderated_total = sum(moderated)    if all(mark >= 40 for mark in moderated):        result = "PASS"    else:        result = "FAIL"    print("\n--- RESULT REPORT ---")    print("Student:", name)    print("Original Marks:", original)    print("Moderated Marks:", moderated)    print("Original Total:", original_total)    print("Moderated Total:", moderated_total)    print("Final Result:", result)



5. Sample Input
Enter number of students: 2
Enter number of subjects: 3

Enter student name: Ravi
Enter subject mark: 35
Enter subject mark: 75
Enter subject mark: 80

Enter student name: Sita
Enter subject mark: 60
Enter subject mark: 70
Enter subject mark: 85


6. Sample Output
--- RESULT REPORT ---
Student: Ravi
Original Marks: [35.0, 75.0, 80.0]
Moderated Marks: [40.0, 75.0, 80.0]
Original Total: 190.0
Moderated Total: 195.0
Final Result: PASS

--- RESULT REPORT ---
Student: Sita
Original Marks: [60.0, 70.0, 85.0]
Moderated Marks: [60.0, 70.0, 85.0]
Original Total: 215.0
Moderated Total: 215.0
Final Result: PASS
