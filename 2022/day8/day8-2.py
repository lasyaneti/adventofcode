def highestScenicScore():
    with open("day8.dat", "r") as f:
        lines = f.readlines()
        maxScore = 0

        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()
            for j in range(len(lines[i])):
                
                rightScore = 0
                tempj = j + 1
                keeplooking = True
                while tempj < len(lines[i]) and keeplooking:
                    if lines[i][tempj] < lines[i][j]:
                        rightScore += 1
                    else: 
                        rightScore += 1
                        keeplooking = False
                    tempj += 1

                leftScore = 0
                tempj = j - 1
                keeplooking = True
                while tempj >= 0 and keeplooking:
                    if lines[i][tempj] < lines[i][j]:
                        leftScore += 1
                    else: 
                        leftScore += 1
                        keeplooking = False
                    tempj -= 1

                topScore = 0
                tempi = i - 1
                keeplooking = True
                while tempi >= 0 and keeplooking:
                    if lines[tempi][j] < lines[i][j]:
                        topScore += 1
                    else: 
                        topScore += 1
                        keeplooking = False
                    tempi -= 1

                downScore = 0
                tempi = i + 1
                keeplooking = True
                while tempi < len(lines) and keeplooking:
                    if lines[tempi][j] < lines[i][j]:
                        downScore += 1
                    else: 
                        downScore += 1
                        keeplooking = False
                    tempi += 1
            
                if topScore * downScore * leftScore * rightScore > maxScore:
                    maxScore = topScore * downScore * leftScore * rightScore

        return maxScore

print(highestScenicScore())
