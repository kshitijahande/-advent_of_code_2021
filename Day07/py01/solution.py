import statistics

f = open ('./input.txt','r')
numbers = [int(x) for x in f.read().split(',')]

#Part1
med = statistics.median(numbers)
distance =0
for i in range (0,len(numbers)):
    if numbers[i] < med:
        distance = distance + med-numbers[i]
    elif numbers [i] > med:
        distance = distance+ numbers [i] -med
print (distance)

#Part2
distance=0
mean=int(statistics.mean(numbers))
print(mean)

for i in range (0,len(numbers)):
    if numbers[i] < mean:
        d1=mean-numbers[i]
    elif numbers [i] > mean:
        d1=numbers [i] -mean
    for i in range (1,d1+1):
        distance=distance+i

print (distance)
