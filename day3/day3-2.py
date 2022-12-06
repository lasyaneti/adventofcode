import string 

def elfGroups():
    groupBadgeSum = 0
    with open("day3.dat", "r") as f:
        lines = f.readlines()
        
        for i in range(0, len(lines), 3):
            for c in lines[i]:
                if c in lines[i + 1] and c in lines[i + 2]:
                    if c.lower() == c:
                        groupBadgeSum += (ord(c.lower()) % 96)
                    else:
                        groupBadgeSum += (ord(c.lower()) % 96 + 26)
                    break

    return groupBadgeSum


print(elfGroups())