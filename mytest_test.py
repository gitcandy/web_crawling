import csv
import  numpy as np
import pandas as pd
# csv_file = csv.reader(open('E:\\test.csv'))
point_info = pd.read_csv("E:\\test.csv", encoding = "utf-8", header=0)
train = np.array(point_info)
x_test = train[:,1:5]
y_test= train[:,1:5]

ar = np.array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],

       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],

       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],

       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],

       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],

       [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],

       [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],

       [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],

       [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],

       [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])
y_predict =[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
a = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
csv_data = pd.DataFrame({'a_name':ar[:,0],'b_name':y_predict})
cc = pd.DataFrame(csv_data)
csv_data.to_csv('E:\my_csv.csv',index=0)

# with open('E:\test_prediction.csv', 'wb') as csvfile:
#     header = ["ID", "TARGET"]
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
