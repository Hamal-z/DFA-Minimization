# -*- coding: UTF-8 -*-
from minDFA import minDFA

dfa = minDFA()
judgeDic, endState = dfa.show()
print('judgeDic', judgeDic)
print('endState', endState)


def getFormatData():
    Data = open("data.dat", 'r')
    strlist = []
    for line in Data:
        strlist += [line]
    formatData = [i for i in strlist[-1]]
    formatData.pop()
    return formatData


strlist = getFormatData()
print(strlist)
nextNum = 1
flag = 1
for i in strlist:
    nextNum = judgeDic[nextNum].get(i, None)
    if nextNum == -1 or nextNum is None:
        flag = 0
        break
    if i == strlist[-1] and nextNum not in endState:
        flag = 0

if flag == 0:
    print('no')
else:
    print('yes')
