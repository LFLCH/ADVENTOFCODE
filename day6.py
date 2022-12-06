def caractersAreUnique(s):
    return len(set(s)) == len(s)

f = open("inputday6.txt","r")
line = f.readline()
buffer_size = 14 # (Part 1) : 4


for i in range(0,len(line)-buffer_size):
    buffer = line[i:i+buffer_size]
    if caractersAreUnique(buffer): 
        print(i+buffer_size)
        break
    elif i>buffer_size:
        buffer = buffer[1:]

    