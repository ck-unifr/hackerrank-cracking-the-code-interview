#https://www.hackerrank.com/challenges/ctci-ransom-note/problem

# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
# exactly using whole words from the magazine; otherwise, print No.

# Input Format

# The first line contains two space-separated integers describing the respective values of
# m (the number of words in the magazine) and n (the number of words in the ransom note).
#
# The second line contains m space-separated strings denoting the words present in the magazine.
#
# The third line contains n space-separated strings denoting the words present in the ransom note.
#

from collections import defaultdict

def ransom_note(magazine, ransom):
    dict_word = defaultdict(int)

    for word in magazine:
        if word in magazine:
            dict_word[word] += 1

    for word in ransom:
        if dict_word[word] == 0:
            return False
        dict_word[word] -= 1

    return True


# magazine = ('two times three is not four').strip().split(' ')
# ransom = ('two times two is four').strip().split(' ')
# print(ransom_note(magazine, ransom))


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")