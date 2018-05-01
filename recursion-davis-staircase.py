# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem

# Input Format
# The first line contains a single integer s denoting the number of staircases in his house.
# Each line i of the s subsequent lines contains a single integer n denoting the height of staircase i.

# Output Format
# For each staircase, print the number of ways Davis can climb it in a new line.


dict = {0:0, 1:1, 2:2, 3:4}

def steps(n):
    if n in dict.keys():
        return dict.get(n)
    result = steps(n-3) + steps(n-2) + steps(n-1)
    dict.update({n: result})
    return dict.get(n)


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    nb_ways = steps(n)
    print(nb_ways)

