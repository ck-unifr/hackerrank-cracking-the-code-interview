# https://www.hackerrank.com/challenges/ctci-merge-sort/problem

# Fork from https://gist.github.com/vumaasha/1999075

#!/bin/python3

import sys

def mergeSort(A):
    if len(A)>1:
        [x1,x2]=divide(A)
        #print x1,x2
        x1, leftInv=mergeSort(x1)
        x2, rightInv=mergeSort(x2)
        #print leftInv,rightInv
        merged, splitInv=merge(x1,x2)
        #print splitInv
        return merged, (leftInv+rightInv+splitInv)
    else:
        return A, 0


def divide(A):
    size=len(A)
    halfSize=int(size/2)
    x1=[]
    x2=[]
    for index in range(0, halfSize):
        x1.append(A[index])
    for index in range(halfSize, size):
        x2.append(A[index])
    return [x1,x2]


def merge(x1,x2):
    x=[]
    x1Index=0
    x2Index=0
    invCount=0
    size1=len(x1)
    size2=len(x2)
    while (x1Index < size1 and x2Index < size2):
        if x1[x1Index]<=x2[x2Index]:
            x.append(x1[x1Index])
            x1Index=x1Index+1
        else:
            x.append(x2[x2Index])
            x2Index=x2Index+1
            invCount += (size1-x1Index)

    for i in range(x1Index,size1):
         x.append(x1[i])

    for i in range(x2Index,size2):
         x.append(x2[i])

    return x, invCount

def countInversions(arr):
    neArr, nbInv = mergeSort(arr)
    return nbInv

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = countInversions(arr)
        print(result)
