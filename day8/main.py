rawinput = ""
with open("./input.txt", "r") as f:
    rawinput = f.read()

# rawinput = """30373
# 25512
# 65332
# 33549
# 35390"""

matrix = []

rows = rawinput.split("\n")

def getTreeScore (x,y): # Used to be called "isTreeVisible for the old one"
    # edgesHidden = 0
    viewscore = 1
    treesviewed = 0
    # check -x direc
    for i in range(x-1, -1, -1):
        treesviewed += 1
        if rows[y][i] >= rows[y][x]:
            break
    viewscore = viewscore * treesviewed
    treesviewed = 0
        
    # check -y direc
    for i in range(y-1, -1, -1):
        treesviewed += 1
        if rows[i][x] >= rows[y][x]:
            break
    viewscore = viewscore * treesviewed
    treesviewed = 0
    # check +x direc
    for i in range(x+1, len(rows[1])):
        treesviewed += 1
        if rows[y][i] >= rows[y][x]:
            break
    viewscore = viewscore * treesviewed
    treesviewed = 0
    # check +y direc
    # old one preserved for "history"
    # for i in range(y+1, len(rows)):
    #     if rows[i][x] >= rows[y][x]:
    #         edgesHidden += 1
    #         break
    for i in range(y+1, len(rows)):
        treesviewed += 1
        if rows[i][x] >= rows[y][x]:
            break
    viewscore = viewscore * treesviewed
    treesviewed = 0

    print (x,y, viewscore)
    
    return viewscore

g = 0

for y in range(1, len(rows)-1):
    for x in range(1, len(rows[y])-1):
        gt = getTreeScore(x,y)
        if g < gt: 
            g = gt

# print(len(rows[y])*len(rows)-g)
print (g)