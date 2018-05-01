# https://www.hackerrank.com/challenges/ctci-lonely-integer/problem

# !/bin/python3

# Input format
# The first line contains a single integer n, denoting the number of integers in the array.
# The second line contains n space-separated integers describing the respective values in A.

# Output format
# Print the unique number that occurs only once in A on a new line.


import sys


def lonely_integer(a):
    dict_a = dict()
    str_output = ''
    for val in a:
        if val not in dict_a:
            dict_a[val] = 1
        else:
            dict_a[val] += 1
    for key, val in dict_a.items():
        if val == 1:
            str_output += str(key) + ' '
    return str_output


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

