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
#chatgpt-mermaid-_r_kn_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_kn_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_kn_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_kn_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-_r_kn_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_kn_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_kn_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_kn_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_kn_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_kn_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_kn_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_kn_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_kn_ p{margin:0;}#chatgpt-mermaid-_r_kn_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_kn_ .label text,#chatgpt-mermaid-_r_kn_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .node rect,#chatgpt-mermaid-_r_kn_ .node circle,#chatgpt-mermaid-_r_kn_ .node ellipse,#chatgpt-mermaid-_r_kn_ .node polygon,#chatgpt-mermaid-_r_kn_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .rough-node .label text,#chatgpt-mermaid-_r_kn_ .node .label text,#chatgpt-mermaid-_r_kn_ .image-shape .label,#chatgpt-mermaid-_r_kn_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_kn_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .rough-node .label,#chatgpt-mermaid-_r_kn_ .node .label,#chatgpt-mermaid-_r_kn_ .image-shape .label,#chatgpt-mermaid-_r_kn_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_kn_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_kn_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_kn_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-_r_kn_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-_r_kn_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_kn_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-_r_kn_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_kn_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-_r_kn_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_kn_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_kn_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_kn_ .icon-shape,#chatgpt-mermaid-_r_kn_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_kn_ .icon-shape p,#chatgpt-mermaid-_r_kn_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-_r_kn_ .icon-shape .label rect,#chatgpt-mermaid-_r_kn_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_kn_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_kn_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_kn_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_kn_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_kn_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_kn_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_kn_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_kn_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_kn_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_kn_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_kn_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_kn_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_kn_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_kn_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_kn_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_kn_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_kn_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_kn_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_kn_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .node rect,#chatgpt-mermaid-_r_kn_ .node circle,#chatgpt-mermaid-_r_kn_ .node ellipse,#chatgpt-mermaid-_r_kn_ .node polygon,#chatgpt-mermaid-_r_kn_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_kn_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_kn_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_kn_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_kn_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_kn_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of participantsEnter participant ID and feeID already exists?Record duplicate IDStore registrationMore participants?Calculate registration incomeEnter sponsorship amountEnter festival expensesCalculate total incomeCalculate final balanceDisplay audit reportStopYesNoYesNo





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
