def assignment():
    with open("day6.dat", "r") as f:
        lines = f.readlines()

        for line in lines:
            for i in range(len(line)):
                chars = []
                broken = False
                for j in range(i, len(line)):
                    if line[j] in chars:
                        break
                    if line[j] not in chars:
                        chars.append(line[j])
                    if len(chars) == 4:
                        print(chars)
                        print(j+1) 
                        broken = True
                        break
                if broken:
                    break

assignment()