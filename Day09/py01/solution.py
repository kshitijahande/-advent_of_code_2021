f= open('./input.txt','r')
lines = f.read().splitlines()

#Part1

a=[[1,0],[-1,0],[0,1],[0,-1]]
sum=0
for i in range (0,len(lines)):
    for j in range (0,len(lines[i])):
        c=[]
        for k in range (0,len(a)):
            if (i+a[k][0]) < len(lines) and (j+a[k][1]) < len(lines[i]):
                if lines[i+a[k][0]][j+a[k][1]] > lines[i][j]:
                    c.append(True)
                else:
                    c.append(False)
        if False in c:
            continue
        else:
            sum += int(lines[i][j])+1
print(sum)