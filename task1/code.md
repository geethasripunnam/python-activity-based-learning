1. Problem Statement
Develop a Python program to shortlist scholarship candidates based on minimum academic marks, attendance percentage, family income and ranking rules. Select eligible students according to their merit and a fixed scholarship quota. Display the selected candidates and rejected candidates with reasons.
2. Algorithm
1. Start the program.
2. Read the number of students and scholarship quota.
3. Enter each student's name, marks, attendance and family income.
4. Check academic eligibility (minimum 75% marks).
5. Check attendance eligibility (minimum 75%).
6. Check family income (maximum ₹2,00,000).
7. Add eligible students to a list.
8. Sort eligible students according to marks in descending order.
9. Select students according to the scholarship quota.
10. Display selected and rejected students.
11. Stop the program.
3. Flowchart (Mermaid Code)






4. Python Source Code
students = []eligible = []rejected = []n = int(input("Enter number of students: "))quota = int(input("Enter scholarship quota: "))for i in range(n):    print("\nEnter details of student", i + 1)    name = input("Enter name: ")    marks = float(input("Enter marks: "))    attendance = float(input("Enter attendance: "))    income = float(input("Enter family income: "))    reasons = []    if marks < 75:        reasons.append("Low Marks")    if attendance < 75:        reasons.append("Low Attendance")    if income > 200000:        reasons.append("High Income")    if len(reasons) == 0:        eligible.append((name, marks, attendance, income))    else:        rejected.append((name, reasons))eligible.sort(key=lambda x: x[1], reverse=True)selected = eligible[:quota]waiting = eligible[quota:]print("\n--- SELECTED STUDENTS ---")for student in selected:    print(student)print("\n--- WAITING LIST ---")for student in waiting:    print(student)print("\n--- REJECTED STUDENTS ---")for student, reasons in rejected:    print(student, "-", ", ".join(reasons))



5. Sample Input
Enter number of students: 4
Enter scholarship quota: 2

Enter details of student 1
Enter name: Ravi
Enter marks: 85
Enter attendance: 90
Enter family income: 150000

Enter details of student 2
Enter name: Sita
Enter marks: 70
Enter attendance: 80
Enter family income: 100000

Enter details of student 3
Enter name: Kumar
Enter marks: 92
Enter attendance: 95
Enter family income: 180000

Enter details of student 4
Enter name: Priya
Enter marks: 80
Enter attendance: 60
Enter family income: 100000


6. Sample Output
--- SELECTED STUDENTS ---
('Kumar', 92.0, 95.0, 180000.0)
('Ravi', 85.0, 90.0, 150000.0)

--- WAITING LIST ---

--- REJECTED STUDENTS ---
Sita - Low Marks
Priya - Low Attendance
