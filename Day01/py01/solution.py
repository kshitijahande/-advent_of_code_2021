
f = open ("./input.txt","r")
lines = list(map(int,f.read().splitlines()))

#part1

count = 0
for i in range (0,len(lines)-1):

    if lines[i] > lines[i-1]:
        #print(data[i+1],data[i])
        count += 1
print(count)

#part 2

slidingCount=0
for i in range (1,len(lines)-2):
    current = lines[i]+lines[i+1]+lines[i+2]
    previous = lines[i]+lines[i-1]+lines[i+1]

    if current > previous:
        slidingCount += 1

print(slidingCount)