import pickle
import numpy as np
class Store():

    def store2txt(self):
        with open('path/zj_pseudoknot.txt', "wb") as f:
            pickle.dump(self.list_t, f)

    #print(compare_distance(test1, test2))

    def hanshu(x):
        return round(1/(1 + x), 2)
    def solveAve(self,a,list_seq):
        #fscv = open('平均值结果.csv', "w")
        m1, m2 = 0, 0
        a[0, 0] = [100, 100]
        list_ave = []
        while m1 < a.shape[1]:
            number = 0
            while m2 < a.shape[0]:
                if m1 != m2:
                    a1 = np.mean(a[m1, number])
                    a2 = np.mean(a[m1, m2])
                    if np.mean(a[m1, number]) > np.mean(a[m1, m2]):
                        number = m2
                m2 += 1
                #list_ave.append(np.mean(a[m1, number]))
            list_ave.append(np.mean(a[m1, number]))
            #seq = [str(list_seq[m1]), ',', str(list_seq[number]), ',', str(round(np.mean(a[m1,number]), 2)), '\n'] #
                #fscv.writelines(seq)
            m2 = 0
            m1 += 1
        #fscv.close()
        return list_ave
    def store2csv2editor(self, a, list_seq):
        fscv = open('path/pseudoknot.csv', "w")
        list_ave=self.solveAve(a,list_seq)
        m1 = 0
        m2 = 1
        while m1 < a.shape[0]:
            while m2 < a.shape[0]:
                if list_seq[m1] == 'Vf-PKB3' and list_seq[m2] == 'Rr-PKB147':
                    print('?')
                if (m1 != m2):
                #seq = [str(list_seq[m1]), ', ', str(list_seq[m2]), ', ', str(self.hanshu(self.list_t[m1][m2])), '\n']
                    seq = [str(list_seq[m1]), ',', str(list_seq[m2]), ',', str((a[m1, m2, 0])), ',',
                           str((a[m1, m2, 1])), ',', str(round((a[m1,m2,0]+a[m1,m2,1])/2, 3)),',',str(round(list_ave[m1],3)),'\n']
                    fscv.writelines(seq)
                m2 += 1
            m1 += 1
            m2 = 0
        fscv.close()
    def store2csv2distance(self,list_t, list_seq):
        fscv = open('path/pseudoknot_juli.csv', "w")
        m1 = 0
        m2 = 1
        while m1 < len(list_t.shape[0]):
            while m2 < len(list_t.shape[0]):
                if (m1 != m2):
                    seq = [str(list_seq[m1]), ',', str(list_seq[m2]), ',', str(list_t[m1][m2]), '\n']
                    fscv.writelines(seq)
                m2 += 1
            m1 += 1
            m2 = 0
        fscv.close()