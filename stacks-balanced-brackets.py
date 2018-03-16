# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

# Given n strings of brackets, determine whether each sequence of brackets is balanced.
# If a string is balanced, print YES on a new line; otherwise, print NO on a new line.

# Input Format
# The first line contains a single integer n denoting the number of strings.
# Each line i of the n subsequent lines consists of a single string s denoting a sequence of brackets.

# Output Format
# For each string, print whether or not the string of brackets is balanced on a new line.
# If the brackets are balanced, print YES; otherwise, print NO.


# https://codereview.stackexchange.com/questions/180567/checking-for-balanced-brackets-in-python
def is_matched(expression):
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    queue = []

    for letter in expression:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
