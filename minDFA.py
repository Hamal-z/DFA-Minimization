# -*- coding: UTF-8 -*-
from toDFA import ToDFA

DFA = ToDFA()
global stateTable, endState, matrix, newMatrix

stateTable = DFA.showDFA()
stateTable, endState, matrix = DFA.newTable(stateTable)
newMatrix = matrix[1:]


class minDFA(object):

    def __init__(self):
        super(minDFA, self).__init__()
        self.itemSet = set(matrix[0][1:])
        self.newNum = 1
        self.resList = {0: set(endState)}
        self.toList = {'.': -1}
        for item in stateTable['I']:
            if item in endState:
                self.toList[item] = 0
            else:
                self.toList[item] = -2
        I1 = list(set(stateTable['I']) - set(endState))
        self.divide(I1)
        I2 = endState
        for item in I2:
            self.toList[item] = -1
        del self.resList[0]
        self.divide(I2)

    def divide(self, I):
        for line1 in I:
            flag = 0
            for key, value in self.resList.items():
                if line1 in value:
                    # toList[line1] = key
                    flag = 1
                    break
            if flag == 0:
                self.resList[self.newNum] = set([line1])
                # resList[newNum] = [line1]
                self.toList[line1] = self.newNum
                self.newNum += 1
            else:
                continue

            for line2 in I:
                if line1 == line2 or line2 in self.resList[self.toList[line1]]:
                    continue
                flag = 1
                for i in range(len(self.itemSet)):
                    if self.toList[newMatrix[line1][i + 1]] != self.toList[newMatrix[line2][i + 1]]:
                        flag = 0
                        break
                if flag == 1:
                    # resList[toList[line1]].add(line2)
                    if self.toList[line2] != -1:
                        aa = line1
                        bb = line2
                        del self.resList[aa]
                    else:
                        aa = line2
                        bb = line1
                    # resList[toList[line1]].append(line2)
                    self.resList[self.toList[bb]].add(aa)
                    self.toList[aa] = self.toList[bb]

    def show(self):
        judgeDic = {}
        for k, v in self.resList.items():
            judgeDic[k] = {}
            for i in self.itemSet:
                f = list(v)
                f = f[0]
                to = stateTable[i][f]
                judgeDic[k][i] = self.toList[to]
        newEnd = set()
        for i in endState:
            newEnd.add(self.toList[i])
        return judgeDic, newEnd


if __name__ == '__main__':
    mindfa = minDFA()
    judgeDic, newEnd = mindfa.show()
    print(mindfa.resList)
    print(mindfa.toList)
    print('judgeDic', judgeDic)
    print('newEnd', newEnd)
