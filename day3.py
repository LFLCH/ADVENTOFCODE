import math

def charValue(c):
    if c.isupper():
        return ord(c) - ord('A') + 27
    else : return  ord(c) - ord('a') + 1

def commonChar(ls):
    # comparaison of  s_ref to all the rest of the list
    s_ref = ls[0]
    del ls[0] 
    # iteration over all the caracters of the string of reference 
    # in order to find a common caracter between all the strings
    for c in s_ref:
        common = True
        for s in ls:
            if c not in s :
                common = False
                break
        if common :
            return c

f = open("inputday3.txt", "r")
lines = f.read().split() # recuperation of the file under the format of a list of strings
total = 0

# (Part 1) 
# addition of the value of the common char between two substring to the total
# for s in lines:
#     n = len(s)
#     mid = math.floor(n/2)
#     s1 = s[slice(mid)]
#     s2 = s[slice(mid,n)]
#     c = commonChar([s1,s2])
#     total += charValue(c)

# (Part 2)  
# gathering  the lines according to the rest of the division of their index per 3 
l1 = lines[0::3] 
l2 = lines[1::3]
l3 = lines[2::3]
# addition of the value of the common char between all the groups of three consecutive strings 
for i in range(0,len(l1)):
    c = commonChar([l1[i],l2[i],l3[i]])
    total += charValue(c)

print(total)
