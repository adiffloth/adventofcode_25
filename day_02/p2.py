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

    result = solve("day_02/0.dat")
    print(f"\nAnswer: {result}")
