1. Problem Statement
Develop a Python program to combine student fee payment details, attendance percentage, internal marks and examination eligibility records. Identify students who have outstanding fees, low attendance or insufficient internal marks. Generate a reason-wise report showing eligible and not eligible students.
2. Algorithm
1. Start the program.
2. Read the number of students.
3. Enter student name, total fee, paid fee, attendance and internal marks.
4. Calculate the pending fee.
5. Check whether the fee is fully paid.
6. Check attendance (minimum 75%).
7. Check internal marks (minimum 40).
8. Store eligible and not eligible students.
9. Display pending fees and reasons for ineligibility.
10. Stop the program.
3. Flowchart (Mermaid Code)


4. Python Source Code
students = []n = int(input("Enter number of students: "))for i in range(n):    print("\nEnter details of student", i + 1)    name = input("Enter student name: ")    total_fee = float(input("Enter total fee: "))    paid_fee = float(input("Enter paid fee: "))    attendance = float(input("Enter attendance percentage: "))    marks = float(input("Enter internal marks: "))    pending_fee = total_fee - paid_fee    reasons = []    if pending_fee > 0:        reasons.append("Fee Pending")    if attendance < 75:        reasons.append("Low Attendance")    if marks < 40:        reasons.append("Low Internal Marks")    if reasons:        status = "Not Eligible"    else:        status = "Eligible"    students.append((name, pending_fee, status, reasons))print("\n--- UNIVERSITY ELIGIBILITY AUDIT REPORT ---")for student in students:



5. Sample Input
Enter number of students: 3

Enter details of student 1
Enter student name: Ravi
Enter total fee: 50000
Enter paid fee: 50000
Enter attendance percentage: 85
Enter internal marks: 45

Enter details of student 2
Enter student name: Sita
Enter total fee: 50000
Enter paid fee: 30000
Enter attendance percentage: 80
Enter internal marks: 50

Enter details of student 3
Enter student name: Kumar
Enter total fee: 50000
Enter paid fee: 50000
Enter attendance percentage: 60
Enter internal marks: 30


6. Sample Output
--- UNIVERSITY ELIGIBILITY AUDIT REPORT ---

Student Name: Ravi
Pending Fee: 0.0
Status: Eligible
Reasons: None

Student Name: Sita
Pending Fee: 20000.0
Status: Not Eligible
Reasons: Fee Pending

Student Name: Kumar
Pending Fee: 0.0
Status: Not Eligible
Reasons: Low Attendance, Low Internal Marks

--- AUDIT COMPLETED ---
