#数据聚合与分组运算

#主要函数如下
#分组：groupby
#与groupby一起使用的:agg,aggregate,可以将函数在数据集中广播
#交叉表：pd.crosstab(data.s1,data.s2)
#透视表：data.pivot_table(rows=['s1','s2'])
#使用groupby
import  numpy as np
import pandas as pd
from pandas import  Series,DataFrame
df=DataFrame({
    'key1':['a','a','b','b','a'],
    'key2':['one','two','one','two','one'],
    'data1':np.random.rand(5),
    'data2':np.random.randn(5)

})
#按照key1给出的分类grouped是一个groupby对象，实际上还没有继进行任何运算
grouped=df['data1'].groupby(df['key1'])
print(grouped.mean())

means=df['data1'].groupby([df['key1'],df['key2']]).mean()
print(means)
#转换为具有层次化的索引
means.unstack()

#实际上，分组键可以是任何长度适当的数组
states=np.array(['Ohio','California','California','Ohio','Ohio'])
years=np.array([2005,2005,2006,2005,2006])
print(df['data1'].groupby([states,years]).mean())

#对分组进行迭代
for name,group in df.groupby('key1'):
    print(name)
    print(group)
# 对于多重键的情况，元组的第一个元素将会是由键值组成的元组
for(k1,k2), group in df.groupby(['key1','key2']):
    print(k1,k2)
    print(group)

prices=dict(list(df.groupby(('key1'))))
print(prices['b'])

#根据类型进行分组
grouped=df.groupby(df.dtypes,axis=1)
print(dict(list(grouped)))

# 通过字典或Series进行分组
#将字典传给groupby就可以进行分组
people=DataFrame(np.random.randn(5,5),
                 columns=['a','b','c','d','e'],
                 index=['Joe','Steve','Wes','Jim','Travis'])
# people._ix[2:3,['b','c']]=np.nan
mapping={'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}
by_column=people.groupby(mapping,axis=1)
print(by_column.sum())
#Series也可以进行分组，但是pandas会检车series以确保其索引跟分组轴是对齐的：
map_series=Series(mapping)
print(people.groupby(map_series,axis=1).count())

#根据索引级别分组
columns=pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],[1,3,5,1,3]],names=['cty','tenor'])
hier_df=DataFrame(np.random.randn(4,5),columns=columns)
#根据level关键字传入级别编号或者名称即可
hier_df.groupby(level='cty',axis=1).count()



#数据聚合
# quantile可以计算series或dataframe列的样本分位数，但它是一个Series方法，它首先会丢SEreies切片，然后对隔片调用piece。quantile（0.9），最后将这些组装成结果
grouped=df.groupby('key1')
print(grouped['data1'].quantile(0.9))
#使用自己的聚合函数，只需要将其传入aggregate或agg方法即可
def peak_to_peak(arr):
    return arr.max()-arr.min()

print(grouped.agg(peak_to_peak))

#分组级运算和转换:主要使用transform和apply方法
k1_means=df.groupby('key1').mean().add_prefix('mean_')
pd.merge(df,k1_means,left_on='key1',right_index=True)
#tansform会将一个函数应用到各个分组，然后将结果放置到适当的位置上，如果各分组产生的是一个标量值，则该值就会被广播出去
key=['one','two','one','two','one']
print(people.groupby(key).mean())
people.groupby(key).transform(np.mean)

def demean(arr):
    return  arr-arr.mean()
demeaned=people.groupby(key).transform(demean)
print(demeaned.groupby(key).mean())

#apply会将待处理的对象拆分成多个片段，然后对各个片段调用传入的函数，最后尝试将各片段组合到一起
#禁止层次化索引，可以使用参数group_keys=False传入groupby函数内禁止该效果
def top(df,n=5,column='tip_pct'):
    return df.sort_index(by_column)[-n:]
print(top(df,n=6))
# 上式的编码可以用以下的代码代替
df.groupby('smoker').apply(top)

#分位数和桶分析
fram=DataFrame({'data1':np.random.randn(1000),
                'data2':np.random.randn(1000)
                })
factor=pd.cut(fram.data1,4)
#根据data1的四分位进行data2的分组
def get_stats(group):
    return {'min':group.min(),'max':group.max(),
            'count':group.count(),'mean':group.mean()
            }
grouped=fram.data2.groupby(factor)
print(grouped.apply(get_stats).unstack())





# 透视表和交叉表
#透视表是各种电子表格程序和其他数据分析软件中一种常见的数据汇总工具，它根据一个或多个键对数据进行聚合，
# 并根据行和列上的分组键将数据分配到各个矩形区域中
#使用pivot_table可以获得透视表,不过在运行的时候，总是会提醒rows参数不存在，出现问题》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》
tips=pd.read_csv('ch08/tips1.csv')
tips.pivot_table(rows=['sex','smoker'])
# tips=DataFrame(np.random.randn(100,5),columns=['tip_pct','size','sex','day','smoker'])
tips.pivot_table(['tip_pic','size'],rows=['sex','day'],cols='smoker')

#交叉表crosstab
#交叉表是一种用于计算分组频率的特殊透视表
pd.crosstab(df.data1,df.data2,margins=True)