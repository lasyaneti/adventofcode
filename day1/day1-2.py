def topThreeElves():
    calsums = []
    with open("day1-1.dat", "r") as f:
        currsum = 0
        lines = f.readlines()

        for line in lines:
            if line == "\n":
                calsums.append(currsum)
                currsum = 0
            else:
                currsum += int(line)
    
    return sum(sorted(calsums, reverse=True)[0:3])


print(topThreeElves())