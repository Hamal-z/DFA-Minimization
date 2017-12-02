# -*- coding: UTF-8 -*-
from read import Read

a = Read()
rpn = a.RPN()


class ToNFA(object):
    def __init__(self):
        super(ToNFA, self).__init__()

    item = set()

    def show(self):
        operatorSet = {'|', '.', '*'}
        nfaStack = []
        nodeNum = 0
        for i in xrange(len(rpn)):
            item = rpn[i]
            if item in operatorSet:
                if item == '.':
                    b = nfaStack.pop()
                    a = nfaStack.pop()
                    del a[a['N']][None]
                    a[a['N']].update(b[b['S']])
                    for key, value in b.items():
                        if key in ['S', 'N']:
                            continue
                        if b['S'] in value.keys():
                            value[a['N']] = value[b['S']]
                            del value[b['S']]
                    del b[b['S']]
                    del b['S']
                    a.update(b)
                    nfaStack.append(a)
                # elif item == '|':
                #     b = nfaStack.pop()
                #     a = nfaStack.pop()
                #     # print(a)
                #     # print(b)
                #     if b['S'] in a[a['S']]:
                #         a[a['S']][b['S']] += [None]
                #     else:
                #         a[a['S']][b['S']] = [None]

                #     if a['N'] in b[b['N']]:
                #         b[b['N']][a['N']] += [None]
                #     else:
                #         b[b['N']][a['N']] = [None]
                #     # print(a)
                #     # print(b)
                #     del b[b['N']][None]
                #     b.update(a)
                #     nfaStack.append(b)
                elif item == '|':
                    b = nfaStack.pop()
                    a = nfaStack.pop()
                    if b['S'] in a[a['S']]:
                        a[a['S']][b['S']] += [None]
                    else:
                        a[a['S']][b['S']] = [None]

                    if a['N'] in b[b['N']]:
                        b[b['N']][a['N']] += [None]
                    else:
                        b[b['N']][a['N']] = [None]
                    del b[b['N']][None]
                    b.update(a)
                    nfaStack.append(b)
                else:
                    a = nfaStack.pop()
                    if a['N'] in a[a['S']]:
                        a[a['S']][a['N']] += [None]
                    else:
                        a[a['S']][a['N']] = [None]

                    if a['S'] in a[a['N']]:
                        a[a['N']][a['S']] += [None]
                    else:
                        a[a['N']][a['S']] = [None]
                    nfaStack.append(a)
            else:
                self.item.add(item)
                nfa = {
                    'S': nodeNum,
                    'N': nodeNum + 1,
                    nodeNum: {nodeNum + 1: [item]},
                    nodeNum + 1: {None: -1}
                }
                nfaStack.append(nfa)
                nodeNum += 2

        return nfaStack.pop(), list(self.item)


if __name__ == '__main__':
    print(rpn)
    res, itemSet = ToNFA().show()
    print('--------------------------------------------')
    print(res)
    print('S:%d  N:%d' % (res['S'], res['N']))
    del res['S']
    del res['N']
    order = res.keys()
    order.sort()
    print('--------------------------------------------')
    for i in order:
        print(i, res[i])
