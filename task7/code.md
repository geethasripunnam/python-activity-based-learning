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
#chatgpt-mermaid-_r_m5_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_m5_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_m5_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_m5_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-_r_m5_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_m5_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_m5_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_m5_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_m5_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_m5_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_m5_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_m5_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_m5_ p{margin:0;}#chatgpt-mermaid-_r_m5_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_m5_ .label text,#chatgpt-mermaid-_r_m5_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .node rect,#chatgpt-mermaid-_r_m5_ .node circle,#chatgpt-mermaid-_r_m5_ .node ellipse,#chatgpt-mermaid-_r_m5_ .node polygon,#chatgpt-mermaid-_r_m5_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .rough-node .label text,#chatgpt-mermaid-_r_m5_ .node .label text,#chatgpt-mermaid-_r_m5_ .image-shape .label,#chatgpt-mermaid-_r_m5_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_m5_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .rough-node .label,#chatgpt-mermaid-_r_m5_ .node .label,#chatgpt-mermaid-_r_m5_ .image-shape .label,#chatgpt-mermaid-_r_m5_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_m5_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_m5_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_m5_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-_r_m5_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-_r_m5_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_m5_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-_r_m5_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_m5_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-_r_m5_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_m5_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_m5_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_m5_ .icon-shape,#chatgpt-mermaid-_r_m5_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_m5_ .icon-shape p,#chatgpt-mermaid-_r_m5_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-_r_m5_ .icon-shape .label rect,#chatgpt-mermaid-_r_m5_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_m5_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_m5_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_m5_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_m5_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_m5_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_m5_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_m5_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_m5_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_m5_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_m5_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_m5_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_m5_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_m5_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_m5_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_m5_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_m5_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_m5_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_m5_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_m5_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .node rect,#chatgpt-mermaid-_r_m5_ .node circle,#chatgpt-mermaid-_r_m5_ .node ellipse,#chatgpt-mermaid-_r_m5_ .node polygon,#chatgpt-mermaid-_r_m5_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_m5_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_m5_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_m5_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_m5_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_m5_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter number of students andsubjectsEnter student name and marksCalculate original totalSubject mark below 40?Shortage <= 5?Add required grace marksMark subject as failedKeep original marksCheck maximum marksCalculate moderated totalMore students?Display original andmoderated resultsStopYesYesNoNoYesNo





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
