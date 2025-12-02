id_ranges = open('day_02/0.dat').read().split(',')
total = 0

for id_range in id_ranges:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end+1):
        id_str = str(id)
        for x in range(1, len(id_str)//2 + 1):
            if id_str == (id_str[:x] * (len(id_str)//x)):
                total += id
                break

print(total)
assert total == 48778605167
print('All tests pass.')
