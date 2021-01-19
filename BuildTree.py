
class buildTree():
    def __init__(self, list_a):
        self.list_a = []
        self.list_b = []
        for i in list_a:
            if i[3] == 'T3L':
                self.list_a.append(i)
            else:
                self.list_b.append(i)

    def iscontain(self, a, b):   #嵌套关系
        if (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1]):
            return True
        return False

    def isparallel(self, a , b):    #平行关系
        if (a[0] < b[0] and a[1] < b[0]) or (a[0] > b[0] and a[1] > b[1]):
            return True
        return False

    def istersect(self,a , b):      #交叉关系
        if (a[0]<b[0] and a[1]<b[1] and b[0]<a[1]) or (b[0]<a[0] and b[1]<a[1] and a[0]<b[1]):
            return True
        return False
    def generate_tree(self):
        j = 0
        k = 0
        p = 0
        q = 0
        list_p = []
        bool_top = True
        n = len(self.list_a)
        list_in = [-1, -1]
        while k < n-1:
            if j == 0:
                while k < n-1 and self.iscontain(self.list_a[k + 1], self.list_a[k]):
                    k = k + 1
            elif bool_top:
                while k < n-1 and self.iscontain(self.list_a[k + 1], self.list_a[k]) and self.isparallel(self.list_a[p-1], self.list_a[k+1]):  #判断嵌套关系
                    k = k + 1
            elif k < n-1 and self.iscontain(self.list_a[k+1], self.list_a[p-1]):
                while self.iscontain(self.list_a[k], self.list_a[p-1]) and k < n-1:
                #while k < n-1 and self.iscontain(self.list_a[k + 1], self.list_a[k]):
                    #k = k + 1
                    i = 0
                    list_p1 = list_p[:k]
                    while i < len(list_p1) and k < n-1 :
                    #for i, j in enumerate(list_p[:k]):
                        if self.iscontain(self.list_a[k],list_p1[i][-1] ): #j[-1]
                            if q != 0 and q != i:
                                list_p.insert(q, [[0, 'T5Lu']])
                                list_a1 = self.list_a[p:k]
                                list_a1.reverse()
                                list_p[q].extend(list_a1)
                                q = 0
                                j = j + 1
                                k = k+1
                                p = k
                                break
                            q = i
                            k = k+1
                            break
                        i += 1

            else:
                while k<n-1 and self.iscontain(self.list_a[k + 1], self.list_a[k])and self.isparallel(self.list_a[p-1], self.list_a[k+1]):  #判断嵌套关系
                    k = k + 1
                list_in[0] = 0
            if k == n - 1 and j == 0:
                self.list_a.reverse()
                list_p = [self.list_a]
                list_p[j].insert(0, [0, 'T1'])
                k = k + 1
            elif k == n -1 and j != 0 and bool_top:
                list_p.append([[0, 'right']])
                list_a1 = self.list_a[p:]
                list_a1.reverse()
                list_p[j].extend(list_a1)
                k = k + 1
            elif k < n-1 and self.isparallel(self.list_a[k], self.list_a[k+1]):
                list_p.append([[0, 'T5Ld']])
                list_a1 = self.list_a[p:k+1]
                list_a1.reverse()
                list_p[j].extend(list_a1)
                j = j + 1
                k = k + 1
                p = k
            elif k < n-1 and j != 0 and self.iscontain( self.list_a[k+1], self.list_a[p-1]):  #嵌套关系
                if self.isparallel(self.list_a[p-1], self.list_a[k]):
                    list_p.append([[0, 'right']])
                    list_a1 = self.list_a[p:k+1]
                    list_a1.reverse()
                    list_p[j].extend(list_a1)
                    j = j + 1
                    k = k + 1
                    p = k
                    while k<n-1 and self.iscontain(self.list_a[k+1], self.list_a[k]):
                        qian = True
                        for z in self.list_a[:k]:
                            if z[0] < self.list_a[k][0] and z[0] > self.list_a[k+1][0]:
                                qian = False
                                break
                        if qian:
                            k = k + 1
                        else:
                            break
                    l = 0
                    m = 1
                    while m < j:
                        if list_p[m-1][1][0] < self.list_a[k][0] < list_p[m][1][0]:
                            l = m
                            break
                        m += 1
                    list_p.insert(l, [[0, 'T5Lu']])
                    list_a1 = self.list_a[p:k+1]
                    list_a1.reverse()
                    list_p[l].extend(list_a1)
                    j = j + 1
                    k = k + 1
                    p = k
                    bool_top = False
                    if list_in[0] != 0:
                        list_in[-1] = l
                    else:
                        list_p[list_in[-1]+1].insert(0, [0, 'T5Ld'])
        if k == n-1:
            if len(self.list_a) == 1:
                self.list_a.insert(0, [0, 'T1'])
                list_p = [ self.list_a]
            elif self.isparallel(self.list_a[p-1], self.list_a[k]):
                list_p.append([[0, 'right']])  #j-1右分支
                list_a1 = self.list_a[p:k+1]
                list_a1.reverse()
                list_p[j].extend(list_a1)
            else:
                for i, j in enumerate(list_p[:k]):
                    if self.iscontain(self.list_a[k], j[1]):
                        list_p.insert(i, [[0, 'T5Lu']])
                        list_a1 = self.list_a[p:k + 1]
                        list_a1.reverse()
                        list_p[i].extend(list_a1)
                        break
                k += 1
        for i, node1 in enumerate(self.list_b):
            for j, node2 in enumerate(list_p):
                jia = 0
                jia_bool = False  # 为了减少循环次数
                while jia < len(node2):
                    if node2[jia][0] != 0 and node2[jia][0] != 1:
                        '''if node2[jia][0] < node1[0] < node2[jia][1]:
                            # list_p[i].append(self.list_a[k])
                            list_p[j].insert(jia + 1, node1)
                            list_p[j][0][0] = 1
                            jia_bool = True
                            #node3 = node2[jia][1:]  # 去掉分支
                            if self.iscontain(node1, node2[jia]):
                                list_p[j][jia + 1][3].replace('u', 'd', 2)
                            break
                        else:
                            jia += 1'''
                        if node1[0] < node2[jia][0] < node1[1]:
                            list_p[j].insert(jia, node1)
                            list_p[j][0][0] = 1
                            jia_bool = True
                            if self.iscontain(node1, node2[jia]):
                                list_p[j][jia][3].replace('u', 'd', 2)
                            break
                        elif jia != len(node2)-1:
                            if (node2[jia][0] < node1[0] < node2[jia][1] ) and node2[jia+1][0] > node1[0]:
                                list_p[j].insert(jia + 1, node1)
                                #list_p[j].append(node1)
                                list_p[j][0][0] = 1
                                jia_bool = True
                                #node3 = node2[jia][1:]
                                if self.iscontain(node1, node2[jia]):
                                    list_p[j][jia + 1][3].replace('u', 'd', 2)
                                break
                            elif (node2[jia][0] < node1[0] < node2[jia][1] ) and (node2[jia+1][0]<node1[0] and node2[jia+1][1]<node1[0]):
                                list_p[j].insert(jia + 1, node1)
                                #list_p[j].append(node1)
                                list_p[j][0][0] = 1
                                jia_bool = True
                                #node3 = node2[jia][1:]
                                if self.iscontain(node1, node2[jia]):
                                    list_p[j][jia + 1][3].replace('u', 'd', 2)
                                break
                            else:
                                jia += 1
                        elif jia == len(node2)-1:
                            if (node2[jia][0] < node1[0] < node2[jia][1]):
                                list_p[j].insert(jia + 1, node1)
                                #list_p[j].append(node1)
                                list_p[j][0][0] = 1
                                jia_bool = True
                                #node3 = node2[jia][1:]
                                if self.iscontain(node1, node2[jia]):
                                    list_p[j][jia + 1][3].replace('u', 'd', 2)
                                break
                            else:
                                jia += 1

                        else:
                            jia += 1
                    else:
                        jia += 1
                if jia_bool:
                    break

        return list_p
if __name__ == '__main__':
    list_a = [[12, 29, 12, 'T3L'], [19, 55, 6, 'T2u1'], [53, 61, 5, 'T3L'], [47, 67, 2, 'T3L']]
    #list_a = [[20, 25, 4, 'T3L'], [50, 56, 6, 'T3L'], [73, 78, 4, 'T3L'], [86, 99, 5, 'T3L'], [67, 104, 5, 'T3L'], [62, 111, 1, 'T3L'], [39, 113, 2, 'T3L'], [35, 117, 7, 'T3L'], [14, 124, 5, 'T3L'], [8, 129, 2, 'T3L'], [95, 133, 6, 'T2u1']]
    #list_a = [[24, 29, 3, 'T3L'], [21, 33, 4, 'T3L'], [16, 38, 5, 'T3L'], [60, 68, 3, 'T3L'], [6, 71, 7, 'T3L'], [63, 78, 2, 'T2u1'], [112, 118, 9, 'T3L'], [135, 139, 4, 'T3L'], [102, 143, 6, 'T3L'], [94, 152, 12, 'T3L'], [57, 169, 7, 'T2u1'], [49, 176, 4, 'T2u1']]
    st = buildTree(list_a)
    print(st.generate_tree())



