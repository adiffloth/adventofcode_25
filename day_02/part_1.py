id_ranges = open('day_02/0.dat').read().split(',')
total = 0

for id_range in id_ranges:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end+1):
        id_str = str(id)
        if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
            total += id

print(total)
assert total == 28844599675
print('All tests pass.')
