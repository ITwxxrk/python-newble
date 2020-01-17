# N4_var_args.py
# 函数的参数

### 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。
### 对于函数的调用者来说，只需要知道如何传递正确的参数，以及函数将返回什么样的值就够了，
### 函数内部的复杂逻辑被封装起来，调用者无需了解。

## 位置参数

### 用来计算x的二次方
def power1(x):	# x:位置参数
	return  x + x

print(power1(5))
print(power1(15))


### 用来计算x的n次方
def power2(x,n):
	s = 1
	while n > 0 :
		n = n - 1
		s = s * x
	return s

print(power2(5,2))
print(power2(5,3))



## 默认参数
def power3(x,n=2):	# n=2,默认参数
	s = 1
	while n > 0 :
		n = n - 1
		s = s * x
	return s

print(power3(5))
print(power3(5,2))
print(power3(5,4)) # 对于n>2的其他情况,就必须明确地传入n

# 默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 二是如何设置默认参数
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
# 变化小的参数就可以作为默认参数。
# 最大的好处是能降低调用函数的难度



### 例子：写个一年级小学生注册的函数，需要传入name和gender两个参数。
### 如果要继续传入年龄、城市等信息怎么办？这样会使得调用函数的复杂度大大增加
### 可以把年龄和城市设为默认参数
def enroll(name,gender,age = 6,city = 'Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city',city)

print(enroll('Sarah','F'))
print(enroll('Bob','M',7))
	# 除了name，gender这两个参数外，最后1个参数应用在参数age上，
	# city参数由于没有提供，仍然使用默认值。
print(enroll('Adam','M',city = 'Tianjing'))
	# city参数用传进去的值，其他默认参数继续使用默认值


## 默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
### 例子：先定义一个函数，传入一个list，添加一个END再返回
def add_end(L=[]):
	L.append('END')
	return L

print(add_end([1,2,3]))
print(add_end(['x','y','z']))
print(add_end())
print(add_end())
print(add_end())

### 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
### 原因解释如下：
### Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
### 因为默认参数L也是一个变量，它指向对象[]，
### 每次调用该函数，如果改变了L的内容，
### 则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

### 定义默认参数要牢记一点：默认参数必须指向不变对象！

## 修改：用None这个不变对象来实现
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end())
print(add_end())
print(add_end())


### 为什么要设计str、None这样的不变对象呢？
### 因为不变对象一旦创建，对象内部的数据就不能修改，
### 这样就减少了由于修改数据导致的错误。
### 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
### 同时读一点问题都没有。
### 我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。




## 可变参数

### 可变参数就是传入的参数个数是可变的，
### 可以是1个、2个到任意个，还可以是0个。


### 例子：给定一组数字a，b，c……，计算a^2 + b^2 + c^2 + ……
### 要定义出这个函数，我们必须确定输入的参数。
### 由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，
### 这样，函数可以定义如下：
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

# 调用的时候，需要先组装出一个list或tuple
print(calc([1,2,3]))
print(calc((1,3,5,7)))


# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
# 如果利用可变参数，调用函数的方式可以简化成这样:
def calc1( *numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print(calc1(1,2,3))
print(calc1(1,3,5,7))

# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 调用该函数时，可以传入任意个参数，包括0个参数
print(calc1(1,2))
print(calc1())

# 如果已经有一个list或者tuple，要调用一个可变参数,可以这样做：
nums = [1,2,3]
print(calc1(nums[0],nums[1],nums[2]))
# 这种写法当然是可行的，问题是太繁琐，
# 所以Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去

nums = [1,2,3]
print(calc1(*nums))
# *nums表示把nums这个list的所有元素作为可变参数传进去
