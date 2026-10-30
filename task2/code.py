 Python Source Code
students = []n = int(input("Enter number of students: "))for i in range(n):   
  print("\nEnter details of student", i + 1)   
  name = input("Enter student name: ")   
  total_fee = float(input("Enter total fee: "))   
  paid_fee = float(input("Enter paid fee: "))   
  attendance = float(input("Enter attendance percentage: "))   
  marks = float(input("Enter internal marks: "))   
  pending_fee = total_fee - paid_fee    reasons = []  
  if pending_fee > 0:       
    reasons.append("Fee Pending")   
    if attendance < 75:      
      reasons.append("Low Attendance")   
      if marks < 40:       
        reasons.append("Low Internal Marks")   
        if reasons:      
          status = "Not Eligible"   
        else:       
          status = "Eligible"   
          students.append((name, pending_fee, status, reasons))
          print("\n--- UNIVERSITY ELIGIBILITY AUDIT REPORT ---")for student in students:
