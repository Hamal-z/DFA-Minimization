# -*- coding: UTF-8 -*-
from toNFA import ToNFA

nfa = ToNFA()
nfa, itemSet = nfa.show()
stateTable = {'I': []}
for item in itemSet:
    stateTable[item] = []


class ToDFA(object):
    def __init__(self):
        super(ToDFA, self).__init__()

    def Iclosure(self, node, lastSet):
        node = nfa[node]
        res1 = set()
        for key, value in node.items():
            if value == -1:
                continue
            if None in value:
                res1.add(key)
        for i in res1:
            if i not in lastSet:
                lastSet.add(i)
                lastSet = lastSet | self.Iclosure(i, lastSet)
        return lastSet

    def Aclosure(self, node, item):
        node = nfa[node]
        res1 = set()
        for key, value in node.items():
            if value == -1:
                continue
            if item in value:
                res1.add(key)
        res2 = set()
        for i in res1:
            res2.add(i)
            res2 = res2 | self.Iclosure(i, set([i]))
        return res1 | res2

    def showDFA(self):
        I1 = set([nfa['S']])
        I1 = I1 | self.Iclosure(nfa['S'], I1)
        stateTable['I'].append(frozenset(I1))

        index = 0
        while(index < len(stateTable['I'])):

            for item in range(len(itemSet)):
                res = set()
                for node in stateTable['I'][index]:
                    res = res | self.Aclosure(node, itemSet[item])
                stateTable[itemSet[item]].append(frozenset(res))
                if len(res) == 0:
                    continue
                if res not in stateTable['I']:
                    stateTable['I'].append(frozenset(res))
            index += 1

        return stateTable

    def newTable(self, stateTable):
        newState = {}
        endState = []
        for i in range(len(stateTable['I'])):
            newState[stateTable['I'][i]] = i
            if nfa['N'] in stateTable['I'][i]:
                endState.append(i)

        for key, value in stateTable.items():
            for i in range(len(value)):
                value[i] = newState.get(value[i], '.')

        matrix = [[key for key in stateTable]]
        for i in range(len(stateTable['I'])):
            matrix.append([])
            for item in stateTable.values():
                matrix[-1].append(item[i])
        return stateTable, endState, matrix


if __name__ == '__main__':
    stateTable = ToDFA().showDFA()
    print(stateTable)
    stateTable, endState, matrix = ToDFA().newTable(stateTable)
    print(matrix)
    print('endState', endState)
    print(stateTable)
    for key in stateTable:
        print('|'),
        print(key),
    print('|')
    for i in range(len(stateTable['I'])):
        for item in stateTable.values():
            print('|'),
            print(item[i]),
        print('|')
