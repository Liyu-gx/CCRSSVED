import numpy as np
from STRtoNode import buildNode
from BuildTree import buildTree
import pickle

class computeEditor():
    list_d2 = []  # 储存左分支对应右边所有分支的最小距离
    dict1 = {}  # 存储所有距离
    mer = 0.75
    delt = 1.75
    count = 0
    '''def __init__(self, list_p1, list_p2):
        self.list_p1 = list_p1
        self.list_p2 = list_p2'''
    def s(self, total):  #计算各个分支内节点距离的平均值或者总和
        sum_distance = 0
        sum_count = 0
        for i in total:
            if len(i) != 0:
                sum_distance += i[1]
                sum_count += 1
        return round(sum_distance/sum_count, 2)
        #return sum_distance
    def o(self, a,b):
        ra = (a[1] - a[0])/2
        rb = (b[1] - b[0])/2
        ca = a[0] + ra
        cb = b[0] + rb
        # if a[0]<=b[0]<=a[1]<=b[1] or b[0]<=a[0]<=b[1]<=a[1]:
        #    return abs(ca-cb)+ra+rb
        # else:
        #     return ca-cb+ra+rb
        if a[0] <= b[0] <= b[1] <= a[1]:
            return 2 * rb
        elif b[0] <= a[0] <= a[1] <= b[1]:
            return 2 * ra
        else:
            return ra + rb - abs(ca - cb)


    def h(self, a, b):
        if a[0]<=b[0]<=a[1]<=b[1]:
            return max(abs(a[0]-b[0]), abs(a[1]-b[0]))
        elif b[0]<=a[0]<=b[1]<=a[1]:
            return max(abs(a[0]-b[1]), abs(a[1]-b[1]))
        elif a[0]<=a[1]<=b[0]<=b[1]:
            return b[0]-a[0]
        elif b[0]<=b[1]<=a[0]<=a[1]:
            return a[1]-b[1]


    def d(self, a,b):
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
        #else:
            #return round(self.h(a, b)*abs(1-self.o(a, b)/(2*ra+1)), 2)
        elif b[0] < b[1] <= a[0] < a[1] or a[0] < a[1] <= b[0] < b[1]:
            return round(self.h(a, b) * (1 - self.o(a, b) / abs(ca - cb)), 2)
        else:
            return round(self.h(a, b) * abs(1 - self.o(a, b) / (ra + rb + 1)), 2)



    def compute(self, list1, list2): #计算两个分支间的距离
        num1 = 0
        num2 = 0
        total = [[] for i in range(len(list1))]
        now = 0
        neone = 0
        changdu = 0
        edit = 0
        c_judge = -1
        while(num1 < len(list1)):
            if list1[num1][0] != 0 and list1[num1][0] != 1:
                while(num2 < len(list2)):
                    if list2[num2][0] == 0 or list2[num2][0] == 1:
                        num2 = num2 + 1
                    else:
                        if now == 0:
                            now = self.d(list1[num1], list2[num2])
                        if num2 != len(list2) - 1:
                            neone = self.d(list1[num1], list2[num2+1])
                            if now < neone:
                                if num1 != 0 and c_judge == num2:
                                    if total[num1 - 1][0] == num2 and total[num1 - 1][1] > now:
                                        total[num1 - 1].clear()
                                        edit += self.delt * list1[num1 - 1][2]
                                total[num1] = [num2, now]
                                # if now==0:
                                #     edit += self.mer * abs(list1[num1][2] - list2[num2][2])
                                c_judge = num2
                                if changdu > 0 and list1[num1][2] > list2[num2][2]:
                                    if list1[num1][2] - (changdu + list2[num2][2]) >= 0:
                                        edit += self.mer * (list1[num1][2] - (changdu + list2[num2][2]))
                                    else:
                                        edit += self.delt * ((changdu + list2[num2][2]) - list1[num1][2])
                                    changdu = 0
                                elif changdu > 0 and list1[num1][2] <= list2[num2][2]: #如果左支长度大的时候直接删除changdu里的
                                    edit += self.delt * changdu
                                    changdu = 0
                                else:
                                    edit += self.mer * abs(list1[num1][2] - list2[num2][2])
                                now = 0
                                break
                            else:
                                now = neone
                                if c_judge != num2:
                                    changdu = list2[num2][2] + changdu
                                    c_judge = num2
                                num2 += 1
                        else:
                            total[num1] = [num2, now]
                            # if now == 0:
                            #     edit += self.mer * abs(list1[num1][2] - list2[num2][2])
                            if changdu > 0 and list1[num1][2] > list2[num2][2]: #如果左支长度小的时候进行整合
                                if list1[num1][2] - (changdu + list2[num2][2]) >= 0:
                                    edit += self.mer * (list1[num1][2] - (changdu + list2[num2][2]))
                                else:
                                    edit += self.delt * ((changdu + list2[num2][2]) - list1[num1][2])
                                changdu = 0
                            elif changdu > 0 and list1[num1][2] <= list2[num2][2]: #如果左支长度大的时候直接删除changdu里的
                                edit += self.delt * changdu
                                changdu = 0
                            else:
                                edit += self.mer * abs(list1[num1][2] - list2[num2][2])
                            num2 += 1
            if num2 != len(list2):
                num1 = num1 + 1
            else:
                break
        while num1< len(list1)-1:
            num1 = num1 + 1
            edit += self.delt * list1[num1][2]
        while num2 < len(list2)-1:   #
            num2 += 1
            try:
                edit = edit + self.delt * list2[num2][2]
            except Exception as e:
                print('出现问题，请及时检查')
        return [self.s(total), edit]


    def getresult(self, result, editor, count1, count2, list_p1, present, nex):
        if count2 in self.dict1:
            if self.dict1[count2] > min(self.list_d2):
                self.dict1[count2] = min(self.list_d2)  #此处删除了一个左边树的一直，需要增加编辑距离
                for delte in list_p1[count1-1]:
                    if delte[0] != 0 and delte[0] != 1:
                        editor += self.delt * delte[2]
            else:
                if len(self.list_d2) != 1: #最后一个分支的时候，出现这种情况，他比上一个分支要打，只能删去当前分支
                    self.list_d2[self.list_d2.index(min(self.list_d2))] = 10000
                    count2 += 1
                    self.dict1[count2] = min(self.list_d2)
                    try:
                        editor += nex[1]
                    except Exception as e:
                        print(list_p1)
                        print(nex)
                else:
                    result -= self.dict1[count2]

        else:
            self.dict1[count2] = min(self.list_d2)  # dict1[(list.index(min(list))+1) % len(list_p2)]
            #count2_1 = list_d2.index(min(list_d2))
            editor += present[1]
        #print(result)
        #print(self.dict1[count2])
        result += self.dict1[count2]
        self.list_d2.clear()
        return round(result, 2), editor

    def compare_distance(self, list_p1, list_p2, num=0): #num用来区分是否为假借分支，默认为0，代表将无假借
        count1 = 0  # 左分支的遍历
        count2 = 0  # 右分支的遍历
        editor = 0  # 编辑距离
        judge = -1  # 进行删除分支操作时需要的参数
        result = 0  # 节点距离
        present = []  # z指向当前分支的指针
        nex = []  # 指向当前下一分支的数的集合
        list_p3 = []
        list_p4 = []
        result1 = 0
        editor1 = 0
        #print('list1:', list_p1)
        #print('list2:', list_p2)
        while count1 < len(list_p1):
            if list_p1[count1][0][0] == num:
                list_p3.append(list_p1[count1])
            else:
                while count2 < len(list_p2):
                    if list_p2[count2][0][0] == num:
                        list_p4.append(list_p2[count2])
                        count2 += 1
                    else:
                        if len(present) == 0:
                            if len(list_p1[count1]) <= len(list_p2[count2]):
                                present = self.compute(list_p1[count1], list_p2[count2])
                            else:
                                present = self.compute(list_p2[count2], list_p1[count1])
                            self.list_d2.append(present[0])
                        while count2 != len(list_p2) - 1 and list_p2[count2+1][0][0] == num:
                            list_p4.append(list_p2[count2+1])
                            count2 += 1
                        if count2 != len(list_p2) - 1 and list_p2[count2+1][0][0] != num:
                            if len(list_p1[count1]) <= len(list_p2[count2 + 1]):
                                nex = self.compute(list_p1[count1], list_p2[count2 + 1])
                            else:
                                nex = self.compute(list_p2[count2 + 1], list_p1[count1])
                            self.list_d2.append(nex[0])
                            if present[0] < nex[0]:
                                result, editor = self.getresult(result, editor, count1, count2 + 1, list_p1, present, nex)
                                judge = count2
                                break
                            else:
                                present = nex
                                if judge != count2:
                                    for delte in list_p2[count2]:
                                        if delte[0] != 0 and delte[0] != 1:
                                            editor += self.delt * delte[2]
                                    judge = count2
                                count2 = count2 + 1
                        else:
                            result, editor = self.getresult(result, editor, count1, count2 + 1, list_p1, present, nex)
                            count2 = count2 + 1
                            present.clear()
            present.clear()
            '''if count2 != len(list_p2):
                count1 = count1 + 1
            else:
                break  
            count1 += 1

        self.count = self.count + len(self.dict1)
        #result = round(result/len(self.dict1), 2)
        while count1 < len(list_p1)-1:
            count1 = count1 + 1
            for delte in list_p1[count1]:
                if delte[0] != 0:
                    editor += self.delt * delte[2]
        while count2 < len(list_p2)-1:
            count2 = count2 + 1
            for delte in list_p2[count2]:
                if delte[0] != 0 and delte[0] != 1:
                    editor += self.delt * delte[2]
        if len(list_p3) != 0 and len(list_p4) != 0:  #迭代求无假借的分支
            self.delt = 1.25
            self.mer = 0.5
            self.dict1.clear()
            result1, editor1 = self.compare_distance(list_p3, list_p4, 1)
        else:
            for fenzhi in list_p3:
                for i in fenzhi:
                    if i[0] != 0:
                        editor += i[2] * self.delt
            for fenzhi in list_p4:
                for i in fenzhi:
                    if i[0] != 0:
                        editor += i[2] * self.delt
        result = round((result+result1)/self.count, 2)
        self.dict1.clear()
        #self.count = 0
        #self.mer = 0.75
        #self.delt = 1.75
        return [result, editor+editor1]



if __name__ == '__main__':
    list_p1 = [[[1, 'T5Ld'], [23, 32, 12, 'T3L'], [31, 60, 5, 'T2u1']], [[0, 'right'], [57, 66, 7, 'T3L']]]
    list_p2 = [[[1, 'T5Ld'], [12, 29, 12, 'T3L'], [19, 55, 6, 'T2u1']], [[0, 'right'], [47, 67, 2, 'T3L'], [53, 61, 5, 'T3L']]]
    edt = computeEditor()
    if len(list_p1) <= len(list_p2):
        result = edt.compare_distance(list_p1,list_p2)
    else:
        result = edt.compare_distance(list_p2,list_p1)
    print(result)