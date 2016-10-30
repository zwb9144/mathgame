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

def doprob(scores):
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
                scores -= 10
                print '唉，要扣分了。正确答案是：\n%s%d'.decode('utf-8').encode('cp936') % (pr, ans)
                print scores
            else:
                print '不对，再想想'.decode('utf-8').encode('cp936')
                
            oops += 1
        except(KeyboardInterrupt, EOFError, ValueError):
            print '不对，再想想吧'.decode('utf-8').encode('cp936')
    return scores

def main():
    times = 0
    scores = 100
    while times<10:
        scores = doprob(scores)
        times+=1
        print '恭喜你，做对了%d道题'.decode('utf-8').encode('cp936') % times
        try:
            if times == 10:
                print '恭喜你，你的得分是%d'.decode('utf-8').encode('cp936') % scores
            opt = raw_input('按任意键继续做题，按N退出:[n]'.decode('utf-8').encode('cp936')).lower()
			
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break	
if __name__ == '__main__':
    main()