input_file = open('test.txt')
input = lambda : input_file.readline().strip('\n')



import numpy as np
import sys
getint = lambda: int(input())
getints = lambda: [int(a) for a in input().split()]
getm = lambda L: [[int(a) for a in input().split()] for l in range(L)]
outp = lambda i,r: print('Case #{}: {}'.format(i, r))

def isr(n):
    n = str(n)
    prev_i = int(n[0])
    r = False
    for size in [2**i for i in range(len(n)) if 2**i <= len(n)]:
        for i in [n[i:i+size] for i in range(0, len(n), size)]:
            i = int(i)
            if not prev_i + 1 == i:
                r = False
                break
            prev_i=i
            r = True
    return r



def solve():
    N = input()
    res = []

    if len(N) == 1:
        return "12"
    N = int(N)

    while not isr(N):
        N+=1

    return N

    
if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        r = solve()
        outp(i,r)
        