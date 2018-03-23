# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

# Task
# Given an n-element array, A=a_0, a_1, ..., a_n-1 of distinct elements,
# sort array A in ascending order using the Bubble Sort algorithm above.
# Once sorted, print the following three lines:
# 1. Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement, where  is the first element in the sorted array.
# 3. Last Element: lastElement, where lastElement is the last element in the sorted array.
# Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

n_swaps = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            n_swaps += 1


print('Array is sorted in {} swaps.'.format(str(n_swaps)))
print('First Element: {}'.format(str(a[0])))
print('Last Element: {}'.format(str(a[-1])))

