

## 1. Problem Statement

Develop a Python program to calculate electricity bills for multiple apartments using progressive tariff rates, fixed charges, and rebates. The program should calculate apartment-wise electricity charges based on consumption units, identify billing discrepancies, and rank apartments according to their electricity consumption. Finally, display the total bill and consumption ranking of all apartments.

## 2. Algorithm

1. Start the program.
2. Enter the number of apartments.
3. Enter each apartment name and electricity consumption units.
4. Calculate electricity charges using progressive tariffs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Above 200 units: ₹5 per unit.
5. Add a fixed charge of ₹50.
6. Apply a 10% rebate if consumption is below 100 units.
7. Calculate the final electricity bill.
8. Check for billing discrepancies.
9. Store apartment details and bills.
10. Rank apartments based on electricity consumption.
11. Display apartment-wise bills and rankings.
12. Stop the program.

## 3. Flowchart (Mermaid Code)


```mermaid
flowchart TD
    A([Start]) --> B[/Enter number of apartments/]
    B --> C[/Enter apartment name and units/]
    C --> D{Units <= 100?}
    D -- Yes --> E[Calculate units * 2]
    D -- No --> F{Units <= 200?}
    F -- Yes --> G[Calculate 100*2 + remaining*3]
    F -- No --> H[Calculate 100*2 + 100*3 + remaining*5]
    E --> I[Add fixed charge 50]
    G --> I
    H --> I
    I --> J{Units < 100?}
    J -- Yes --> K[Apply 10 percent rebate]
    J -- No --> L[No rebate]
    K --> M[Calculate final bill]
    L --> M
    M --> N[Check billing discrepancy]
    N --> O[Store apartment details]
    O --> P{More apartments?}
    P -- Yes --> C
    P -- No --> Q[Rank apartments by consumption]
    Q --> R[/Display bills and rankings/]
    R --> S([Stop])
```



      

## 5. Sample Input

```
SMART ELECTRICITY BILLING SYSTEM
Enter number of apartments: 3

Apartment 1
Enter apartment name: A101
Enter electricity units: 80
Enter previous calculated bill: 194

Apartment 2
Enter apartment name: A102
Enter electricity units: 150
Enter previous calculated bill: 400

Apartment 3
Enter apartment name: A103
Enter electricity units: 250
Enter previous calculated bill: 1050
```

## 6. Sample Output

```
--- ELECTRICITY BILL REPORT ---

Apartment: A101
Units Consumed: 80
Final Bill: Rs. 194.0
Billing Status: No Discrepancy

Apartment: A102
Units Consumed: 150
Final Bill: Rs. 400.0
Billing Status: No Discrepancy

Apartment: A103
Units Consumed: 250
Final Bill: Rs. 1050.0
Billing Status: No Discrepancy

--- CONSUMPTION RANKING ---

1 A103 - 250 units
2 A102 - 150 units
3 A101 - 80 units
```


