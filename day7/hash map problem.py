"""
hash_map_problems.py

Problems included:
1. Two Sum
2. Is Anagram
3. First Unique Character
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True

def first_unique_character(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    for i, char in enumerate(s):
        if frequency[char] == 1:
            return i

    return -1


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(is_anagram("listen", "silent"))
    print(first_unique_character("leetcode"))