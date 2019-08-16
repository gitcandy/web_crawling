class Task:
    def sort(self, xlist):

        step = 0
        t = 0
        step = 1
        len_list = len(xlist)


        while(step==1):
            # print(' '.join(str(a) for a in xlist))
            count = 0
            for i in  range(0,len_list-1):
                if xlist[i] > xlist[i+1]:
                    count = count+1
                    step = 1
                if count ==0:
                    step = 0


            for i in  range(0,len_list-1):
                if xlist[i] > xlist[i+1]:
                    step = 1
                    t = xlist[i]
                    count = 1
                    xlist[i] = xlist[i+1]
                    xlist[i+1] = t

                    print(' '.join(str(a) for a in xlist))
                # else:
                #     step = 0

            for i in  range(1,len_list):
                if xlist[len_list-i-1] > xlist[len_list-i]:
                    step = 1
                    count = 1
                    t = xlist[len_list-i-1]
                    xlist[len_list-i-1] = xlist[len_list-i]
                    xlist[len_list-i] = t

                    print(' '.join(str(a) for a in mylist))
                # else:
                #     step = 0
            # if count ==0:
            #     print(' '.join(str(a) for a in mylist))
            #     step = 0







mytask = Task()
mylist = [1,5,4,3,2,6]
len_list = len(mylist)
sep = ' '
mytask.sort(mylist)
# sep = sep.join(str(i) for i in mylist)
# print(sep)
#
# print(' '.join(str(i) for  i in mylist))








    # ********* Begin *********#


    # ********* End *********#



# -*- coding: utf-8 -*-
class Task:
    def sort(self, xlist):
        # ********* Begin *********
        t = 0
        step = 1
        count = 1
        len_list = len(xlist)
        while (step == 1):

            for i in range(0, len_list - 1):
                if xlist[i] > xlist[i + 1]:
                    t = xlist[i]
                    xlist[i] = xlist[i + 1]
                    xlist[i + 1] = t
                    step = 1
                    count = 0
                    print(' '.join(str(a) for a in xlist))
                else:
                    step = 0
            for i in range(1, len_list):
                if xlist[len_list - i - 1] > xlist[len_list - i]:
                    t = xlist[len_list - i - 1]
                    xlist[len_list - i - 1] = xlist[len_list - i]
                    xlist[len_list - i] = t
                    step = 1
                    count = 0
                    print(' '.join(str(a) for a in xlist))

            if count == 1:
                print(' '.join(str(a) for a in xlist))
                step = 0
            else:
                cc_ount = 0
                for i in range(0, len_list - 1):
                    if xlist[i] > xlist[i + 1]:
                        cc_ount = cc_ount + 1
                        step = 1
                    if cc_ount == 0:
                        step = 0


                        # ********* End *********#


