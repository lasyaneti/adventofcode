def assignment():
    overlaps = 0
    with open("day4.dat", "r") as f:
        lines = f.readlines()
        
        for line in lines:
            pair = line.split(",")
            
            if int(pair[0].split("-")[0]) >= int(pair[1].split("-")[0]) and int(pair[0].split("-")[1]) <= int(pair[1].split("-")[1]):
                overlaps += 1
            
            elif int(pair[1].split("-")[0]) >= int(pair[0].split("-")[0]) and int(pair[1].split("-")[1]) <= int(pair[0].split("-")[1]):
                overlaps += 1

    return overlaps

print(assignment())