1. Problem Statement
Develop a Python program to manage campus festival registrations and financial records. Verify participant registrations, calculate registration fee collections, add sponsorship contributions, calculate total expenses, detect duplicate registrations and display the final financial balance.
2. Algorithm
1. Start the program.
2. Read the number of participants.
3. Enter participant ID and registration fee.
4. Check duplicate participant IDs.
5. Store valid registrations.
6. Calculate total registration fees.
7. Enter sponsorship contributions.
8. Enter festival expenses.
9. Calculate total income.
10. Calculate final balance by subtracting expenses from income.
11. Display duplicate registrations and financial report.
12. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-


4. Python Source Code
participants = []duplicates = []n = int(input("Enter number of participants: "))for i in range(n):    print("\nParticipant", i + 1)    pid = input("Enter participant ID: ")    fee = float(input("Enter registration fee: "))    if pid in [p[0] for p in participants]:        duplicates.append(pid)    else:        participants.append((pid, fee))sponsorship = float(input("\nEnter sponsorship amount: "))expenses = float(input("Enter total expenses: "))registration_income = sum(p[1] for p in participants)total_income = registration_income + sponsorshipbalance = total_income - expensesprint("\n--- FESTIVAL FINANCIAL AUDIT ---")print("Valid Participants:", len(participants))print("Registration Income: Rs.", registration_income)print("Sponsorship: Rs.", sponsorship)print("Total Income: Rs.", total_income)print("Total Expenses: Rs.", expenses)print("Final Balance: Rs.", balance)print("Duplicate IDs:", duplicates)



5. Sample Input
Enter number of participants: 4

Participant 1
Enter participant ID: S101
Enter registration fee: 500

Participant 2
Enter participant ID: S102
Enter registration fee: 500

Participant 3
Enter participant ID: S103
Enter registration fee: 500

Participant 4
Enter participant ID: S101
Enter registration fee: 500

Enter sponsorship amount: 5000
Enter total expenses: 3000


6. Sample Output
--- FESTIVAL FINANCIAL AUDIT ---

Valid Participants: 3
Registration Income: Rs. 1500.0
Sponsorship: Rs. 5000.0
Total Income: Rs. 6500.0
Total Expenses: Rs. 3000.0
Final Balance: Rs. 3500.0
Duplicate IDs: ['S101']
Financial Status: Profit
