Python Source Code
packages = []vehicles = []n = int(input("Enter number of packages: "))
for i in range(n):    
  print("\nPackage", i + 1)   
  pid = input("Package ID: ")  
  weight = float(input("Weight: "))   
  zone = input("Destination zone: ")    
  priority = int(input("Priority (1=High): "))  
  packages.append([pid, weight, zone, priority])m = int(input("\nEnter number of vehicles: "))
  for i in range(m):   
    print("\nVehicle", i + 1)   
    vid = input("Vehicle ID: ")   
    zone = input("Destination zone: ")   
    capacity = float(input("Capacity: "))   
    vehicles.append([vid, zone, capacity, []])packages.sort(key=lambda x: x[3])not_dispatched = []
    for p in packages:   
      allocated = False   
      for v in vehicles:        
      if v[1] == p[2] and v[2] >= p[1]:

