def assignment2():
    overlaps = 0
    with open("day4.dat", "r") as f:
        lines = f.readlines()
        
        for line in lines:
            pair = line.split(",")
            
            min1 = int(pair[0].split("-")[0])
            max1 = int(pair[0].split("-")[1])
            min2 = int(pair[1].split("-")[0])
            max2 = int(pair[1].split("-")[1])

            for i in range(min1, max1+1):
                broken = False
                for j in range(min2, max2+1):
                    if i == j:
                        overlaps += 1
                        broken = True
                        break
                if broken:
                    break


    return overlaps

print(assignment2())

