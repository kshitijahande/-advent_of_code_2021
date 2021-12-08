
f = open('./input.txt','r')
data= [int(x) for x in f.read().split(',')]

'''
#Part1 (This code will not work for part 2 as number of days are quite high)
for i in range (80):
    for i in range (0,len(data)):
        if data[i]==0:
            data [i] = 6
            data.append(8)
        else:
            data[i]=data[i]-1
print(len(data))
'''

#This part of code will work for both part.

d = {i:data.count(i) for i in data}
p=max(8,max(data))

for i in range (0,p+1):
    if i in d:
        continue
    else:
        d[i]=0

for j in range (256):
    ZeroCount=d[0]
    for i in range (1,9):
        d[i-1] = d[i]  
    d[8]=ZeroCount
    d[6]=d[6]+ZeroCount
print(sum(d.values()))