1. Problem Statement
Develop a Python program to process courier package weights, destination zones, vehicle capacities and delivery priorities. Allocate packages to suitable vehicles based on their capacity and identify packages that cannot be dispatched.
2. Algorithm
1. Start the program.
2. Read the number of packages and vehicles.
3. Enter package ID, weight, destination zone and priority.
4. Enter vehicle ID, destination zone and capacity.
5. Sort packages according to priority.
6. Check destination zone and vehicle capacity.
7. Allocate packages to suitable vehicles.
8. Update the remaining vehicle capacity.
9. Identify packages that cannot be dispatched.
10. Display the dispatch report.
11. Stop the program.
3. Flowchart (Mermaid Code)
#chatgpt-mermaid-_r_ir_{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;fill:rgb(13, 13, 13);}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#chatgpt-mermaid-_r_ir_ .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_ir_ .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#chatgpt-mermaid-_r_ir_ .error-icon{fill:rgb(243, 243, 243);}#chatgpt-mermaid-_r_ir_ .error-text{fill:rgb(13, 13, 13);stroke:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .edge-thickness-normal{stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .edge-thickness-thick{stroke-width:3.5px;}#chatgpt-mermaid-_r_ir_ .edge-pattern-solid{stroke-dasharray:0;}#chatgpt-mermaid-_r_ir_ .edge-thickness-invisible{stroke-width:0;fill:none;}#chatgpt-mermaid-_r_ir_ .edge-pattern-dashed{stroke-dasharray:3;}#chatgpt-mermaid-_r_ir_ .edge-pattern-dotted{stroke-dasharray:2;}#chatgpt-mermaid-_r_ir_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_ir_ .marker.cross{stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_ir_ svg{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:16px;}#chatgpt-mermaid-_r_ir_ p{margin:0;}#chatgpt-mermaid-_r_ir_ .label{font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .cluster-label text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .cluster-label span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .cluster-label span p{background-color:transparent;}#chatgpt-mermaid-_r_ir_ .label text,#chatgpt-mermaid-_r_ir_ span{fill:rgb(13, 13, 13);color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .node rect,#chatgpt-mermaid-_r_ir_ .node circle,#chatgpt-mermaid-_r_ir_ .node ellipse,#chatgpt-mermaid-_r_ir_ .node polygon,#chatgpt-mermaid-_r_ir_ .node path{fill:rgb(222, 234, 251);stroke:rgb(83, 154, 248);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .rough-node .label text,#chatgpt-mermaid-_r_ir_ .node .label text,#chatgpt-mermaid-_r_ir_ .image-shape .label,#chatgpt-mermaid-_r_ir_ .icon-shape .label{text-anchor:middle;}#chatgpt-mermaid-_r_ir_ .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .rough-node .label,#chatgpt-mermaid-_r_ir_ .node .label,#chatgpt-mermaid-_r_ir_ .image-shape .label,#chatgpt-mermaid-_r_ir_ .icon-shape .label{text-align:center;}#chatgpt-mermaid-_r_ir_ .node.clickable{cursor:pointer;}#chatgpt-mermaid-_r_ir_ .root .anchor path{fill:rgb(143, 143, 143)!important;stroke-width:0;stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_ir_ .arrowheadPath{fill:rgb(143, 143, 143);}#chatgpt-mermaid-_r_ir_ .edgePath .path{stroke:rgb(143, 143, 143);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .flowchart-link{stroke:rgb(143, 143, 143);fill:none;}#chatgpt-mermaid-_r_ir_ .edgeLabel{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_ir_ .edgeLabel p{background-color:rgb(252, 252, 252);}#chatgpt-mermaid-_r_ir_ .edgeLabel rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_ir_ .labelBkg{background-color:rgba(252, 252, 252, 0.5);}#chatgpt-mermaid-_r_ir_ .cluster rect{fill:rgb(243, 243, 243);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .cluster text{fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ .cluster span{color:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";font-size:12px;background:rgb(243, 243, 243);border:1px solid rgba(0, 0, 0, 0.1);border-radius:2px;pointer-events:none;z-index:100;}#chatgpt-mermaid-_r_ir_ .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgb(13, 13, 13);}#chatgpt-mermaid-_r_ir_ rect.text{fill:none;stroke-width:0;}#chatgpt-mermaid-_r_ir_ .icon-shape,#chatgpt-mermaid-_r_ir_ .image-shape{background-color:rgb(252, 252, 252);text-align:center;}#chatgpt-mermaid-_r_ir_ .icon-shape p,#chatgpt-mermaid-_r_ir_ .image-shape p{background-color:rgb(252, 252, 252);padding:2px;}#chatgpt-mermaid-_r_ir_ .icon-shape .label rect,#chatgpt-mermaid-_r_ir_ .image-shape .label rect{opacity:0.5;background-color:rgb(252, 252, 252);fill:rgb(252, 252, 252);}#chatgpt-mermaid-_r_ir_ .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#chatgpt-mermaid-_r_ir_ .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#chatgpt-mermaid-_r_ir_ .node .neo-node{stroke:rgb(83, 154, 248);}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node rect,#chatgpt-mermaid-_r_ir_ [data-look="neo"].cluster rect,#chatgpt-mermaid-_r_ir_ [data-look="neo"].node polygon{stroke:url(#chatgpt-mermaid-_r_ir_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ir_ [data-look="neo"].swimlane.cluster rect{filter:none;}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node path{stroke:url(#chatgpt-mermaid-_r_ir_-gradient);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node .neo-line path{stroke:rgb(83, 154, 248);filter:none;}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node circle{stroke:url(#chatgpt-mermaid-_r_ir_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ir_ [data-look="neo"].node circle .state-start{fill:#000000;}#chatgpt-mermaid-_r_ir_ [data-look="neo"].icon-shape .icon{fill:url(#chatgpt-mermaid-_r_ir_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ir_ [data-look="neo"].icon-shape .icon-neo path{stroke:url(#chatgpt-mermaid-_r_ir_-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#chatgpt-mermaid-_r_ir_ .node text{font-size:14px;font-weight:600;letter-spacing:normal;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_ir_ .edgeLabels text{font-size:13px;font-weight:600;letter-spacing:-0.08px;fill:rgb(0, 79, 153);}#chatgpt-mermaid-_r_ir_ .node tspan[font-weight="normal"],#chatgpt-mermaid-_r_ir_ .edgeLabels tspan[font-weight="normal"]{font-weight:600;}#chatgpt-mermaid-_r_ir_ .edgeLabel .label rect{opacity:1;rx:13px;ry:13px;fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .node rect,#chatgpt-mermaid-_r_ir_ .node circle,#chatgpt-mermaid-_r_ir_ .node ellipse,#chatgpt-mermaid-_r_ir_ .node polygon,#chatgpt-mermaid-_r_ir_ .node path{fill:rgb(229, 243, 255);stroke:rgba(0, 0, 0, 0.1);stroke-width:1px;}#chatgpt-mermaid-_r_ir_ .node rect{rx:16px;ry:16px;}#chatgpt-mermaid-_r_ir_ .mermaid-decision .label-container{fill:rgb(245, 250, 255);stroke:rgb(206, 219, 229);stroke-dasharray:2,2;}#chatgpt-mermaid-_r_ir_ .edgePaths .flowchart-link{stroke:rgb(143, 143, 143);stroke-width:1px;stroke-linecap:round;stroke-linejoin:round;}#chatgpt-mermaid-_r_ir_ .marker{fill:rgb(143, 143, 143);stroke:rgb(143, 143, 143);}#chatgpt-mermaid-_r_ir_ :root{--mermaid-font-family:-apple-system-body,ui-sans-serif,-apple-system,system-ui,"Segoe UI",Helvetica,"Apple Color Emoji",Arial,sans-serif,"Segoe UI Emoji","Segoe UI Symbol";}StartEnter packages and vehiclesSort packages by prioritySelect next packageMatching zone vehicleavailable?Mark package as notdispatchedWeight <= Remainingcapacity?Check another matchingvehicleAnother vehicle available?Allocate package to vehicleUpdate remaining capacityMore packages?Display dispatch reportStopNoYesNoYesNoYesYesNo





