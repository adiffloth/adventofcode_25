lines = open('day_01/0.dat').read().splitlines()

pos = 50
combo = 0

for line in lines:
    dir = 1 - 2 * (line[0] == 'L')
    amt = int(line[1:])
    pos = (pos + amt*dir) % 100
    if pos == 0:
        combo += 1

print(combo)
