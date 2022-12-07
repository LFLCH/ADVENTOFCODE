# Defining File and Folders for our File System
# the toString redefinition is just for pretty printing
class File:
    def __init__(self, name : str, size : list):
        self.name = name
        self.size =size

    def __str__(self):
        return self.name +" (file, size="+str(self.size)+")"

class Folder:
    def __init__(self, name: str,parent,files : list, folders : list):
        self.name = name
        self.files = files
        self.folders = folders
        self.parent = parent
    
    def getSize(self):
        size = 0
        for f in self.files:
            size+=f.size

        for f in self.folders:
            size += f.getSize()
        return size

    def __str__(self):
        s= self.name+" ("+str(self.getSize())+')'
        for file in self.files:
            s+=" "+str(file)
        return s

# Just to check if the file tree is the right one
def tree(fold : Folder,depth=0):
    print(" "*depth," - ",fold)
    depth+=1
    for fo in fold.folders:
        tree(fo,depth)

def lightChildDirectoriesSizes(fold : Folder,max_size=100000):
    light = []
    if fold.getSize()<=max_size:
        light=[fold.getSize()]
    for child in fold.folders :
        light = light + lightChildDirectoriesSizes(child,max_size)
    return light

# (Part 2)
def findDirectoryWithClosestSize(fold : Folder,size):
    min_directory = fold
    for child in fold.folders:
        closest = findDirectoryWithClosestSize(child,size)
        closest_size = closest.getSize()
        if closest_size< min_directory.getSize() and closest_size>=size:
            min_directory = closest
    return min_directory

        
f = open("inputday7.txt","r")
lines = f.read().split("\n")

fs = Folder("/",None,[],[]) # File system : a Folder with the name "/". No Parent directory of course
cd = fs # cd is the current directory (where the user is placed)


for l in lines:
    if l.startswith("$ "):
        l = l[2:]
        command = l[:2]
        dest = l[3:]
        if command == "cd":
            if dest == "..":
                cd = cd.parent
            elif dest == "/":
                cd = fs
            else :
                for fold in  cd.folders:
                    if fold.name==dest:
                        cd = fold
                        break
    elif l.startswith("dir"):
        dirname = l[4:]
        d = Folder(dirname,cd,[],[])
        cd.folders.append(d)

    elif l[0].isnumeric():
        size = [int(s) for s in l.split() if s.isdigit()][0]
        filename = l[len(str(size))+1:]
        fi = File(filename,size)
        cd.files.append(fi)

# (Part 1)
#print(sum(lightChildDirectoriesSizes(fs))) 

# (Part 2)
unused_space = 70000000 - fs.getSize()
space_to_free = 30000000 - unused_space
# From now on we suppose space_to_free is > 0 (otherwise the exercise wouldn't make sense)
closest = findDirectoryWithClosestSize(fs,space_to_free)
print(closest.getSize())