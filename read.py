# -*- coding: UTF-8 -*-


class Read(object):

    def __init__(self):
        super(Read, self).__init__()

    def getFormatData(self):
        Data = open("regex.dat", 'r')
        strlist = []
        for line in Data:
            strlist += [line]
        formatData = [i for i in strlist[-1]]
        formatData.pop()
        return formatData

    def RPN(self):
        stack1 = ['#']
        res = []
        regex = self.getFormatData()
        for item in regex:
            if item == '(':
                stack1.append(item)

            elif item == ')':
                while stack1[-1] != '(':
                    res.append(stack1.pop())
                stack1.pop()

            elif item == '*':
                while stack1[-1] == '*':
                    res.append(stack1.pop())
                stack1.append(item)

            elif item == '.':
                while stack1[-1] == '*' or stack1[-1] == '.':
                    res.append(stack1.pop())
                stack1.append(item)

            elif item == '|':
                while stack1[-1] != '#' and stack1[-1] != '(':
                    res.append(stack1.pop())
                stack1.append(item)

            else:
                res.append(item)

        while stack1[-1] != '#':
            res.append(stack1.pop())

        return res


if __name__ == '__main__':
    a = Read()
    print(a.RPN())
