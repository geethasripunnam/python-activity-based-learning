Python Source Code
students = []eligible = []rejected = []n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))
for i in range(n):    
  print("\nEnter details of student", i + 1)   
  name = input("Enter name: ")   
  marks = float(input("Enter marks: "))   
  attendance = float(input("Enter attendance: "))   
  income = float(input("Enter family income: "))    
  reasons = []    if marks < 75:       
  reasons.append("Low Marks")   
  if attendance < 75:       
    reasons.append("Low Attendance")   
    if income > 200000:      
      reasons.append("High Income")   
      if len(reasons) == 0:       
        eligible.append((name, marks, attendance, income))    
      else:        rejected.append((name, reasons))eligible.sort(key=lambda x: x[1], reverse=True)selected = eligible[:quota]waiting = eligible[quota:]
      print("\n--- SELECTED STUDENTS ---")for student in selected:    
        print(student)print("\n--- WAITING LIST ---")for student in waiting:  
        print(student)print("\n--- REJECTED STUDENTS ---")for student, reasons in rejected:   
        print(student, "-", ", ".join(reasons))

