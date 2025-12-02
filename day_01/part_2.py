lines = open('day_01/0.dat').read().splitlines()

pos = 50
combo = 0

for line in lines:
    dir = 1 - 2 * (line[0] == 'L')
    amt = int(line[1:])
    
    if dir==1:
        combo += (pos + amt)//100
    else:
        combo += ((100-pos)%100 + amt)//100
    
    pos = (pos + amt*dir) % 100

print(combo)
