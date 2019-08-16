# -*- coding: utf-8 -*-
class Task:
    def virusArea(self, n, m, area):
        virus_num = 0
        viruns = 0
        a = []
        b = []
        # count = 0
        for  i in range(0,n):
            for j in range(0,m):
                if area[i][j]=='o':
                    viruns = viruns+1
                    a.append(i)
                    b.append(j)
                    # print('area[:',i,"][",j,']',area[i][j])
                    # if area[i][j]==area[i+1][j]:
                    #     virus_num+=1
                    # if  area[i][j]==area[i+1][j]:
                    #     # virus_num+=1
        # print(viruns,'a:',a,'b:',b)
        count = 0
        for i in range(len(a)):
            for j in range(len(a)):
                if a[i]==a[j] and i!=j:

                    # print('相等的行:a[',i,']','a[',j,']',a[i],a[j])
                    if (b[j]==b[i]-1 and b[i]-1>=0 or b[j]-1==b[i] and b[j]-1>=0) :
                        # print('对应的列值:','b[',i,']','b[',j,']', b[i], b[j])
                        count = count+1
                if b[i]==b[j] and i!=j:
                    # print('相等的列:','b[',i,']','b[',j,']', b[i], b[j])
                    if (a[j]==a[i]-1 and a[i]-1>=0 or a[j]-1==a[i] and a[j]-1>=0) :
                        # print('对应的行值:a[',i,']','a[',j,']:', a[i], a[j])
                        count = count+1

        print(int(count/2))

mytask= Task()
new_area=[['x','o','x','x','x'],['x','x','x','o','x'],['x','x','o','o','x'],['x','x','x','x','x']]
# new_area=[['x','o','x','o','x','x'],['x','x','x','o','o','x'],['x','o','x','x','x','x'],['x','o','x','o','o','x']]

mytask.virusArea(4,5,new_area)
# print( new_area[1][1])


    # ********* Begin *********#


    # ********* End *********#