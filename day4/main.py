with open("./input.txt", "r") as f:
    rawinput = f.read()

# rawinput = """1-93,2-11
# 26-94,26-94
# 72-92,48-88
# 36-37,37-52
# 2-98,1-98
# 1-83,1-84
# 74-79,76-76
# 66-85,66-86"""

pairs = rawinput.split("\n")

overlappers = 0

for i in pairs:
    p = i.split(",")
    fns = int(p[0].split("-")[0])
    sns = int(p[1].split("-")[0])
    fne = int(p[0].split("-")[1])
    sne = int(p[1].split("-")[1])
    # first part
#     if fns <= sns:
#         if fne >= sne:
#             overlappers += 1
#             print(fns, fne, sns, sne, "first")
#             continue
#     if sns <= fns:
#         if sne >= fne:
#             overlappers += 1
#             print(fns, fne, sns, sne, "second")
#   second
    if sns >= fns and sns <= fne:
        overlappers += 1
    elif fns >= sns and fns <= sne:
        overlappers += 1
    elif sne <= fne and sne >= fns:
        overlappers += 1
    elif fne <= sne and fne >= sns:
        overlappers += 1

print(overlappers)
input(">")