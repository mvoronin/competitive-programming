#!/bin/python
# -*- coding: utf-8 -*-

import sys
import os

def get_chain_num(ss, w, acc):
    for s in ss[w]:
        return get_chain_num(ss, s, acc=acc+1)
    else:
        return acc

def longest_chain(ws):
    solutions = {}

    for w in ws:
        l = len(w)
        solutions[w] = []
        #print('solutions: {}'.format(solutions))

        for cw in ws:
            if len(cw) >= l:
                continue
            for i in range(l):
                #print('{} == {}'.format(w[:i]+w[i+1:], cw))
                if w[:i]+w[i+1:] == cw:
                    solutions[w] += [cw]
                    break
        #print('solutions: {}'.format(solutions))

    max_acc = 0
    for w in ws:
        if len(w) <= max_acc:
            continue

        acc = 1
        acc = get_chain_num(solutions, w, acc=acc)
        if acc > max_acc:
            max_acc = acc
    return max_acc

print longest_chain(['a', 'b', 'bc', 'bca', 'bda', 'bdca'])  # 4
