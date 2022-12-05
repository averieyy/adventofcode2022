elves = []
with open('./input.txt', 'r') as f:
    rawin = f.read()
    elvesitems = rawin.split("\n\n")
    for i in elvesitems:
        elves.append(sum([int(ii) for ii in i.split("\n")]))
elves.sort()
print(elves[-1])

# Part Two
print(elves[-1] + elves[-2] + elves[-3])
input(">") #to stop the program from stopping