f = open('./input.txt','r')
data = f.read().splitlines()

a={}

#Part1 and Part2, For Part1 - Remove the else condition
for coordinate in data:
    j,k= coordinate.split(' -> ')

    x1,y1= j.split(',')
    x1,y1=int(x1),int(y1)

    x2,y2=  k.split(',')
    x2,y2=int(x2),int(y2)

    if x1==x2:
        for i in range(min(y1,y2),max(y1,y2)+1):
            if (x1,i) in a:
                a[x1,i] += 1
            else:
                a[x1,i] =1
    
    elif y1==y2:
        for i in range(min(x1,x2),max(x1,x2)+1):
            if (i,y1) in a:
                a[i,y1] += 1
            else:
                a[i,y1] =1
    
    else:
        x=[]
        y=[]
        if (x1<x2):
            for i in range (x1,x2+1):
                x.append(i)
        else:
            for i in range (x1,x2-1,-1):
                x.append(i)
        if (y1<y2):
            for i in range (y1,y2+1):
                y.append(i)
        else:
            for i in range (y1,y2-1,-1):
                y.append(i)
        for i in range (0,len(x)):
            if (x[i],y[i]) in a:
                 a[x[i],y[i]] += 1
            else:
                a[x[i],y[i]] =1        

count=0
for (i,j) in a:
    if a[i,j] > 1:
        count+=1
print(count)