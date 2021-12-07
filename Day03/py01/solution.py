
f = open ("./input.txt","r")
lines = f.read().splitlines()


#Part1
gamma=''
epsilon=''
 
for i in range (0 , len(lines[0])):
    ZeroCount=0
    OneCount=0
    for j in range (0,len(lines)):
        if lines[j][i]=='0':
            ZeroCount +=1
        else:
            OneCount+=1
    if ZeroCount > OneCount:
        gamma +='0'
        epsilon +='1'
    else:
        gamma +='1'
        epsilon +='0'

#print(int(gamma,2),int(epsilon,2))       
print(int(gamma,2)*int(epsilon,2))

#Part2


newlines=lines
PositionCount = 0
while len(newlines) > 1:
    zerolines=[]
    onelines=[]
    ZeroCount=0
    OneCount=0       
    for j in range (0,len(newlines)):
        if newlines[j][PositionCount] == '0':
            ZeroCount +=1
            zerolines.append(newlines[j])
        else:
            OneCount +=1
            onelines.append(newlines[j])
    if ZeroCount > OneCount:
        newlines=zerolines
    else:
        newlines=onelines
    PositionCount +=1
O2Rating= newlines[0]
print(O2Rating)

newlines=lines
PositionCount=0
while len(newlines) > 1:
    zerolines=[]
    onelines=[]
    ZeroCount=0
    OneCount=0
    for j in range (0,len(newlines)):
        if newlines[j][PositionCount]=='0':
            ZeroCount +=1
            zerolines.append(newlines[j])
        else:
            OneCount +=1
            onelines.append(newlines[j])
    if ZeroCount > OneCount:
        newlines=onelines
    else :
        newlines=zerolines
    PositionCount+=1
CO2Rating= newlines[0]
print(CO2Rating)

#print(int(CO2Rating,2),int(O2Rating,2))       
print(int(O2Rating,2)*int(CO2Rating,2))


























