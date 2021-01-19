import numpy as np
import re

def sum(total):
    sum_distance = 0
    sum_count = 0
    for i in total:
        if len(i)!=0:
            sum_distance +=i[1]
            sum_count += 1
    return round(sum_distance/sum_count, 2)
    #return sum_distance



def iscontain(a, b):
    if (a[0] < b[0] and a[1] > b[1]) or (a[0] > b[0] and a[1] < b[1]):
        return True
    return False


def isparallel(a , b):
    if (a[0] < b[0] and a[1] < b[0]) or (a[0] > b[0] and a[1] > b[1]):
        return True
    return False


def istersect(a , b):
    if a[0]<b[0] and a[1]<b[1]:
        return True
    return False


def o(a,b):
    ra = (a[1] - a[0])/2
    rb = (b[1] - b[0])/2
    ca = a[0] + ra
    cb = b[0] + rb
    if a[0] <= b[0] <= b[1] <= a[1]:
        return 2*rb
    elif b[0]<=a[0]<=a[1]<= b[1]:
        return 2*ra
    else:
        return ra+rb-abs(ca-cb)


def h(a, b):
    if a[0]<=b[0]<=a[1]<=b[1]:
        return max(abs(a[0]-b[0]), abs(a[1]-b[0]))
    elif b[0]<=a[0]<=b[1]<=a[1]:
        return max(abs(a[0]-b[1]), abs(a[1]-b[1]))
    elif a[0]<=a[1]<=b[0]<=b[1]:
        return b[0]-a[0]
    elif b[0]<=b[1]<=a[0]<=a[1]:
        return a[1]-b[1]


def d(a,b):
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
    elif b[0]<b[1]<=a[0]<a[1] or a[0]<a[1]<=b[0]<b[1]:
        return round(h(a, b)* (1-abs(o(a, b)/(ca-cb))), 2)
    else:
        return round(h(a, b)*abs(1-o(a, b)/(ra+rb+1)), 2)

def compute(list1, list2):
    num1 = 0
    num2 = 0
    total = [[] for i in range(len(list1))]
    now = 0
    neone = 0
    changdu = 0
    edit = 0
    c_judge = -1 #用来判断
    while(num1 < len(list1)):
        if list1[num1][0] != 0:
            while(num2 < len(list2)):
                if list2[num2][0] == 0:
                    num2 = num2 + 1
                else:
                    if now == 0:
                        now = d(list1[num1], list2[num2])
                    if num2 != len(list2) - 1:
                        neone = d(list1[num1], list2[num2+1])
                        if now < neone:
                            if num1 !=0 and c_judge == num2:
                                if total[num1-1][0] == num2 and total[num1-1][1] > now:
                                    total[num1-1].clear()
                                    edit += 0.5 * list1[num1-1][2]
                            total[num1] = [num2, now]
                            c_judge = num2
                            if changdu > 0 and list1[num1][2] > list2[num2][2]:
                                if list1[num1][2] - (changdu + list2[num2][2]) >= 0:
                                    edit += 0.5 * (list1[num1][2] - (changdu + list2[num2][2]))
                                else:
                                    edit += 1.25 * ((changdu + list2[num2][2]) - list1[num1][2])
                                changdu = 0
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
                        if changdu > 0 and list1[num1][2] > list2[num2][2]:
                            if list1[num1][2] - (changdu+list2[num2][2]) >= 0:
                                edit += 0.5 * (list1[num1][2] - (changdu+list2[num2][2]))
                            else:
                                edit += 1.25 * ((changdu + list2[num2][2])-list1[num1][2])
                            '''if changdu <= (list1[num1][2] - list2[num2][2]):  # 在判断是否合并时，根据是什么？
                                edit += 0.5 * changdu
                            else:
                                edit += 1.25 * list2[num2 - 1][2]'''
                        num2 += 1
        if num2 != len(list2):
            num1 = num1 + 1
        else:
            break
    while num1< len(list1)-1:
        num1 = num1 + 1
        edit += 1.25*list1[num1][2]
    while num2 < len(list2)-1:   #
        num2 += 1
        try:
            edit = edit + 1.25 * list2[num2][2]
        except Exception as e:
            print(list2)
            print(list_t[n1])
            print(list_t[n2])

    return [sum(total), edit]


def getresult(result, editor, count1, count2, list_p1, present, nex):
    global bool_nex
    if count2 in dict1:
        if dict1[count2] > min(list_d2):
            result -= dict1[count2]
            dict1[count2] = min(list_d2)  #此处删除了一个左边树的一直，需要增加编辑距离
            for delte in list_p1[count1-1]:
                if delte[0] != 0:
                    editor += 1.25 * delte[2]
        else:
            list_d2[list_d2.index(min(list_d2))] = 10000
            count2=count2+1
            dict1[count2] = min(list_d2)
            bool_nex = True
            #dict1[count2 + count1] = min(list_d2)
            try:
                editor += nex[1]
            except Exception as e:
                print(list_p1)
                print(nex)

    else:
        dict1[count2] = min(list_d2)  # dict1[(list.index(min(list))+1) % len(list_p2)]
        #count2_1 = list_d2.index(min(list_d2))
        editor += present[1]
    result += dict1[count2]
    list_d2.clear()
    return round(result, 2), editor

