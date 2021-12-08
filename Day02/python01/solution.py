# Part 1
moves = [move.split() for move in open('../input.txt').read().splitlines()]
moves = [[move[0], int(move[1])] for move in moves]

x = y = 0
for move in moves:
    if move[0] == 'forward': x += move[1]
    if move[0] == 'down': y += move[1]
    if move[0] == 'up': y -= move[1]

print(f"horizontal: {x}\n"
      f"depth: {y}\n"
      f"product: {x*y}")


# Part 2 
moves = [move.split() for move in open('../input.txt').read().splitlines()]
moves = [[move[0], int(move[1])] for move in moves]


x = y = aim = 0
for move in moves:
    if move[0] == 'forward':
        x += move[1]
        y += aim * move[1]
    if move[0] == 'down':
        aim += move[1]
    if move[0] == 'up':
        aim -= move[1]

# What do you get if you multiply your final horizontal position by your final depth?
print(f"horizontal: {x}\n"
      f"depth: {y}\n"
      f"product: {x*y}")