#ndarray是一个N维数组对象，是一个通用的同构数据多维容器
#创建数组最简单的办法就是使用array函数
import  numpy as np


data1=[6,7.5,8,0,1]
#1.数组的创建：将接受的序列数组转换为一个多位Numpy数组
arr1=np.array(data1)
# print(arr1)
# print(arr1.dtype)
#新建数组的方法还有zeros,ones,arrange，asarray,ones_like,zeros_like,empty,eye,empty_like,identity等
arr2=np.zeros((3,6))
arr3=np.empty((2,3,2))
arr4=np.ones((2,3))
# print(arr2,arr3,arr4)
#2.数组的转换：array类型可以转换，有两种方法，一种是创建的时候利用dtype属性进行创建，一种是通过astype的方法进行创建
arr5=np.array([1,2,3],dtype=np.int32)
# print(arr5.dtype)
float_arr=arr5.astype(np.float64)
# print(float_arr.dtype)
#3.数组的索引和切片：数组的切片和列表不同，数组切片是原始数组的视图，这意味着数组不会被复制，视图上的任何修改都会被直接反映到原数组上
arr6=np.arange(10)
# print(arr6)
arr_slice=arr6[5:8]
arr_slice[1]=12345
# print(arr6)
#进行复制需要使用copy()函数
arr_slice1=arr6[5:8].copy()
arr_slice1[1]=123456
# print(arr6)
#4.布尔型索引：布尔型数组的长度必须跟被索引的轴长度一致，此外还可以将布尔型数组跟切片、整数混合使用
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data=np.random.rand(7,4)
# print(data[names=='Bob'])
# print(data[names=='Bob',2:])
#5.花式索引：利用整数素组进行索引
arr=np.empty((8,4))
for i in range(8):
    arr[i]=i
# print(arr[[4,3,0,6]])
# print(arr[[1,5,7,2],[0,3,1,2]])
#np.ix_()可以将两个一维整数数组转换为一个用于选取方形区域的索引器
# print(arr[np.ix_([1,5,7,2],[0,3,1,2])])
#6.数组转置和轴对换
#转置是重塑的一种特殊形式，他返回的是源数据视图，不会进行复制操作,T属性可以进行转置
arr=np.arange(15).reshape((3,5))
# print(arr,arr.T)
arr8=np.arange(16).reshape((2,2,4))
print(arr8.transpose((1,0,2)))
#利用np.dot来计算矩阵的内积,矩阵与矩阵转置的乘积
print(np.dot(arr.T,arr))
#swapaxex()，需要给轴编号进行转置
#6.数组的文件输入和输出
#np.save 和 np.load是读写磁盘数组数据的两个主要函数
arr=np.arange(10)
np.save('some_array',arr)
print(np.load('some_array.npy'))