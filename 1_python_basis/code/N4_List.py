# list,列表,可变的有序表


## 列表的定义,用中括号[]
classmates = ['Michael','Bob','Tracy']
print(classmates)

## len():获得list元素的个数
lc = len(classmates)
print('len =',lc)

## 用索引访问list中的每一个位置的元素
### 索引是从0开始的,最后一个元素的索引是len(classmates)-1
### 当索引超出了范围时,Python会报一个IndexError错误
print(classmates[0])
print(classmates[1])
print(classmates[2])

### 如果要取最后一个元素,还可以用-1做索引,直接获取最后一个元素
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

## append():追加元素到末尾
classmates.append('Adam')
print(classmates)


## insert():把元素插入到指定的位置
classmates.insert(1,'Jack')
print(classmates)


## pop():删除末尾元素
classmates.pop()
print(classmates)

## pop(i):删除指定位置的元素
classmates.pop(2)
print(classmates) 

## 替换list中任意位置的元素,直接赋值即可
classmates[0]='Sarah'
print(classmates)


### list里面的元素的数据类型可不同
L1 = ['Apple',123,True,None]
print(L1)

### list里面的元素的数据类型可以是list
L2 = ['Apple',123,['Orange',12,True],'A']
print(L2)
print(L2[2])
print(L2[3])

p = ['asp','php']
s = ['python','java',p,'scheme']
print(s)
print('len(s) =',len(s))
print(s[2][0])	#取p[0]的值，即'asp'

### list可以为空
L = []
print('len(L) =',len(L))





