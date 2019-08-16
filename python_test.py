# str = "hello world"
# lens = len(str)
# # chars = []
# strs = ''
# print(len(strs))
# for i in range(0, lens):
#     strs = strs+str[lens-1-i]
#     print(lens-1-i)
# #
# # for i in range(0, lens-1):
# #     strs = strs+chars[lens-1-i]
# # strs.join(chars)
# # strs = strs+chars[0]
# # print(strs)
# # print(len(str),str[4],strs)
# print(strs)

#
# class Task:
#     def inversion(self, str):
#         # ********* Begin *********#
#         lens = len(str)
#         strs = ''
#         if lens == 0:
#             strs = ''
#         else:
#             lens = len(str)
#
#             strs = ''
#             for i in range(0, lens):
#                 strs = strs + str[lens - 1 - i]
#         print(strs)

# def getNum(n):
#     num = 0
#     rest=n
#
#     while rest>=1:
#         if rest%2==0:


#             rest = rest/2
#             print(rest,num)
#         else:
#             num=num+1
#             rest = rest-1
#             print(rest,num)
#     print(num)


# getNum(8)

import numpy as np
matrix =[[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
print(matrix[0][1])
def get_matrix(matrix):
    col = np.shape(matrix)[0]
    rol = np.shape(matrix)[1]
    print(col,rol)
    for i in range(0, col-1):
        for j in range(0, rol - 1):
            t = matrix[i][j]
            matrix[i][j] = matrix[col-j-1][rol-1-i]
            matrix[col-1-j][rol-1-i] = t
            print(matrix[i][j],matrix[col-1-j][i])
    print(matrix)
get_matrix(matrix)
