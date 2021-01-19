import numpy as np
from STRtoNode import buildNode
from BuildTree import buildTree
from store import Store
class computeDistance():
    list_d2 = []  # 储存左分支对应右边所有分支的最小距离
    dict1 = {}  # 存储所有距离
    '''def __init__(self, list_p1, list_p2):
        self.list_p1 = list_p1
        self.list_p2 = list_p2'''

    def h(self,a, b):
        if a[0]<=b[0]<=a[1]<=b[1]:
            return max(abs(a[0]-b[0]), abs(a[1]-b[0]))
        elif b[0]<=a[0]<=b[1]<=a[1]:
            return max(abs(a[0]-b[1]), abs(a[1]-b[1]))
        elif a[0]<=a[1]<=b[0]<=b[1]:
            return b[0]-a[0]
        elif b[0]<=b[1]<=a[0]<=a[1]:
            return a[1]-b[1]


    def d(self,a,b):
        ra = (a[1] - a[0]) / 2
        rb = (b[1] - b[0]) / 2
        ca = a[0] + ra
        cb = b[0] + rb
        if a[0] == b[0] and a[1] == b[1]:
            return 0
        elif b[0]<=a[0]<=a[1]<=b[1] or a[0]<=b[0]<=b[1]<=a[1]:
            return max(abs(a[0]-b[0]), abs(a[1]-b[1]))
        elif ra == rb==0:
            return abs(ca-cb)         #(a[0]+(a[0]-a[1])/2)-(b[0]+(b[0]-b[1])/2)
        # else:
        #     return round(self.h(a, b)*abs(1-self.o(a, b)/(2*ra+1)), 2)
        elif b[0] < b[1] <= a[0] < a[1] or a[0] < a[1] <= b[0] < b[1]:
            return round(self.h(a, b) * (1 - self.o(a, b) / abs(ca - cb)), 2)
        else:
            return round(self.h(a, b) * abs(1 - self.o(a, b) / (ra + rb + 1)), 2)

    def compute(self, list1, list2): #计算两个分支的距离
        num1 = 0
        num2 = 0
        total = 0
        now = 0
        neone = 0
        while (num1 < len(list1)):
            if list1[num1][0] != 0:
                while (num2 < len(list2)):
                    if list2[num2][0] == 0:
                        num2 = num2 + 1
                    else:
                        if now == 0:
                            now = self.d(list1[num1], list2[num2])
                        if num2 != len(self.list2) - 1:
                            neone = self.d(list1[num1], list2[num2 + 1])
                            if now < neone:
                                total = total + now
                                now = 0
                                break
                            else:
                                now = neone
                                num2 += 1
                        else:
                            total = total + now
                            num2 += 1
            num1 = num1 + 1
        return total

    def getresult(self, result, count2): #将结果储存在一个字典里
        if count2 in self.dict1:
            if self.dict1[count2] > min(self.list_d2):
                self.dict1[count2] = min(self.list_d2)  #此处删除了一个左边树的一直，需要增加编辑距离
            else:
                self.list_d2[self.list_d2.index(min(self.list_d2))] = 10000
                self.dict1[count2] = min(self.list_d2)
        else:
            self.dict1[count2] = min(self.list_d2)  # dict1[(list.index(min(list))+1) % len(list_p2)]
        result += self.dict1[count2]
        self.list_d2.clear()
        return result

    def compare_distance(self, list_p1, list_p2):#比较两个分支
        count1 = 0  # 左分支的遍历
        count2 = 0  # 右分支的遍历
        judge = -1  # 进行删除分支操作时需要的参数
        result = 0  # 节点距离
        present = 0  # z指向当前分支的指针
        nex = 0  # 指向当前下一分支的数的集合
        while count1 < len(list_p1):
            while count2 < len(list_p2):
                if present == 0:
                    if len(list_p1[count1]) <= len(list_p2[count2]):
                        present = self.compute(list_p1[count1], list_p2[count2])
                    else:
                        present = self.compute(list_p2[count2], list_p1[count1])
                    self.list_d2.append(present)
                if count2 != len(list_p2) - 1:
                    if len(list_p1[count1]) <= len(list_p2[count2 + 1]):
                        nex = self.compute(list_p1[count1], list_p2[count2 + 1])
                    else:
                        nex = self.compute(list_p2[count2 + 1], list_p1[count1])
                        self.list_d2.append(nex)
                    if present < nex:
                        result = self.getresult(result, count2+1)
                        self.list_d2.clear()
                        break
                    else:
                        present = nex
                        count2 = count2 + 1
                else:
                    result = self.getresult(result, count2 + 1)
                    count2 = count2 + 1
                    present = 0
            present = 0
            count1 = count1 + 1
        self.dict1.clear()
        return result




if __name__ == '__main__':
    list_t = []
    struct = ''
    list_seq = []
    f = open('path/PseudoKnots.txt')   #The path of storing the data.
    for line in f:
        if line[:15] == '>RNAz cluster #':
            struct = line[15:-1]
        elif line[:10] == '>Structure':
            seq = struct + '-' + line[12:-1]
            list_seq.append(seq)
        elif line[0] == ':' or line[0] == '(':
            node = buildNode(line)
            node1 = node.generate_node()
            tree = buildTree(node1)
            tree1 = tree.generate_tree()
            list_t.append(tree1)
    f.close()
    print(list_t)
    distance = computeDistance()
    n1 = 0
    n2 = 0
    list_d1 = [[] for _ in range(len(list_t))]
    while n1 < len(list_t):
        while n2 < len(list_t):
            if len(list_t[n1]) <= len(list_t[n2]):
                list_d1[n1].append(distance.compare_distance(list_t[n1], list_t[n2]))
            else:
                list_d1[n1].append(distance.compare_distance(list_t[n2], list_t[n1]))
            n2 += 1
        n2 = 0
        n1 += 1
    a = np.array(list_d1)
    store = Store(list_t)
    store.store2csv(list_seq)
    print(a)

