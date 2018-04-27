# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

#!/bin/python3

import sys


def solve(arr, money):
    costs = dict()

    for i in range(len(arr)):
        costs[arr[i]] = i

    max_i = 0
    max_j = 0
    max_dist = 0
    for i, arr_i in enumerate(arr):
        if (money - arr_i) in costs:
            j = costs[(money - arr_i)]
            if i != j:
                dist = abs(i - j)
                if dist > max_dist:
                    max_dist = dist
                    max_i = i + 1
                    max_j = j + 1
    print('{} {}'.format(min(max_i, max_j), max(max_i, max_j)))



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)