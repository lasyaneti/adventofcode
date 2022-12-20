def headTail():
    lines = open("day9.dat", "r").readlines()
    # dont have to build the board itself
    # just keep track of points visited in the coordinate system 
    tvisited = []
    h = (0, 0)
    t = (0, 0)
    tvisited.append(t)

    for line in lines:
        line = line.rstrip()

        for i in range(int(line[2:])):

            # move head one step at a time
            if line[0] == "R":
                h = (h[0] + 1, h[1])
            elif line[0] == "L":
                h = (h[0] - 1, h[1])
            elif line[0] == "U":
                h = (h[0], h[1] + 1)
            elif line[0] == "D":
                h = (h[0], h[1] - 1)

            # update t if needed
            while abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
                # move vertically, already in same row
                if (h[0] == t[0] and h[1] != t[1]):
                    if (h[1] > t[1]):
                        t = (t[0], t[1] + 1)
                    if (t[1] > h[1]):
                        t = (t[0], t[1] - 1)

                # move horizontally, already in same col
                elif (h[0] != t[0] and h[1] == t[1]):
                    if (h[0] > t[0]):
                        t = (t[0] + 1, t[1])
                    if (t[0] > h[0]):
                        t = (t[0] - 1, t[1])

                # move diagonally, neither in same row nor col 
                else:
                    if (h[0] > t[0] and h[1] > t[1]):
                        t = (t[0] + 1, t[1] + 1)
                    elif (h[0] < t[0] and h[1] < t[1]):
                        t = (t[0] - 1, t[1] - 1)
                    elif (h[0] > t[0] and h[1] < t[1]):
                        t = (t[0] + 1, t[1] - 1)
                    elif (h[0] < t[0] and h[1] > t[1]):
                        t = (t[0] - 1, t[1] + 1)
                
                # add new t to list!!! 
                if t not in tvisited:
                    tvisited.append(t)

    return len(tvisited)

print(headTail())