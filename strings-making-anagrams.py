# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

# Alice is taking a cryptography class and finding anagrams to be very useful.
# We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form
# the second string.
# In other words, both strings must contain the same exact letters in the same exact frequency.
# For example, 'bacdc' and 'dcbac' are anagrams, but 'bacdc' and 'dcbad' are not.

# Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

# Given two strings a and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make a and b anagrams.
# Any characters can be deleted from either of the strings.


# Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.



def number_needed(a, b):
    cnt = [0] * 26

    for a_i in a:
        cnt[ord(a_i)-ord('a')] += 1

    for b_i in b:
        cnt[ord(b_i)-ord('a')] -= 1

    n_needed = 0
    for value in cnt:
        n_needed += abs(value)

    return n_needed


a = input().strip()
b = input().strip()

print(number_needed(a, b))