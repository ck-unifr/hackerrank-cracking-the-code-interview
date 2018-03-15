# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

def array_left_rotation(a, n, k):
    new_list = a[k:] + a[0:k]
    return new_list


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))

answer = array_left_rotation(a, n, k)

print(*answer, sep=' ')