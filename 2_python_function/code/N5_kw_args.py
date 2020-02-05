# N5_kw_args.py
## 关键字参数

# 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict(字典)
def person(name,age,**kw):	# kw:关键字参数
	print('name:',name,'age:',age,'other:',kw)

	
# 在调用该函数时，可以只传入必选参数
print(person('Michael',30))
# 也可以传入任意个数的关键字参数
print(person('BOb',35,city = 'Beijing'))
print(person('Adam',45,gender = 'M',job = 'Engineer'))


# 关键字参数可以扩展函数的功能：

# 比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，
# 利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，
# 然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))

# 上面复杂的调用可以用简化的写法：
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, **extra))


# extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。


### 命名关键字参数
### 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
### 至于到底传入了哪些，就需要在函数内部通过kw检查


#### 以person()函数为例，检查是否有city和job参数：
def person(name,age,**kw):
	if 'city' in kw:
		# 有city参数
		pass
	if 'job' in kw:
		# 有job参数
		pass
	print('name:',name,'age:',age,'other:',kw)
### 调用者仍可以传入不受限制的关键字参数
print(person('Jack',24,city = 'Beijing',adder = 'Chaoyang',zipcode = 123456))


### 如果要限制关键字参数的名字，就可以用命名关键字参数，
### 例如，只接收city和job作为关键字参数。
### 这种方式定义的函数如下：
def person(name,age,*,city,job): # 命名关键字参数需要一个特殊分隔符*
				 # *后面的参数被视为命名关键字参数
	print(name,age,city,job)
print(person('Jack',24,city = 'Beijing',job = 'Engineer'))


### 如果函数定义中已经有了一个可变参数
### 后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
### def person(name,age,*args,city,job):
###		print(name,age,args,city,job)
### print(person('Jack',24,'Beijing','Engineer')) #报错
### 命名关键字参数必须传入参数名,如果没有传入参数名，调用将报错.
### 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。

### 命名关键字参数可以有缺省值，从而简化调用
def person(name,age,*,city='Beijing',job):
	print(name,age,city,job)
### 由于命名关键字参数city具有默认值，调用时，可不传入city参数
print(person('Jack',24,job='Engineer'))

#### 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
#### 如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person(name,age,city,job):
	# 缺少 *，city和job被视为位置参数
	pass


## 参数组合
### 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
### 这5种参数都可以组合使用
### 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

print(f1(1,2))
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99,ext=None))


### 通过一个tuple和dict，你也可以调用上述函数:
args = (1,2,3,4)
kw = {'d':99,'x':'#'}
print(f1(*args,**kw))

args = (1,2,3)
kw = {'d':88,'x':'#'}
print(f2(*args,**kw))

##### 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
##### 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。


## practice:
### 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
### def product(x,y):
### 	return x * y
def product(x=0, y=0,*args):
     return x * y
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


### 小结
### Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
### 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

### 要注意定义可变参数和关键字参数的语法：
### *args是可变参数，args接收的是一个tuple；
### **kw是关键字参数，kw接收的是一个dict。

### 调用函数时如何传入可变参数和关键字参数的语法：
### 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
### 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

### 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
### 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
### 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
