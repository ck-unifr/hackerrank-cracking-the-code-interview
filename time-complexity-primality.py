# https://www.hackerrank.com/challenges/ctci-big-o/problem

# For each integer, print whether n is Prime or Not prime on a new line.

def is_prime(n):
    if n == 1:
        return False
    divisor = 2
    while divisor**2 <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if is_prime(n):
        print('Prime')
    else:
        print('Not prime')