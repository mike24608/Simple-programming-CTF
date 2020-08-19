file = open("C:/Users/mike/AppData/Roaming/Code/User/pythonstuff/Simple Programming CTF/data.dat","r")
newlines = file.readlines()
file.close()

counter = 0

for nlines in newlines:
    if((nlines.count("0"))%3 ==0 or (nlines.count("1"))%2 ==0):
        counter+=1
    else:
        continue

print(counter)

