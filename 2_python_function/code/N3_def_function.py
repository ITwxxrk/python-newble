# N3_def_function.py
# 定义函数

## 定义一个函数要使用def语句,依次写出函数名、括号、括号中的参数和冒号:,
## 然后,在缩进块中编写函数体,函数的返回值用return语句返回。

### 例子:求绝对值的my_abs函数
# def my_abs(x):
# 	if x>0:
# 		return x
# 	else:
# 		return -x	
# print(my_abs(-99))


### 函数体内部的语句在执行时,一旦执行到return时,函数就执行完毕,并将结果返回。
### 因此,函数内部通过条件判断和循环可以实现非常复杂的逻辑。
### 如果没有return语句,函数执行完毕后也会返回结果,只是结果为None。
### return None可以简写为return。


## 空函数
### 可以用pass语句
def nop():
	pass
### pass还可以用在其他语句里
age = 10
if age >=18:
	pass 	# 缺少了pass,代码运行就会有语法错误


### 调用函数时，
### 如果参数个数不对,Python解释器会自动检查出来,并抛出TypeError
### 如果参数类型不对,Python解释器就无法帮我们检查
### 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
	if not isinstance(x,(int,float)):	
			#对参数类型做检查,只允许整数和浮点数类型的参数

		raise TypeError('bad operand type')
			#添加了参数检查后,如果传入错误的参数类型,函数就可以抛出一个错误
	
	if x>0:
		return x
	else:
		return -x

# print(my_abs('A'))
print(my_abs(12))


## 返回多个值
### 例子:在游戏中经常需要从一个点移动到另一个点,
### 给出坐标、位移和角度,就可以计算出新的坐标

import math		# math包,并允许后续代码引用math包里的sin、cos等函数

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi/6)
print(x,y)

#### 其实这只是一种假象,Python函数返回的仍然是单一值
r = move(100, 100, 60, math.pi / 6)
print(r)
##### 原来返回值是一个tuple！
##### 但是,在语法上,返回一个tuple可以省略括号,而多个变量可以同时接收一个tuple,按位置赋给对应的值,
##### 所以,Python的函数返回多值其实就是返回一个tuple,但写起来更方便。


# 小结
# 定义函数时,需要确定函数名和参数个数；
# 如果有必要,可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时,自动return None。
# 函数可以同时返回多个值,但其实就是一个tuple


## practice:
### 请定义一个函数quadratic(a, b, c),
### 接收3个参数,返回一元二次方程 a*x^2+b*x+c=0的两个解。
### 提示：
### 一元二次方程的求根公式为：
### x=（-b(+/-)sqrt(b^2-4*a*c)）/(2*a)
### 计算平方根可以调用math.sqrt()函数
import math
def quadratic(a,b,c):
	if not isinstance(a,(int,float))&isinstance(b,(int,float))&isinstance(c,(int,float)):	
		raise TypeError('bad operand type')
	x1 = (-b + math.sqrt(b * b - 4 * a *c)) / (2 *a)
	x2 = (-b - math.sqrt(b * b - 4 * a *c)) / (2 *a)
	return x1,x2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
