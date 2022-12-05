def crateValue(cratestr):
    v = ""
    for i in cratestr:
        if i.isalpha():
            v = "".join([v, i])
    return v

def getCrateColumns(crate_lines,crates,crate_size = 3):
    for line in crate_lines:
        crate = ""
        col_number = 1
        for c in line:
            crate+=c
            if len(crate)==crate_size :
                if len(crateValue(crate))==1 : crates[col_number].insert(0,crateValue(crate))
                col_number+=1
            elif len(crate)>crate_size:
                crate=""
    return crates

def cratesPrinter(crates):
    for k in crates:
        print(k,crates[k])
    print("----")


f = open("inputday5.txt","r")
lines = f.read().split("\n")

crates_drawing = []
crates = {}
for l in lines:
    # First condition : we retrieve the drawing of the piled up crates 
    if  "[" in l:
        crates_drawing.append(l)
    # Second condition : we have retrieved all the crates
    # We now recuperate the numbers indicated on the line
    # And we re-constitute the stacks under a well-known format ( a dictionnary)
    elif "move" not in l:
        numbers = ([int(s) for s in l.split() if s.isdigit()])
        for i in numbers:
            crates[i]=[]
        crates = getCrateColumns(crates_drawing,crates)
    # Next part : we can now move the crates according to the instructions 
    else :
        n,source,destination = ([int(s) for s in l.split() if s.isdigit()])
        moving_crates = [] # only for Part 2
        for i in range(n):
            c = crates[source].pop()
            # (Part 1) we move boxes one by one
            # crates[destination].append(c)
            # (Part 2) we move all the involved boxes in one single action
            moving_crates.insert(0,c)
        crates[destination].extend(moving_crates) # only for Part 2

# Display results
cratesPrinter(crates) 
# Getting the top of each stack
top_of_crates = []
for k in crates:
    top_of_crates.append(crates[k].pop())

print("".join(top_of_crates))