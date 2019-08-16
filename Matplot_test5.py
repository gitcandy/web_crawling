#绘图和可视化
#s虽然pandas有许多处理普通的绘图任务，但如果自定义一些高级功能的话，就必须学习matplotlib APT

import  matplotlib.pyplot as plt
import matplotlib.figure
from  numpy.random import  randn
from datetime import  datetime
import pandas as pd
from  pandas import Series,DataFrame
import  numpy as np
from  mpl_toolkits.basemap import Basemap
#1 figure和subplot
fig=plt.figure()
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
#绘制折线图，使用k--线型
plt.plot(randn(50).cumsum(),'k--')
#绘制直方图
_=ax1.hist(randn(100),bins=20,color='k',alpha=0.3)
#绘制散点图
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))
fig,axes=plt.subplots(2,3)


#调整subplot周围的间距
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)
#设置坐标轴的刻度是否是相同的。subplots的参数还有nrows,ncols,sharex,sharey,subplot_kw,**fig_kw
fig,axes=plt.subplots(2,2,sharex=True,sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(randn(500),bins=50,color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0)

#颜色、标记和线型
data=randn(30).cumsum()
plt.plot(data,'k--',label='Default')
plt.plot(data,'k-',drawstyle='steps-post',label='steps-post')
#添加注释框，图例
plt.legend(loc='best')

plt.plot(randn(30).cumsum(),'ko--')

#设置标题，轴标签，刻度以及刻度标签
fig=plt.figure();ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum())
ticks=ax.set_xticks([0,250,500,750,1000])
labels=ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')
ax.set_title('My first matplotlib plot')
ax.set_xlabel('Stages')

#添加图例
fig=plt.figure();ax=fig.add_subplot(1,1,1)
ax.plot(randn(1000).cumsum(),'k',label='one')
ax.plot(randn(1000).cumsum(),'k--',label='two')
ax.plot(randn(1000).cumsum(),'k.',label='three')
#loc告诉要将图例放在那里，beat会选择最不碍事的位置，要从图例中去除一个或多个原色，不传入label或传入label='_nolegend_'即可
ax.legend(loc='best')

#注解以及在subplot上绘图
#根据2007年以来的标准普尔500指数收盘价格绘制一张曲线图，并标出2008年到2009年金融危机期间的一些重要日期
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
data=pd.read_csv('ch08/spx.csv',index_col=0,parse_dates=True)
spx=data['SPX']
spx.plot(ax=ax, style='k-')
crisis_data=[
    (datetime(2017,10,11),'Peak of bull market'),
    (datetime(2018,3,12),'Bear Stearns Fails'),
    (datetime(2018,9,15),'Lehman Bankruptcy')
]

for date,laber in crisis_data:
    ax.annotate(laber,xy=(date,spx.asof(date)+50),
                xytext=(date,spx.asof(date)+20),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',verticalalignment='top' )
ax.set_xlim(['1/1/2017','1/1/2019'])
ax.set_ylim([600,800])
ax.set_title('Importance dates in 2008-2009 financial crisis')

#在图表中添加图像，需要创建一个块对象shp,然后通过ax.add_patch(shp)来将其添加到subplot中
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#创建块
rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)
circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)
pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)
rect1=plt.Rectangle((0.2,0.5),0.4,0.15,color='k',alpha=0.3)
#将创建块放进ax中
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
ax.add_patch(rect1)


#将图表保存到文件
#利用plt.savefig可以将当前图表保存到文件,一般在绘图完后再执行如下语句，即可保存到项目文件中
plt.savefig('figpath.png',dpi=40,bbox_inches='tight')
#matplotlib配置信息：配置文件为matplotlibrc,如果对文件自定义，则每次使用matplotlib时就会自动加载该文件



# pandas中的绘图函数
#线形图
#series的线形图
s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
#Dataframe的plot方法会在一个subplopt中为各列绘制一条线，并自动创建图例
df=DataFrame(np.random.randn(10,4).cumsum(0),
             columns=['A','B','C','D'],
             index=np.arange(1,100,10)
             )
df.plot()

#柱状图
fig,axes=plt.subplots(2,1)
data=Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar',ax=axes[0],color='k',alpha=0.7)
data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)

df=DataFrame(np.random.rand(6,4),index=['one','two','three','four','five','six'], columns=pd.Index(['A','B','C','D'],names='Genus'))
df.plot(kind='bar')
df.plot(kind='barh',stacked='True',alpha=0.5)

#直方图和密度图
tips=pd.read_csv('ch08/tips.csv')
party_counts=pd.crosstab(tips.day,tips.size)
party_counts=party_counts.ix[:,2:5]


comp1=np.random.normal(0,1,size=200)
comp2=np.random.normal(10,2,size=200)
values=Series(np.concatenate([comp1,comp2]))
values.hist(bins=100,alpha=0.3,color='k',normed=True)
#kind='pde'可直接生成密度图，但是这里出现了问题，问题是不存在scipy
values.plot(kind='kde',style='k--')
values.plot(style='k--')
#散布图
#主要使用两种方法：plt.scatter(data[1),data[2]),plt.scatter_matrix(dataform)

#绘制地图
data=pd.read_csv('ch08/Haiti1.csv')
data=data[(data.LATITUDE>18)&(data.LATITUDE<20)&(data.Longtitude>-75)&(data.Longitude<-70)&(data.CATEGORY.notnull())]
#编写函数，用来获取所有分类的列表，然后将各个分类信息拆分为编码和英语名称
def to_cat_list(catstr):
    stripped=(x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
def get_all_categories(cat_series):
    cat_sets=(set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def get_english(cat):
    code,names=cat.split('.')
    if '|' in names :
        names=names.split('|')[1]
        return code,names.strip()

#做一个编码跟名称映射起来的字典
all_cats=get_all_categories(data.CATEGORY)
english_mapping=dict(get_english(x) for x in all_cats)

#分类选取记录，添加指标（哑变量）列，每个分类一列，首先抽取出唯一的分类编码，并构造一个全零DataFrame,列为分类编码，索引跟data的索引一样
def get_code(seq):
    return [x.split('.')[0] for x in seq if x ]

all_codes=get_code(all_cats)
code_index=pd.Index(np.unique(all_codes))
dummy_frame=DataFrame(np.zeros((len(data),len(code_index))),index=data.index,columns=code_index)

for row, cat in zip(data.index,data.CATEGORY):
    codes=get_code(to_cat_list(cat))
    dummy_frame.ix[row,codes]=1
data=data.join(dummy_frame.add_prefix('category_'))

#开始绘图
def basic_haiti_map(ax=None,lllat=17.25,urlat=20.25,lllon=-75,urlon=-71):
    m=Basemap(ax=ax,projection='stere',lon_0=(urlon+lllon))