#!/bin/python
import sys
import os

def maxThreats(a):
    n = len(a)
    c = [0] * n
    y = 1
    for x in a:
        c[y-1] = 0

        for xi, yi in zip(xrange(x-1,0,-1), xrange(y-1,0,-1)):  # X <, Y <
            if a[yi-1] == xi:
                c[y-1] += 1
                break

        for xi, yi in zip(xrange(x+1,n+1), xrange(y-1,0,-1)):  # X >, Y <
            if a[yi-1] == xi:
                c[y-1] += 1
                break

        for xi, yi in zip(xrange(x-1,0,-1), xrange(y+1,n+1)):  # X <, Y >
            if a[yi-1] == xi:
                c[y-1] += 1
                break

        for xi, yi in zip(xrange(x+1,n+1), xrange(y+1,n+1)):  # X >, Y >
            if a[yi-1] == xi:
                c[y-1] += 1
                break

        y += 1

    return max(c)

#f = open(os.environ['OUTPUT_PATH'], 'w')


#_a_cnt = int(raw_input())
#_a_i=0
#_a = []
#while _a_i < _a_cnt:
#    _a_item = int(raw_input())
#    _a.append(_a_item)
#    _a_i+=1


# res = maxThreats(_a)
res = maxThreats([3,1,4,2])
#f.write(str(res) + "\n")
#f.close()
print res
