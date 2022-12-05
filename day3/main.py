prioritylist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

rawin = ""
with open("./input.txt", "r") as f:
    rawin = f.read()

# rawin = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

rucksacks = rawin.split("\n")
score = 0

def checkParts (parts):
    global score
    for p1 in parts[0]:
        for p2 in parts[1]:
            for p3 in parts[2]: # forgot to change [1] to [2] causing me to be stuck on part 2 for ages
                if p1 == p2 and p2 == p3:
                    # print(p1, p2, p3) debug code
                    score += int(checkalpha(p1))
                    return 0
            # I used this in part 1
            # if p1 == p2:
            #     score += int(checkalpha(p2))+1
            #     specials.append(p1)
            #     return
    return -1 # will never happen

def checkalpha(letter):
    for i in range(len(prioritylist)):
        if prioritylist[i] == letter:
            return i+1
    return 0

# PART 1
# for i in rucksacks:
#     parts = ['','']
#     parts[0] = i[0: int(len(i)/2)]
#     parts[1] = i[int(len(i)/2):len(i)]

#     checkParts(parts)

for i in range(0, len(rucksacks), 3):
    # print(i) debug code
    parts = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]

    if (checkParts(parts) == -1): print(i)
    

print(score)
input(">")
