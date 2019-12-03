## 循环


### Python的循环有两种
### 一种是for...in循环,依次把list或tuple中的每个元素迭代出来
###	第二种循环是while循环,只要条件满足,就不断循环,条件不满足时退出循环


## for...in循环
names = ['Michael','Bob','Tracy']
for name in names :		# 依次打印names的每一个元素
	print(name)


### 计算1-10的整数之和,用sum变量做累加
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum +x
print(sum)

### range()函数,可以生成一个整数序列,再通过list()函数可以转换为list
print(list(range(5)))


### 计算1-100的整数之和
sum = 0
for i in range(101):
	sum = sum +i
print(sum)




## while 循环

### 计算100以内所有奇数之和
sum = 0
n = 99
while n>0:
	sum = sum + n
	n = n - 2	# n不断自减,直到变为-1时,不再满足while条件,循环退出
print(sum)


### practice:
### 利用循环依次对list中的每个名字打印出Hello, xxx!
### L = ['Bart', 'Lisa', 'Adam']
L = ['Bart','Lisa','Adam']
for name in L:
	print('Hello,' + name + '!')





##  break 和 continue
### 这两个语句通常都必须配合if语句使用
### 不要滥用break和continue语句。
### break和continue会造成代码执行逻辑分叉过多,容易出错。


### break:结束当前循环
n = 1
while n<=100:
	if n>10:	##打印出1~10后,紧接着打印END,程序结束
		break;
	print(n)
	n=n+1
print('END')


### continue:跳过当前的这次循环,直接开始下一次循环
n = 0
while n<10:
	n = n + 1
	if n % 2 == 0:	##如果是偶数,跳出当前循环,进入下一层循环。打印奇数
		continue
	print(n)


##### 如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。
##### 这时可以用Ctrl+C退出程序，或者强制结束Python进程
