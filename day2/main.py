orock = "A"
opaper = "B"
osciss = "C"

yrock = "X"
ypaper = "Y"
ysciss = "Z"

#load input
rawout = ""
with open("./input.txt", "r") as f:
    rawout = f.read()

#testing purposes
#rawout = """A Y
#B X
#C Z"""

matches = rawout.split("\n")
score = 0

for i in matches:
    splmatch = i.strip().split(" ")
    opp = splmatch[0]
    you = splmatch[1]
    # Check if you won or drawed
    # This wis part ones logic
    # if (opp == orock and you == ypaper) or (opp == opaper and you == ysciss) or (opp == osciss and you == yrock):
    #     score += 6
    # if (opp == orock and you == yrock) or (opp == opaper and you == ypaper) or (opp == osciss and you == ysciss):
    #     score += 3

    if you == ypaper: # Named them in part 1, and didnt bother changing thema
        score += 3
    if you == ysciss:
        score += 6

    yourpick = ""
    if (opp == orock and you == ypaper) or (opp == opaper and you == yrock) or (opp == osciss and you == ysciss): # Rock check
        yourpick = "A"
    if (opp == orock and you == ysciss) or (opp == opaper and you == ypaper) or (opp == osciss and you == yrock): # Paper check
        yourpick = "B"
    if (opp == orock and you == yrock) or (opp == opaper and you == ysciss) or (opp == osciss and you == ypaper): # Scissors check
        yourpick = "C"
    
    # add points base on your choise
    if yourpick == orock: score += 1
    if yourpick == opaper: score += 2
    if yourpick == osciss: score += 3

print(score)
input(">") #to stop the program from stopping