4. Python Source Code
packages = []vehicles = []n = int(input("Enter number of packages: "))for i in range(n):    print("\nPackage", i + 1)    pid = input("Package ID: ")    weight = float(input("Weight: "))    zone = input("Destination zone: ")    priority = int(input("Priority (1=High): "))    packages.append([pid, weight, zone, priority])m = int(input("\nEnter number of vehicles: "))for i in range(m):    print("\nVehicle", i + 1)    vid = input("Vehicle ID: ")    zone = input("Destination zone: ")    capacity = float(input("Capacity: "))    vehicles.append([vid, zone, capacity, []])packages.sort(key=lambda x: x[3])not_dispatched = []for p in packages:    allocated = False    for v in vehicles:        if v[1] == p[2] and v[2] >= p[1]:



5. Sample Input
Enter number of packages: 3

Package 1
Package ID: P101
Weight: 20
Destination zone: A
Priority: 2

Package 2
Package ID: P102
Weight: 40
Destination zone: B
Priority: 1

Package 3
Package ID: P103
Weight: 60
Destination zone: A
Priority: 1

Enter number of vehicles: 2

Vehicle 1
Vehicle ID: V1
Destination zone: A
Capacity: 50

Vehicle 2
Vehicle ID: V2
Destination zone: B
Capacity: 50


6. Sample Output
--- DISPATCH REPORT ---

Vehicle: V1
Zone: A
Packages: ['P101']
Remaining Capacity: 30.0

Vehicle: V2
Zone: B
Packages: ['P102']
Remaining Capacity: 10.0

Not Dispatched Packages: ['P103']
