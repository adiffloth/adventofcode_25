#!/usr/bin/env python3
"""
Day 2 Part 2 (regex-based): Find invalid product IDs (updated rules)

An invalid ID is a number that consists of some sequence of digits
repeated at least twice. Examples:
- 12341234 ("1234" twice)
- 123123123 ("123" three times)
- 1212121212 ("12" five times)

This implementation uses a regular expression to detect whether a string
is composed of repeats of a smaller substring.
"""

import re

# (.+) captures a non-empty substring; \1+ requires one or more repeats
_REPEAT_PATTERN = re.compile(r"^(.+)\1+$")


def is_invalid_id_regex(num: int) -> bool:
    """Return True if num's decimal representation is a repetition of a substring."""
    s = str(num)
    # Single-digit numbers cannot be repetitions
    if len(s) < 2:
        return False
    return _REPEAT_PATTERN.match(s) is not None


def solve(input_file: str) -> int:
    with open(input_file, "r") as f:
        data = f.read().strip()

    ranges: list[tuple[int, int]] = []
    for range_str in data.split(","):
        range_str = range_str.strip()
        if range_str:
            start, end = map(int, range_str.split("-"))
            ranges.append((start, end))

    total = 0
    invalid_count = 0

    for start, end in ranges:
        for num in range(start, end + 1):
            if is_invalid_id_regex(num):
                invalid_count += 1
                total += num

    print(f"Found {invalid_count} invalid IDs (regex)")
    print(f"Sum of all invalid IDs (regex): {total}")

    return total


if __name__ == "__main__":
    result = solve("day_02/0.dat")
    print(f"\nAnswer (regex): {result}")