def compare_distance(list_p1, list_p2):
    global bool_nex
    count1 = 0  # 左分支的遍历
    count2 = 0  # 右分支的遍历
    editor = 0  # 编辑距离
    judge = -1  # 进行删除分支操作时需要的参数
    result = 0  # 节点距离
    present = []  # 指向当前分支的指针
    nex = []  # 指向当前下一分支的数的集合
    while count1 < len(list_p1):
        while count2 < len(list_p2):
            if len(present) == 0:
                if len(list_p1[count1]) <= len(list_p2[count2]):
                    present = compute(list_p1[count1], list_p2[count2])
                else:
                    present = compute(list_p2[count2], list_p1[count1])
                list_d2.append(present[0])
            if count2 != len(list_p2) - 1:
                if len(list_p1[count1]) <= len(list_p2[count2 + 1]):
                    nex = compute(list_p1[count1], list_p2[count2 + 1])
                else:
                    nex = compute(list_p2[count2 + 1], list_p1[count1])
                list_d2.append(nex[0])
                if present[0] < nex[0]:
                    result, editor = getresult(result, editor, count1, count2 + 1, list_p1, present, nex)
                    if bool_nex:
                        count2 += 1
                        bool_nex = False
                    judge = count2
                    break
                else:
                    present = nex
                    if judge != count2:
                        for delte in list_p2[count2]:
                            if delte[0] != 0:
                                editor += 1.25 * delte[2]
                        judge = count2
                    count2 = count2 + 1
            else:
                result, editor = getresult(result, editor, count1, count2 + 1, list_p1, present, nex)
                count2 = count2 + 1
                present.clear()
        present.clear()
        if count2 != len(list_p2) - 1:
            count1 = count1 + 1
        else:
            break
    while count1 < len(list_p1)-1:
        count1 = count1 + 1
        for delte in list_p1[count1]:
            if delte[0] != 0:
                editor += 1.25 * delte[2]
    while count2 < len(list_p2)-1:
        count2 = count2 + 1
        for delte in list_p2[count2]:
            if delte[0] != 0:
                editor += 1.25 * delte[2]
    result = round(result/len(dict1), 2)
    return [result, editor]


list_d2 = []        #储存左分支对应右边所有分支的最小距离

