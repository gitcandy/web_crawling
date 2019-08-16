# -*- coding: utf-8 -*-
class Task:

    def concaveValley(self,X):
        num_len = []
        max_len = 0
        change_num=[0]
        a = 0
        len_x  = len(X)
        for i in range(0,len_x-1):
            num_len.append(int(X[i]>=X[i+1]))
        print(num_len)
        for i in range(0,len_x-2):
            if (num_len[i]-num_len[i+1]==-1):
                # 判断低谷结束的位置
                change_num.append(i+2)
            if (num_len[i]-num_len[i+1]==1):
                # 判断要存在低谷
                a = 1
        #         如果存在低谷且当前只有一个低谷的时候，长度为当前的数组长度
        if (len(change_num)==1 and a==1):
            change_num.append(len_x)
            max_len = len_x
            print(len(change_num))
        #     如果存在低谷且当前不止一个低谷的时候，长度为变化低谷的相减的位置
        else:
            for j in range(0,len(change_num)-1):
                if a==1:
                    step = change_num[j+1]-change_num[j]
                    if step>=max_len:
                        max_len=step
        # print(str(max_len),change_num,a)
        return max_len


    #********* Begin *********#

new_x = [5,2,4,5,8,10]
mytask = Task()
mytask.concaveValley(new_x)

    #********* End *********#
