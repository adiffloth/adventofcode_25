id_ranges = open('day_02/0.dat').read().split(',')
total = 0

for id_range in id_ranges:
    start, end = map(int, id_range.split('-'))
    for id in range(start, end+1):
        id_str = str(id)
        len_id_str = len(id_str)
        for x in range(1, len_id_str//2 + 1):
            if len_id_str % x != 0:
                continue
            if id_str == (id_str[:x] * (len_id_str//x)):
                total += id
                break

print(total)
assert total == 48778605167
print('All tests pass.')
