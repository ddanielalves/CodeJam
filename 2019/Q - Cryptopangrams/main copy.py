input_file = open('test.txt')
input = lambda : input_file.readline().strip('\n')


import numpy as np
import sys
import math
getint = lambda: int(input())
getints = lambda: [int(a) for a in input().split()]
getints2 = lambda: [int(a)-1 for a in input().split()]
getm = lambda L: [[int(a) for a in input().split()] for l in range(L)]
outp = lambda i,r: print('Case #{}: {}'.format(i, r))

def solve():
    def testf(val, i):
        cy = [val]
        while i < L-1:
            i+=1
            if M[i] % val==0:
                val = M[i] // val
                cy.append(val)  
            else:
                return False
        
        return cy
    
    def testb(val, i):
        cy = []
        while i > 0:
            i-=1
            if M[i] % val==0:
                val = M[i] // val
                cy.append(val)  
            else:
                return False
        return cy[::-1]

    N,L = getints()
    M = getints()
    
    i = 0
    while M[i] == M[i+1]:
        i+=1

    j = np.gcd(M[i], M[i+1])
    
    c = testb(j, i) + [M[i]//j] + testf(j, i)

    ans = [None] * (L+1)
    c2 = np.argsort(c) 
    prevv = c[c2[0]]
    prevl = 65
    for i in c2:
        if c[i] != prevv:
            prevl+=1
            prevv = c[i]
        ans[i] = chr(prevl)
    return "".join(ans)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(1, t+1):
        r = solve()
        aux = outp(i,r)
        