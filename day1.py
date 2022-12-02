f = open("inputday1.txt", "r")

r = 0
elves = []
for x in f:
    if x!='\n':
        r+=int(x)
    else :
        elves.append(r)
        r = 0

ms = []
for i in range(0,3):
    m = max(elves)
    ms.append(m)
    elves.remove(m)

print(sum(ms))

    
