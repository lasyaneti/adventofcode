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
    
    # find directory sums above 100k
    toRet = 0
    for sum in sums:
        if sum <= 100000:
            toRet += sum

    return toRet

print(assignment())

# class TreeNode:
#     # dir = have children, size set after tree built?  
#     # file = leaf, size set when initialized 
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.size = 0

# def assignment():
#     with open("day7.dat", "r") as f:

#         # directories are fundamentally TREES
#         # iterate through commands and build tree
#         lines = f.readlines()
#         root = TreeNode("/")
#         root.size = 20

#         fillChildren = False 
#         curr = root 

#         for line in lines:

#             if line == "$ ls\n":
#                 fillChildren = True

#             if line == "$ ls\n" and not fillChildren:
#                 fillChildren = False

#             while fillChildren and line != "$ ls\n":
#                 curr.children.append(line)



#         # recurse tree and find sum

# assignment()