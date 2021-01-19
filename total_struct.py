from BuildTree import buildTree
from STRtoNode import buildNode
from compute_distance import computeDistance
from compute_editor import computeEditor
from Store import Store
import numpy as np

def panduan(list1, node1):
    now = 0
    for i in list1:
        for j in i:
            if j[0] != 0 and j[0] != 1:
                if now > j[0]:
                    return node1
                else:
                    now = j[0]


if __name__ == '__main__':
    f = open('PseudoKnots.txt')
    list_seq = [] #存储名称标号
    #pattern = r'>+,+(+'
    list_t = []   #存储所有的树节点
    test = []
    for line in f:
        line.replace(' ', '')
        #line = line.strip()+'\n'
        if len(line) == 0:
            continue
        elif '>'in line and '(' in line and ',' not in line:
            struct = line[1:3]
        elif '>' in line and ',' in line and '(' in line:
            print(line)
            line = line.split(',')
            list_seq.append(struct +'-'+ line[0][1:])
        elif line[0] == ':' or line[0] == '(':
            print(line)
            line = line.strip()+'\n'
            node = buildNode(line)
            node1 = node.generate_node()
            print(node1)
            tree = buildTree(node1)
            result1 = tree.generate_tree()
            list_t.append(result1)
            print(result1)
            #test1 = panduan(result1, node1)
            '''if test1 != None:
                test.append(test1)'''
            node1.clear()
    #editor = computeEditor()
    n1, n2 = 0, 0
    list_d1 = [[] for _ in range(len(list_t))]
    while n1 < len(list_t):
        print('n1')
        print(n1)
        while n2 < len(list_t):
            editor = computeEditor()
            if len(list_t[n1]) <= len(list_t[n2]):
                print(n2)
                list_d1[n1].append(editor.compare_distance(list_t[n1], list_t[n2]))
            else:
                print(n2)
                list_d1[n1].append(editor.compare_distance(list_t[n2], list_t[n1]))
            n2 += 1
        n2 = 0
        n1 += 1
    a = np.array(list_d1)
    store = Store()
    store.store2csv2editor(a,list_seq)
    #store.solveAve(a, list_seq)
    # print(list_d1)[[24, 29, 3, 'T3L'], [21, 33, 4, 'T3L'], [16, 38, 5, 'T3L'], [60, 68, 3, 'T3L'], [6, 71, 7, 'T3L'], [63, 78, 2, 'T2u1'], [112, 118, 9, 'T3L'], [135, 139, 4, 'T3L'], [102, 143, 6, 'T3L'], [94, 152, 12, 'T3L'], [57, 169, 7, 'T2u1'], [49, 176, 4, 'T2u1']]
    # print('错误结果')
    # print(test)