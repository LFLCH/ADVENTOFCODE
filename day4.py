f = open("inputday4.txt", "r")
lines = f.read().split()

#full_containements = 0 # (Part 1)
overlaps = 0 # (Part 2)

for l in lines:
    elf1, elf2 = l.split(',')
    elf1 = [int(s) for s in elf1.split('-') if s.isdigit()]
    elf2 = [int(s) for s in elf2.split('-') if s.isdigit()]
    # Using python sets for their usefull properties
    set_elf1 = set(range(elf1[0],elf1[1]+1))
    set_elf2 = set(range(elf2[0],elf2[1]+1))
    # (Part 1)
    # if set_elf2.issubset(set_elf1) or set_elf1.issubset(set_elf2):
    #     full_containements +=1
    # (Part 2)
    if set_elf1.intersection(set_elf2):
        overlaps+=1


#print(full_containements) # (Part 1)
print(overlaps) # (Part 2)

