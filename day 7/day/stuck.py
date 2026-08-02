from collections import Counter

def first_non_repeating_char(s):
    # Count the frequency of each character
    freq = Counter(s)

    # Find the first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    return None  # No non-repeating character found


# Example usage
s = "swiss"
result = first_non_repeating_char(s)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")