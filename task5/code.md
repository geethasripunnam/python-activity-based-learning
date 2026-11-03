1. Problem Statement
Develop a Python program to validate student records stored using lists and tuples. Check student IDs, names, marks, attendance and course details. Identify duplicate records, missing values and inconsistent academic information.
2. Algorithm
1. Start the program.
2. Read the number of student records.
3. Enter student ID, name, marks, attendance and course.
4. Check for duplicate student IDs.
5. Check for missing values.
6. Validate marks between 0 and 100.
7. Validate attendance between 0 and 100.
8. Identify invalid records.
9. Display valid and inconsistent records.
10. Stop the program.
3. Flowchart (Mermaid Code)
   flowchart TD
    A([Start]) --> B[/Enter number of students/]
    B --> C[/Enter student record/]
    C --> D{Duplicate ID?}
    D -- Yes --> E[Record duplicate error]
    D -- No --> F{Any missing values?}
    F -- Yes --> G[Record missing value error]
    F -- No --> H{Marks and attendance valid?}
    H -- No --> I[Record invalid academic data]
    H -- Yes --> J[Mark record as valid]
    E --> K{More records?}
    G --> K
    I --> K
    J --> K
    K -- Yes --> C
    K -- No --> L[/Display consistency report/]
    L --> M([Stop])
5. Sample Input
Enter number of students: 3

Student 1
Student ID: 101
Student Name: Ravi
Marks: 85
Attendance: 90
Course: AIML

Student 2
Student ID: 102
Student Name: Sita
Marks: 75
Attendance: 80
Course: CSE

Student 3
Student ID: 101
Student Name: Kumar
Marks: 110
Attendance: 85
Course: AIML
6. Sample Output
--- VALID STUDENT RECORDS ---
('101', 'Ravi', '85', '90', 'AIML')
('102', 'Sita', '75', '80', 'CSE')

--- INCONSISTENT RECORDS ---
101 : Duplicate ID, Invalid Marks

Total Records: 3
Valid Records: 2
Invalid Records: 1
