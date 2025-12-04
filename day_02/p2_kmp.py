#!/usr/bin/env python3
"""
Day 2 Part 2 (KMP-optimized): Find invalid product IDs (updated rules)

An invalid ID is a number that consists of some sequence of digits
repeated at least twice. Examples:
- 12341234 ("1234" twice)
- 123123123 ("123" three times)
- 1212121212 ("12" five times)

This implementation uses the KMP prefix-function to detect whether a
string is composed of repeats of a smaller substring in O(L) time per ID.
"""


def _prefix_function(s: str) -> list[int]:
    """Compute the prefix-function (pi array) for string s in O(len(s))."""
    n = len(s)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j
    return pi


def is_invalid_id_kmp(num: int) -> bool:
    """Return True if num's decimal representation is a repetition of a substring.

    Uses the KMP prefix-function to detect if the string s of length L
    is equal to some substring of length p repeated L / p times.
    """
    s = str(num)
    L = len(s)
    if L < 2:
        return False

    pi = _prefix_function(s)
    longest_border = pi[-1]
    if longest_border == 0:
        return False

    period = L - longest_border
    if period == L:
        return False

    return L % period == 0


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
            if is_invalid_id_kmp(num):
                invalid_count += 1
                total += num

    print(f"Found {invalid_count} invalid IDs (KMP)")
    print(f"Sum of all invalid IDs (KMP): {total}")

    return total


if __name__ == "__main__":
    result = solve("day_02/0.dat")
    print(f"\nAnswer (KMP): {result}")
