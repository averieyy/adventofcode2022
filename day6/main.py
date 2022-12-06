rawinput = ""
with open('./input.txt', 'r') as f:
    rawinput = f.read()

# rawinput = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

def part1():
    last4 = ['this will be cleared']
    for i in range(3, len(rawinput)):
        while len(last4) != 5:
            last4.append(rawinput[i])
        last4.pop(0)
        print(last4)
        didit = True
        for ii in last4:
            print(last4.count(ii))
            if last4.count(ii) != 1:
                didit = False
                print(didit)
                break
        if didit:
            print (i + 1)
            break

def part2 ():
    last = ['osflas']
    for i in range(3, len(rawinput)):
        while len(last) != 15:
            last.append(rawinput[i])
        last.pop(0)
        print(last)
        didit = True
        for ii in last:
            print(last.count(ii))
            if last.count(ii) != 1:
                didit = False
                print(didit)
                break
        if didit:
            print (i + 1)
            break

part2()
input("> ")