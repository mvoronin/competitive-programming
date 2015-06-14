#!/bin/python
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/candies

def solution(n, rs, cs):
    for i in xrange(1, n):
        if rs[i-1] > rs[i]:  # предыдущий элемент больше чем текущий
            if cs[i-1] <= cs[i]:  # у предыдущего конфет меньше или равно, чем у текущего
                cs[i-1] = cs[i] + 1

                j = i-1
                while j > 0 and rs[j-1] > rs[j] and cs[j-1] <= cs[j]:
                    cs[j-1] = cs[j] + 1
                    j -= 1

        elif rs[i-1] < rs[i]:  # предыдущий элемент меньше чем текущий
            cs[i] = cs[i-1] + 1

        i += 1


# n = int(raw_input())
# rs = []
# cs = n*[1]
# for i in xrange(n):
#     rs.append(int(raw_input()))
# solution(n, rs, cs)
# sum(cs)

n = 10
rs = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
cs = n*[1]
solution(n, rs, cs)
assert sum(cs) == 19

n = 3
rs = [1, 2, 2]
cs = n*[1]
solution(n, rs, cs)
assert sum(cs) == 4
