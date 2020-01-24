# N1_do_slice.py
# 切片



## 取一个list或tuple的部分元素
L = ['Michael','Sarah','Tracy','Bob','Jack']
print(L[0],L[1],L[2])	#取前3个元素



## 取前N个元素,也就是索引为0-(N-1)的元素,
## 可以用循环
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)



### 切片(Slice)操作符
print(L[0:3]) #取前3个元素,从索引0开始取,直到索引3为止,但不包括索引3
print(L[2:4])



### 如果第一个索引是0,还可以省略
print(L[:2])



## python 支持倒数切片
### 倒数第一个元素的索引是-1
print(L[-2:])
print(L[-2:-1])

L1 = list(range(100))
print(L1)
print(L1[:10]) #取前10个元素
print(L1[-10:]) #取后10个元素
print(L1[10:20]) #取前11-20个数
print(L1[:10:2]) #前10个数,每两个取一个
print(L1[::5]) #所有数,每5个取一个
print(L1[:]) #复制一个list

## tuple元素不可变,也可以用切片操作
T = (0,1,2,3,4,5,6)
print(T[:3])

## 字符串,也可以切片操作
abs = 'ABCDEFGH'
print(abs[4:6])
print(abs[::3])
### Python没有针对字符串的截取函数,只需要切片一个操作就可以完成

### practice:
### 利用切片操作,实现一个trim()函数,去除字符串首尾的空格,
### 注意不要调用str的strip()方法
def trim(s):
	if len(s)==0:
		return ''
	while s[0]==' ':
		s = s[1:]
		if len(s)==0:
			return ''

	while s[-1]==' ':
		s = s[:-1]
		if len(s)==0:
			return ''
	return s

print(trim('hello  '))
print(trim('  hello'))
print(trim('  hello  '))
print(trim('  hello  world  '))
print(trim(''))
print(trim('    '))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

### 小结
### 有了切片操作,很多地方循环就不再需要了。
### Python的切片非常灵活,一行代码就可以实现很多行循环才能完成的操作。
