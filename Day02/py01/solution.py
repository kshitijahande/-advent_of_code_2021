
f = open ("./input.txt","r")
lines = f.read().splitlines()

#Part1
forwardDistance = 0
depthDistance = 0

for line in lines:
    command,distance = line.split()
    distance = int(distance)

    if command == 'forward':
        forwardDistance = forwardDistance + distance

    elif command == 'up':
        depthDistance = depthDistance - distance

    elif command == 'down':
        depthDistance = depthDistance + distance

print (forwardDistance*depthDistance)


#Part 2
forwardDistance = 0
depthDistance = 0
aim =0 

for line in lines:
    command,distance = line.split()
    distance = int(distance)

    if command == 'forward':
        forwardDistance = forwardDistance + distance
        aim = aim +(depthDistance * distance)

    elif command == 'up':
        depthDistance = depthDistance - distance

    elif command == 'down':
        depthDistance = depthDistance + distance

print (forwardDistance*aim)