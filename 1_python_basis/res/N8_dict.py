# dict:字典,全称dictionary
## 使用键-值（key-value）存储,具有极快的查找速度



### 假设要根据同学的名字查找对应的成绩,如果用list实现,需要两个list。
### names = ['Michael', 'Bob', 'Tracy']
### scores = [95, 75, 85]
### 给定一个名字,要查找对应的成绩,就先要在names中找到对应的位置,再从scores取出对应的成绩
### list越长,耗时越长。

### 如果用dict实现,只需要一个“名字”-“成绩”的对照表
### 直接根据名字查找成绩,无论这个表有多大,查找速度都不会变慢。

### 用Python写一个dict如下：
d = {'Michael':95,'Bob':75,'Tracy':85}
print(d['Michael'])




### dict的实现原理和查字典是一样的。
### 先在字典的索引表里（比如部首表）查这个字对应的页码,然后直接翻到该页,找到这个字。
### 无论找哪个字,这种查找速度都非常快,不会随着字典大小的增加而变慢。

### 这种key-value存储方式,在放进去的时候,必须根据key算出value的存放位置,
### 这样,取的时候才能根据key直接拿到value。





## 把数据放入dict的方法,除了初始化时指定外,还可以通过key放入。
d['Adam'] = 67
print(d)
print(d['Adam'])



## 由于一个key只能对应一个value
## 所以,多次对一个key放入value,后面的值会把前面的值冲掉
d['Jack'] = 90
print(d)
print(d['Jack'])

d['Jack'] = 88
print(d)
print(d['Jack'])




## 如果key不存在,dict就会报错
## 要避免key不存在的错误,有两种办法:

### 一是通过in判断key是否存在
#'Thomas' in d   #可执行,不输出结果
print('Thomas' in d)

### 二是通过dict提供的get()方法,如果key不存在,可以返回None,或者自己指定的value
#d.get('Thomas')	#可执行,不输出结果
print(d.get('Thomas'))		# 返回None
							# 注意:返回None的时候Python的交互环境不显示结果
#d.get('Thomas',-1)
print(d.get('Thomas',-1))	# 返回-1





## 删除一个key,用pop(key)方法,对应的value也会从dict中删除
#d.pop('Bob')
print(d.pop('Bob'))
print(d)




## dict内部存放的顺序和key放入的顺序是没有关系的








# 和list比较,dict有以下几个特点：
### 查找和插入的速度极快,不会随着key的增加而变慢；
### 需要占用大量的内存,内存浪费多。

# 而list相反：
### 查找和插入的时间随着元素的增加而增加；
### 占用空间小,浪费内存很少。

# 所以,dict是用空间来换取时间的一种方法。


# dict可以用在需要高速查找的很多地方,在Python代码中几乎无处不在


# dict的key必须是不可变对象
# 这是因为dict根据key来计算value的存储位置,
# 如果每次计算相同的key得出的结果不同,那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）
# 要保证hash的正确性,作为key的对象就不能变。
# 在Python中,字符串、整数等都是不可变的,因此,可以放心地作为key。
# 而list是可变的,就不能作为key。

key = [1,2,3]
print(key)
# d[key] = 'a list'会报错

