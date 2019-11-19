# call_function.py
# 函数


# Python内置了很多有用的函数,我们可以直接调用
# 要调用一个函数,需要知道函数的名称和参数。
# 可以直接从Python的官方网站查看文档。
# 也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。

### abs():绝对值函数,有且仅有一个参数
a = abs(100)
b = abs(-20)
c = abs(-12.34)
print(a,b,c)

### 调用函数的时候,如果传入的参数数量不对,会报TypeError的错误
### 如果传入的参数数量是对的,但参数类型不能被函数所接受,也会报TypeError的错误,
### 并且给出错误信息:str是错误的参数类型




### max():可以接收任意多个参数，并返回最大的那个
m1 = max(1,2)
m2 = max(2,-3,1,5)
print(m1,m2)


## 数据类型转换

### int():可以把其他数据类型转换为整数
print(int('123'))
print(int(12.34))

### float():可以把其他数据类型转换为浮点型
print(float('12.13'))

### str():可以把其他数据类型转换为字符串
print(str(1.23))
print(str(100))

### bool():可以把其他数据类型转换为布尔型
print(bool(1))
print(bool(''))





##### 函数名其实就是指向一个函数对象的引用，
##### 完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名
a = abs
print(a(-1))




### practice:
### 利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
### n1 = 255
### n2 = 1000
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
