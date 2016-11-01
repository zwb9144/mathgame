# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:35:03 2016

@author: 恒安
"""

from Tkinter import *
from operator import add, sub
from random import randint, choice


#------
ops = {'+':add,'-':sub}

#生成题库
pr = ['','','','','','','','','','']
ans = [0,0,0,0,0,0,0,0,0,0]
j=0
while j<10:
    op = choice('+-')
    nums = [randint(10,100) for i in range(2)]
    nums.sort(reverse=True)
    ans[j] = ops[op](*nums)
    pr[j] = '%d %s %d = ' % (nums[0], op, nums[1])
    j+=1

def reset():
    pass
#--------

top = Tk()
top.geometry('600x350')

assign = Button(top, text = '开始做题',command = reset)
assign.pack()

#生成所有组件
exam_1 = Frame(top)
exam_1.pack(fill = X)
prob_1 = Entry(exam_1,width=25)
prob_1.insert(0,pr[0])
prob_1.pack(fill = "y",side = 'left')
equal_1 = Label(exam_1,width=15, text = ' = ')
equal_1.pack(fill = "y",side = 'left')
ans_1 = Entry(exam_1,width=15)
ans_1.pack(fill = "y",side = 'left')
c_ans1 = Label(exam_1,width=15, text = '做对了', fg = 'green')
c_ans1_1 = Label(exam_1,width=15, text = '做错了', fg = 'red')


exam_2 = Frame(top)
prob_2 = Entry(exam_2,width=25)
prob_2.insert(0,pr[1])
prob_2.pack(side = 'left')
equal_2 = Label(exam_2,width=15, text = ' = ')
equal_2.pack(side = 'left')
ans_2 = Entry(exam_2,width=15)
ans_2.pack(side = 'left')
c_ans2 = Label(exam_2,width=15, text = '做对了', fg = 'green')
c_ans2_1 = Label(exam_2,width=15, text = '做错了', fg = 'red')
exam_2.pack(fill = X,expand = 1)


exam_3 = Frame(top)
prob_3 = Entry(exam_3,width=25)
prob_3.insert(0,pr[2])
prob_3.pack(side = 'left')
equal_3 = Label(exam_3,width=15, text = ' = ')
equal_3.pack(side = 'left')
ans_3 = Entry(exam_3,width=15)
ans_3.pack(side = 'left')
c_ans3 = Label(exam_3,width=15, text = '做对了', fg = 'green')
c_ans3_1 = Label(exam_3,width=15, text = '做错了', fg = 'red')
exam_3.pack(fill = X,expand = 1)

exam_4 = Frame(top)
prob_4 = Entry(exam_4,width=25)
prob_4.insert(0,pr[3])
prob_4.pack(side = 'left')
equal_4 = Label(exam_4,width=15, text = ' = ')
equal_4.pack(side = 'left')
ans_4 = Entry(exam_4,width=15)
ans_4.pack(side = 'left')
c_ans4 = Label(exam_4,width=15, text = '做对了', fg = 'green')
c_ans4_1 = Label(exam_4,width=15, text = '做错了', fg = 'red')
exam_4.pack(fill = X,expand = 1)

exam_5 = Frame(top)
prob_5 = Entry(exam_5,width=25)
prob_5.insert(0,pr[4])
prob_5.pack(side = 'left')
equal_5 = Label(exam_5,width=15, text = ' = ')
equal_5.pack(side = 'left')
ans_5 = Entry(exam_5,width=15)
ans_5.pack(side = 'left')
c_ans5 = Label(exam_5,width=15, text = '做对了', fg = 'green')
c_ans5_1 = Label(exam_5,width=15, text = '做错了', fg = 'red')
exam_5.pack(fill = X,expand = 1)

exam_6 = Frame(top)
prob_6 = Entry(exam_6,width=25)
prob_6.insert(0,pr[5])
prob_6.pack(side = 'left')
equal_6 = Label(exam_6,width=15, text = ' = ')
equal_6.pack(side = 'left')
ans_6 = Entry(exam_6,width=15)
ans_6.pack(side = 'left')
c_ans6 = Label(exam_6,width=15, text = '做对了', fg = 'green')
c_ans6_1 = Label(exam_6,width=15, text = '做错了', fg = 'red')
exam_6.pack(fill = X,expand = 1)

exam_7 = Frame(top)
prob_7 = Entry(exam_7,width=25)
prob_7.insert(0,pr[6])
prob_7.pack(side = 'left')
equal_7 = Label(exam_7,width=15, text = ' = ')
equal_7.pack(side = 'left')
ans_7 = Entry(exam_7,width=15)
ans_7.pack(side = 'left')
c_ans7 = Label(exam_7,width=15, text = '做对了', fg = 'green')
c_ans7_1 = Label(exam_7,width=15, text = '做错了', fg = 'red')
exam_7.pack(fill = X,expand = 1)

exam_8 = Frame(top)
prob_8 = Entry(exam_8,width=25)
prob_8.insert(0,pr[7])
prob_8.pack(side = 'left')
equal_8 = Label(exam_8,width=15, text = ' = ')
equal_8.pack(side = 'left')
ans_8 = Entry(exam_8,width=15)
ans_8.pack(side = 'left')
c_ans8 = Label(exam_8,width=15, text = '做对了', fg = 'green')
c_ans8_1 = Label(exam_8,width=15, text = '做错了', fg = 'red')
exam_8.pack(fill = X,expand = 1)

exam_9 = Frame(top)
prob_9 = Entry(exam_9,width=25)
prob_9.insert(0,pr[8])
prob_9.pack(side = 'left')
equal_9 = Label(exam_9,width=15, text = ' = ')
equal_9.pack(side = 'left')
ans_9 = Entry(exam_9,width=15)
ans_9.pack(side = 'left')
c_ans9 = Label(exam_9,width=15, text = '做对了', fg = 'green')
c_ans9_1 = Label(exam_9,width=15, text = '做错了', fg = 'red')
exam_9.pack(fill = X,expand = 1)

exam_10 = Frame(top)
prob_10 = Entry(exam_10,width=25)
prob_10.insert(0,pr[9])
prob_10.pack(side = 'left')
equal_10 = Label(exam_10,width=15, text = ' = ')
equal_10.pack(side = 'left')
ans_10 = Entry(exam_10,width=15)
ans_10.pack(side = 'left')
c_ans10 = Label(exam_10,width=15, text = '做对了', fg = 'green')
c_ans10_1 = Label(exam_10,width=15, text = '做错了', fg = 'red')
exam_10.pack(fill = X,expand = 1)




#批发作业

def TKBD():
    score = 100
    if ans_1.get() == str(ans[0]):
        c_ans1.pack(fill = "y",side = 'left')
    else:
        c_ans1_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_2.get() == str(ans[1]):
        c_ans2.pack(fill = "y",side = 'left')
    else:
        c_ans2_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_3.get() == str(ans[2]):
        c_ans3.pack(fill = "y",side = 'left')
    else:
        c_ans3_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_4.get() == str(ans[3]):
        c_ans4.pack(fill = "y",side = 'left')
    else:
        c_ans4_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_5.get() == str(ans[4]):
        c_ans5.pack(fill = "y",side = 'left')
    else:
        c_ans5_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_6.get() == str(ans[5]):
        c_ans6.pack(fill = "y",side = 'left')
    else:
        c_ans6_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_7.get() == str(ans[6]):
        c_ans7.pack(fill = "y",side = 'left')
    else:
        c_ans7_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_8.get() == str(ans[7]):
        c_ans8.pack(fill = "y",side = 'left')
    else:
        c_ans8_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_9.get() == str(ans[8]):
        c_ans9.pack(fill = "y",side = 'left')
    else:
        c_ans9_1.pack(fill = "y",side = 'left')
        score-=10
    if ans_10.get() == str(ans[9]):
        c_ans10.pack(fill = "y",side = 'left')
    else:
        c_ans10_1.pack(fill = "y",side = 'left')
        score-=10
    st = Label(top,fg = 'red',text = '你的得分是%s' % score )    
    st.pack()
    return score
        
#进行作业的批改
exam_11 = Frame(top)
submit = Button(top, text = '提交作业',command = TKBD)
submit.pack(side = 'bottom')
exam_11.pack(fill = X,expand = 1)


    


mainloop()