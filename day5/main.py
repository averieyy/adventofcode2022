rawinput = ""
with open('./input.txt', 'r') as f:
    rawinput = f.read()

# rawinput = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

rawlayout = rawinput.split("\n\n")[0]
layoutlist = rawlayout.split("\n")
moves = rawinput.split('\n\n')[1]

print(moves)

# process the start layout
processedlayout = []
maxheight = len(layoutlist)-1
columns = len(layoutlist[maxheight-1].split("]"))-1
column = 0 # in the start, changes as I check more columns

for x in range(columns):
    currentcolumn = []
    for y in range(maxheight):
        if layoutlist[y][x*4+1] != " ":
            currentcolumn.append(layoutlist[y][x*4+1])
    currentcolumn.reverse()
    processedlayout.append(currentcolumn)

def displaylayout():
    for i in processedlayout:
        print(i)
displaylayout()

# move boxes
claw = [] # whats gettin moved
for i in moves.split('\n'):
    print (i)
    args = i.split(' ')
    print(args)
    amount = int(args[1])
    fromstack = int(args[3])-1 # -1 to fix starting from 0
    tostack = int(args[5])-1 # same here
    claw = processedlayout[fromstack][-amount:]
    for i in claw:
        processedlayout[fromstack].pop()
    
    # claw.reverse() Only thing I changed for part 2
    processedlayout[tostack].extend(claw)

displaylayout()

input("> ")