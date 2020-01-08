# tuple:元祖,有序集合,但一旦初始化就不能修改


## tuple的定义:用小括号()
## 当定义一个tuple时,在定义的时候,tuple的元素就必须被确定下来
classmates = ('Michael','Bob','Tracy')

##	获取元素的方法:同list相同
### 用索引访问tuple中的每一个位置的元素
### 索引是从0开始的,最后一个元素的索引是len(classmates)-1
### 当索引超出了范围时,Python会报一个IndexError错误
print(classmates[1])
print(classmates[-1])


## 如果要定义一个空的tuple,可以写成()
t = ()
print(t)


### 要定义一个只有1个元素的tuple,定义时必须加一个逗号,，来消除歧义
###	因为t = (1)定义的不是tuple,是1这个数！
### 这是因为括号()既可以表示tuple,又可以表示数学公式中的小括号,这就产生了歧义
t = (1)
print(t)	# 1
t = (1,)
print(t)	# (1,)


## “可变的”tuple
t = ('a','b',['A','B'],'c')
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'		
print(t)	
# 表面上看,tuple的元素确实变了,但其实变的不是tuple的元素,而是list的元素
# “指向不变”


### practice:
L = [
	['Apple','Google','Microsoft'],
	['Java','Python','Ruby','PHP'],
	['Adam','Bart','Lisa']
]

###	打印Apple:
### 打印Python:
### 打印Lisa:

print(L[0][0])
print(L[1][1])
print(L[2][2])