dict1={}            #存储所有距离
list_t = []
struct=''
list_seq = []
pattern = r'>+.+/+\-+'
f = open('Path/RNAz cluster #86486.txt')  #The path of storing the data.
global bool_nex
bool_nex=False
for line in f:
    line = line.strip()+'\n'
    if len(line) == 0:
        continue
    elif line[:12] == '>Structure #':
        struct = line[12:-1]
    elif '-' in line and '.' in line and '/' in line:
        seq = line.split('.')
        list_seq.append(struct+'-'+seq[0][1:])
    elif line[0] == '.' or line[0] == '(':
        print(line)
        tag = line
        count = 0
        stack = []
        r_list = []
        length = 0
        while count < len(tag) - 1:
            if tag[count] == '(':
                stack.append(count)
                count = count + 1
            if tag[count] == '.':
                if tag[count - 1] == '(' or tag[count + 1] == ')':  # 左括号的下一个或者右括号的前一个点进栈
                    stack.append('.')
                    count = count + 1
                else:
                    count = count + 1
            while tag[count] == ')':
                if stack[-1] == '.':
                    stack.pop()
                    if (stack[-1]) != '.':
                        sanyuan = [stack[-1], count]
                        stack.pop()
                        count = count + 1
                        length = length + 1
                    if tag[count] != ')':
                        sanyuan.append(length)
                        r_list.append(sanyuan)
                        length = 0
                elif (stack[-1]) != '(' and (tag[count + 1] == '.' or tag[count + 1] == '(' or tag[count + 1] == '\n'):
                    stack.pop()
                    length = length + 1
                    count = count + 1
                    sanyuan.append(length)
                    r_list.append(sanyuan)
                    length = 0
                else:
                    stack.pop()
                    count = count + 1
                    length = length + 1
                    if stack[-1] == '.':
                        sanyuan.append(length)
                        r_list.append(sanyuan)
                        length = 0
        #print(r_list)
        list_a = r_list
        j = 0
        k = 0
        p = 0
        n = len(list_a)
        list_p = []
        bool_top = True
        list_in = [-1, -1]
        while k < n - 1:
            if j == 0:
                while k < n - 1 and iscontain(list_a[k + 1], list_a[k]):
                    k = k + 1
            elif bool_top:
                while k < n - 1 and iscontain(list_a[k + 1], list_a[k]) and isparallel(list_a[p - 1], list_a[k + 1]):
                    k = k + 1
            elif iscontain(list_a[k + 1], list_a[k]):
                while k < n - 1 and iscontain(list_a[k + 1], list_a[k]) and (isparallel(list_a[p - 1], list_a[k + 1])or iscontain(list_a[p-1], list_a[k+1])):
                    k = k + 1
            else:
                while k < n - 1 and iscontain(list_a[k + 1], list_a[k]) and isparallel(list_a[p - 1], list_a[k + 1]):  # 判断嵌套关系
                    k = k + 1
                list_in[0] = 0
            if k == n - 1 and j == 0:
                list_a.reverse()
                list_p = [list_a]
                k = k + 1
            elif k == n - 1 and j != 0 and bool_top:
                list_p.append([[0, 'right']])
                list_a1 = list_a[p:]
                list_a1.reverse()
                list_p[j].extend(list_a1)
                k = k + 1
            elif k < n-1 and isparallel(list_a[k], list_a[k + 1]):
                list_p.append([[0, 'T5Ld']])
                list_a1 = list_a[p:k + 1]
                list_a1.reverse()
                list_p[j].extend(list_a1)
                j = j + 1
                k = k + 1
                p = k
            elif k < n-1 and j != 0 and iscontain(list_a[k + 1], list_a[p - 1]):
                if isparallel(list_a[p - 1], list_a[k]):
                    list_p.append([[0, 'right']])
                    list_a1 = list_a[p:k + 1]
                    list_a1.reverse()
                    list_p[j].extend(list_a1)
                    j = j + 1
                    k = k + 1
                    p = k
                    while k < n - 1 and iscontain(list_a[k + 1], list_a[k]):
                        qian = True
                        for z in list_a[:k]:
                            if z[0] < list_a[k][0] and z[0] > list_a[k + 1][0]:
                                qian = False
                                break
                        if qian:
                            k = k + 1
                        else:
                            break
                    l = 0
                    m = 1
                    while m < j:
                        if list_p[m - 1][1][0] < list_a[k][0] < list_p[m][1][0]:
                            l = m
                            break
                        m += 1
                    list_p.insert(l, [[0, 'T5Lu']])
                    list_a1 = list_a[p:k + 1]
                    list_a1.reverse()
                    list_p[l].extend(list_a1)
                    j = j + 1
                    k = k + 1
                    p = k
                    bool_top = False
                    if list_in[0] != 0:
                        list_in[-1] = l
                    else:
                        list_p[list_in[-1] + 1].insert(0, [0, 'T5Ld'])
        if k == n - 1:
            if isparallel(list_a[p - 1], list_a[k]):
                list_p.append([[0, 'right']])  # j-1右分支
                list_a1 = list_a[p:k + 1]
                list_a1.reverse()
                list_p[j].extend(list_a1)
                if list_in[0] != 0:
                    list_in[-1] = l
                else:
                    list_p[list_in[-1]].insert(0, [0, 'T5Ld'])
            else:
                for i, j in enumerate(list_p):
                    if iscontain(list_a[k], j[1]):
                        list_p.insert(i, [[0, 'T5Lu']])
                        list_a1 = list_a[p:k + 1]
                        list_a1.reverse()
                        list_p[i].extend(list_a1)
                        break
        print(list_p)
        list_t.append(list_p)
f.close()
n1 = 0
n2 = 0

list_d1 = [[] for _ in range(len(list_t))]        #zuihou
while n1 < len(list_t):
    while n2 < len(list_t):
        if len(list_t[n1]) <= len(list_t[n2]):
            list_d1[n1].append(compare_distance(list_t[n1], list_t[n2]))
        else:
            list_d1[n1].append(compare_distance(list_t[n2], list_t[n1]))
        dict1.clear()
        n2 += 1
    n2 = 0
    n1 += 1

print(list_d1)

a = np.array(list_d1)
print(a)
import pickle
with open('path/86486_zj_result.txt', "wb") as f:
    pickle.dump(a, f)


fscv = open('path/86486_av_result.txt', "w")

def hanshu(x):
    return round(1/(1 + x), 2)

m1 = 0
m2 = 1
while m1 < len(list_t):
    while m2 < len(list_t):
        if (m1 != m2):
            #seq = [str(list_seq[m1]), ', ', str(list_seq[m2]), ', ', str((a[m1, m2, 0])), ',', str((a[m1, m2, 1])), ',', str(round((a[m1,m2,0]+a[m1,m2,1])/2, 3)), '\n']
            seq = [str(list_seq[m1]), ', ', str(list_seq[m2]), ', ', str((a[m1, m2, 0])), ',', str((a[m1, m2, 1])), ',', str(round(0.5*a[m1, m2, 0] + 0.5*a[m1, m2, 1], 3)), '\n']
        #seq = ['1', ',', '2', ',', str((a[m1, m2, 0])), ',', str((a[m1, m2, 1])), '\n']
            print(seq)
            fscv.writelines(seq)
        m2 += 1
    m1 += 1
    m2 = 0

fscv.close()