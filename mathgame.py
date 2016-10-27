# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""
Created on Wed Oct 26 00:44:40 2016

@author: 恒安
"""

from operator import add, sub
from random import randint, choice

ops = {'+':add,'-':sub}
MAXTRIES = 2

def doprob():
    op = choice('+-')
    nums = [randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    ans = ops[op](*nums)
    pr = '%d %s %d = ' %(nums[0], op, nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:              
                break
            if oops == MAXTRIES:
                print '正确答案是：\n%s%d' % (pr, ans)
            else:
                print '不对，再想想'
                
            oops += 1
        except(KeyboardInterrupt, EOFError, ValueError):
            print '不对，再想想'

def main():
    times = 0
    while times<20:
        doprob()
        times+=1
        print '恭喜你，做对了%d道题' % times
        try:
            opt = raw_input('按任意键继续做题，按N退出:[n]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()