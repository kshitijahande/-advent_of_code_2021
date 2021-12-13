from typing import DefaultDict


f= open('./input.txt','r')
lines = f.read().splitlines()

#Part1
a={}

a=DefaultDict(int)
print()
for line in lines:
    code1,code2 = line.split(' | ') 
    code2list=code2.split(' ')
    for i in range (0, len(code2list)):
        if len(code2list[i])==2:
            if (1) in a:
                a[1] +=1
            else:
                a[1]=1      
        elif len(code2list[i])==4:
            if (4) in a:
                a[4] +=1
            else:
                a[4]=1
        elif len(code2list[i])==3:
            if (7) in a:
                a[7] +=1
            else:
                a[7]=1
        elif len(code2list[i])==7:
            if (8) in a:
                a[8] +=1
            else:
                a[8]=1     
                 
print(sum(a.values()))     


