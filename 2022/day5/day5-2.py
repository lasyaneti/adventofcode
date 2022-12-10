def assignment():
    with open("day5.dat", "r") as f:
        lines = f.readlines()
        
        crates = [[], [], [], [], [], [], [], [], []]
        cratecomplete = False
        cratecleaned = False

        for line in lines:
            if line == "\n":
                cratecomplete = True

            if cratecomplete and cratecleaned:
                orders = line.split(" ")
                numtomove = int(orders[1])
                movefrom = int(orders[3]) - 1
                moveto = int(orders[5]) - 1
                bruh = []
                for i in range(numtomove):
                    
                    if len(crates[movefrom]) != 0:
                        bruh.append(crates[movefrom][-1])
                        crates[movefrom].pop()
                
                bruh.reverse()
                crates[moveto].extend(bruh)
            
            if cratecomplete and not cratecleaned:
                for stack in crates:
                    while " " in stack:
                        stack.remove(" ")
                    if len(stack) != 0:
                        stack.pop()
                        stack.reverse()
                cratecleaned = True

            if not cratecomplete:
                temp = line[1::4]
                i = 0
                for t in temp:
                    crates[i].append(t)
                    i += 1
        
        cratetops = ""
        for stack in crates:
            if len(stack) != 0:
                cratetops += stack[-1]
            
    return cratetops

print(assignment())