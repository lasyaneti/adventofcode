def rckPprSci():
    # given A rock, B paper, C scissors
    # +0 X loss, +3 Y draw, +6 Z win
    # +1 rock, +2 paper, +3 scissors 
    score = 0
    with open("day2-1.dat", "r") as f:
        lines = f.readlines()
        for line in lines:
            if ("A" in line):
                # p1 played rock
                if ("X" in line):
                    score += 3 # 3 + 0
                elif ("Y" in line):
                    score += 4 # 1 + 3
                elif ("Z" in line):
                    score += 8 # 2 + 6
            
            elif ("B" in line):
                # p1 played paper
                if ("X" in line):
                    score += 1 # 1 + 0
                elif ("Y" in line):
                    score += 5 # 2 + 3
                elif ("Z" in line):
                    score += 9 # 3 + 6

            elif ("C" in line):
                # p1 played scissors 
                if ("X" in line):
                    score += 2 # 2 + 0
                elif ("Y" in line):
                    score += 6 # 3 + 3
                elif ("Z" in line):
                    score += 7 # 1 + 6
    
    return score


print(rckPprSci())