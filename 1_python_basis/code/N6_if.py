# 条件判断

# 例子:输入用户年龄,根据年龄打印不同的内容,在Python程序中,用if语句实现
### 如果if语句判断是True,就把缩进的两行print语句执行了,
### 否则,什么也不做
age = 20
if age >= 18 :
	print('your age is',age)
	print('adult')
### 给if添加一个else语句,
### 如果if判断是False,不要执行if的内容,执行else
age = 13
if age >= 18 :
	print('your age is',age)
	print('adult')
else :
	print('your age is',age)
	print('teenager')
### 可以用elif做更细致的判断
### elif是else if的缩写,完全可以有多个elif
age = 3
if age >= 18 :
	print('your age is',age)
	print('adult')
elif age >= 6 :
	print('your age is',age)
	print('teenager')
else :
	print('your age is',age)
	print('kid')
### if语句执行时是从上往下判断,
### 如果在某个判断上是True,把该判断对应的语句执行后,就忽略掉剩下的elif和else
age = 20
if age >= 6 :
	print('your age is',age)
	print('teenager')
elif age >= 18 :
	print('your age is',age)
	print('adult')
else :
	print('your age is',age)
	print('kid')


### if判断条件还可以简写
### 只要条件是非零数值、非空字符串、非空list等,就判断为True,否则为False
if 4:	#True
    print('ABC')


### 用input()读取用户的输入,input()返回的数据类型是str
### 与数值比较时,str不能直接和整数比较,必须先用int()函数把str转换成整数
### int()函数发现一个字符串并不是合法的数字时就会报错,程序就退出了
birth = input('birth: ')
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')


### practice：
'''
小明身高1.75,体重80.5kg。
请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数,
并根据BMI指数:
	低于18.5:过轻
	18.5-25:正常
	25-28:过重
	28-32:肥胖
	高于32:严重肥胖
用if-elif判断并打印结果
'''
height = 1.75
weight = 80.5
BMI = 80.5/pow(1.75,2)
print('BMI = %.2f' % BMI)
#print(BMI)
if BMI < 18.5 :
	print('过轻')
elif BMI < 25 :
	print('正常')
elif BMI < 28 :
	print('过重')
elif BMI <32 :
	print('肥胖')
else :
	print('严重肥胖')

