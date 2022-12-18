def treesVisible():
    # all trees in border are visible
    # find trees visible in interior from left right top down directions
    with open("day8.dat", "r") as f:
        lines = f.readlines()
        visibility = []
        for line in lines:
            line = line.rstrip()
            tmp = []
            for x in line:
                tmp.append(False)
            visibility.append(tmp)
        
        # set border visibility
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()
            for j in range(len(lines[i])):
                if i == 0 or (i == len(lines) - 1) or j == 0 or (j == len(lines[i]) - 1):
                    visibility[i][j] = True

        # check interior visibility  
        for i in range(1, len(lines) - 1):
            lines[i] = lines[i].rstrip()
            for j in range(1, len(lines[i]) - 1):

                tempj = j + 1
                keeplooking = True
                while tempj < len(lines[i]) and keeplooking:
                    if lines[i][tempj] >= lines[i][j]:
                        keeplooking = False
                    tempj += 1
                if keeplooking: visibility[i][j] = True

                tempj = j - 1
                keeplooking = True
                while tempj >= 0 and keeplooking:
                    if lines[i][tempj] >= lines[i][j]:
                        keeplooking = False
                    tempj -= 1
                if keeplooking: visibility[i][j] = True

                tempi = i - 1
                keeplooking = True
                while tempi >= 0 and keeplooking:
                    if lines[tempi][j] >= lines[i][j]:
                        keeplooking = False
                    tempi -= 1
                if keeplooking: visibility[i][j] = True

                tempi = i + 1
                keeplooking = True
                while tempi < len(lines) and keeplooking:
                    if lines[tempi][j] >= lines[i][j]:
                        keeplooking = False
                    tempi += 1
                if keeplooking: visibility[i][j] = True

        return sum(item.count(True) for item in visibility)

print(treesVisible())
