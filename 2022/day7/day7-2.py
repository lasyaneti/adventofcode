def getDir(setName):
    direc = {}
    direc["type"] = "dir"
    direc["name"] = setName
    direc["size"] = 0
    direc["contents"] = [] # to fill after ls 
    return direc

def getFile(setSize):
    file = {}
    file["type"] = "file"
    file["size"] = setSize
    file["contents"] = None
    return file

def assignment():
    with open("day7.dat", "r") as f:

        # tree approach too complicated
        filesystem = {}
        filesystem["/"] = getDir("/")
        lines = f.readlines()
        path = "/"
        
        for line in lines[1:]:

            if line == "$ cd ..\n":
                path = path[:-1]
                while path[-1] != "/":
                    path = path[:-1]

            elif line != "$ cd /\n" and "$ cd" in line:
                path += line.split(" ")[2].rstrip() + "/"
                filesystem[path] = getDir(path)

            elif "dir" in line:
                filesystem[path]["contents"].append(getDir(path + line.split(" ")[1].rstrip() + "/"))
            
            elif "$ ls" not in line:
                newFile = getFile(line.split(" ")[0])
                filesystem[path]["contents"].append(newFile)
    
    # calculate directory sizes 
    sums = []
    for key, item in reversed(filesystem.items()):
        if item["type"] == "dir":
            tot = 0
            for bruh in item["contents"]:
                if bruh["type"] == "dir":
                    tot += int(filesystem[bruh["name"]]["size"])
                else:
                    tot += int(bruh["size"])
        filesystem[key]["size"] = str(tot)
        sums.append(tot)
    
    # find which directory to delete
    spaceNeeded = 30000000 - (70000000 - int(filesystem["/"]["size"]))
    toDelete = int(filesystem["/"]["size"])
    for key, val in filesystem.items():
        if int(val["size"]) >= spaceNeeded and int(val["size"]) < toDelete:
            toDelete = int(val["size"])

    return toDelete

print(assignment())
