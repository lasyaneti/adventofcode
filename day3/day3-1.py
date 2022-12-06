import string 

def rucksack():
    duplicatesum = 0
    with open("day3.dat", "r") as f:
        lines = f.readlines()
        for line in lines:
            
            mid = int(len(line)/2)
            firsthalf = line[:mid]
            secondhalf = line[mid:]

            for c in firsthalf:
                if c in secondhalf:
                    # lowercase
                    if c.lower() == c:
                        duplicatesum += (ord(c.lower()) % 96)
                        
                    # uppercase
                    else:
                        duplicatesum += (ord(c.lower()) % 96 + 26)

                    break # given only 1 item per rucksack

    return duplicatesum


print(rucksack())