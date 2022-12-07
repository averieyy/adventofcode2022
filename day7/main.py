directories = {

}

rawinput = ""
with open("./input.txt", 'r') as f:
    rawinput = f.read()

# rawinput = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""

# Low answer

commands = rawinput.split("$")
totalsize = 0

class Directory:
    def __init__(self, name, containing) -> None:
        self.name = name
        self.rawcontaining = containing
        self.sizeCalc = False
        self.size = 0
        pass
    def calculateSize (self):
        self.sizeCalc = True
        for item in self.rawcontaining:
            arg = item.split(" ")
            if arg[0] == "dir":
                if self.name+"/"+arg[1] in directories:
                    self.size += directories[self.name+"/"+arg[1]].getSize()
            else:
                self.size += int(arg[0])

    def getSize(self) -> int:
        if self.sizeCalc == True:
            return self.size
        else:
            self.calculateSize()
            return self.size

currentpath = []

for i in range(len(commands)):
    k = commands[i]
    k = k.strip()
    if k.startswith("ls"):
        earlier = commands[i-1].strip()
        currentpath.append(earlier.split(" ")[1])
        directories['/'.join(currentpath)] = Directory('/'.join(currentpath), k.split("\n")[1:])
    elif k == "cd ..":
        currentpath.pop()

# for i in directories:
#     print (i)
#     if directories[i].getSize() <= 100000:
#         totalsize += directories[i].getSize()
# print(totalsize)

lowestavailable = 100000000000000000
for i in directories:
    print(i, directories[i].getSize())
    if directories["/"].getSize()-directories[i].getSize() < 40000000 and directories[i].getSize() < lowestavailable:
        lowestavailable = directories[i].getSize()
print(lowestavailable)