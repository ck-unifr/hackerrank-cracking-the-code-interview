# https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem

# Given an input stream of n integers, you must perform the following task for each ith integer:
#
# 1. Add the ith integer to a running list of integers.
# Find the median of the updated list (i.e., for the first element through the ith element).
# Print the list's updated median on a new line.
# The printed value must be a double-precision number scaled to decimal place (i.e., 12.3 format).

# Input Format
# The first line contains a single integer, n, denoting the number of integers in the data stream.
# Each line i of the n subsequent lines contains an integer, a_i, to be added to your list.


# Output Format
# After each new integer is added to the list,
# print the list's updated median on a new line as a single double-precision number scaled to 1 decimal place
# (i.e.,  12.3 format).

# Fork from https://github.com/egalli64/pythonesque/blob/master/hr/ctci/find_the_running_median.py

#!/bin/python3

import sys

from heapq import heappop, heappush


class MedianHeap:
    def __init__(self):
        self.left = []   # max heap
        self.right = []  # min heap

    def push(self, value):
        if not self.left or value < -self.left[0]:
            heappush(self.left, -value)
        else:
            heappush(self.right, value)

        # balance the heaps
        bigger = self.left if len(self.left) > len(self.right) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right
        if len(bigger) - len(smaller) > 1:
            moved = -1 * heappop(bigger)
            heappush(smaller, moved)

    def median(self):
        bigger = self.left if len(self.left) > len(self.right) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right

        if bigger is smaller:
            return (self.right[0] - self.left[0]) / 2
        else:
            maxi = -1.0 if bigger is self.left else 1.0
            return maxi * bigger[0]


def solution(values):
    heap = MedianHeap()

    result = []
    for value in values:
        heap.push(value)
        result.append(str(heap.median()))

    return '\n'.join(result)


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))

    print(solution(data))


