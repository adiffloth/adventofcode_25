<<<<<<< HEAD
#!/usr/bin/env python3
"""
Day 2 Part 2: Find invalid product IDs (updated rules)
An invalid ID is a number that consists of some sequence of digits repeated at least twice.
Examples: 12341234 (1234 twice), 123123123 (123 three times), 1212121212 (12 five times)
"""

def is_invalid_id(num):
    """Check if a number is invalid (sequence repeated at least twice)."""
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    # Pattern must repeat at least twice, so max pattern length is length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the string can be formed by repeating a pattern of this length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repeats = length // pattern_len
            
            # Check if repeating the pattern gives us the original string
            if pattern * repeats == s:
                return True
    
    return False


def solve(input_file):
    """Solve the puzzle."""
    with open(input_file, 'r') as f:
        data = f.read().strip()
    
    # Parse ranges (they're comma-separated)
    ranges = []
    for range_str in data.split(','):
        range_str = range_str.strip()
        if range_str:
            start, end = map(int, range_str.split('-'))
            ranges.append((start, end))
    
    # Find all invalid IDs
    total = 0
    invalid_ids = []
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id(num):
                invalid_ids.append(num)
                total += num
    
    print(f"Found {len(invalid_ids)} invalid IDs")
    print(f"Sum of all invalid IDs: {total}")
    
    return total


if __name__ == "__main__":
    # Test with examples
    print("Testing with examples:")
    assert is_invalid_id(11)  # 1 repeated twice
    assert is_invalid_id(22)  # 2 repeated twice
    assert is_invalid_id(99)  # 9 repeated twice
    assert is_invalid_id(111)  # 1 repeated three times
    assert is_invalid_id(999)  # 9 repeated three times
    assert is_invalid_id(1010)  # 10 repeated twice
    assert is_invalid_id(1188511885)  # 11885 repeated twice
    assert is_invalid_id(222222)  # 222 repeated twice or 22 repeated three times
    assert is_invalid_id(446446)  # 446 repeated twice
    assert is_invalid_id(38593859)  # 3859 repeated twice
    assert is_invalid_id(565656)  # 56 repeated three times
    assert is_invalid_id(824824824)  # 824 repeated three times
    assert is_invalid_id(2121212121)  # 21 repeated five times
    assert is_invalid_id(12341234)  # 1234 repeated twice
    assert is_invalid_id(123123123)  # 123 repeated three times
    assert is_invalid_id(1212121212)  # 12 repeated five times
    assert is_invalid_id(1111111)  # 1 repeated seven times
    assert not is_invalid_id(101)  # Not a repeating pattern
    assert not is_invalid_id(123)  # Not a repeating pattern
    print("All tests passed!")
    
    print("\nSolving puzzle:")
    result = solve("0.dat")
    print(f"\nAnswer: {result}")
=======
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
>>>>>>> fa9f3c1329cf8a292c21139ac163ccfa3e85db4f
