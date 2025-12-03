<<<<<<< HEAD
#!/usr/bin/env python3
"""
Day 2 Part 1: Find invalid product IDs
An invalid ID is a number that consists of some sequence of digits repeated exactly twice.
Examples: 55 (5 twice), 6464 (64 twice), 123123 (123 twice)
"""

def is_invalid_id(num):
    """Check if a number is invalid (sequence repeated twice)."""
    s = str(num)
    length = len(s)
    
    # Must have even length to be repeated twice
    if length % 2 != 0:
        return False
    
    # Check if first half equals second half
    mid = length // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half


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
    print(f"Invalid IDs: {invalid_ids}")
    print(f"Sum of all invalid IDs: {total}")
    
    return total


if __name__ == "__main__":
    # Test with example
    print("Testing with examples:")
    assert is_invalid_id(11)
    assert is_invalid_id(22)
    assert is_invalid_id(99)
    assert is_invalid_id(1010)
    assert is_invalid_id(1188511885)
    assert is_invalid_id(222222)
    assert is_invalid_id(446446)
    assert is_invalid_id(38593859)
    assert not is_invalid_id(101)
    assert not is_invalid_id(123)
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
        if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
            total += id

print(total)
assert total == 28844599675
print('All tests pass.')
>>>>>>> fa9f3c1329cf8a292c21139ac163ccfa3e85db4f
