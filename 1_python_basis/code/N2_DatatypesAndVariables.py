# N2_DatatypesAndVariables.py
# 数据类型和变量

## 数据类型
### 转义字符
print('I\'m \"OK\"!')  # \'表示的是',\"表示的是"
print('I\'m OK.')
print('I\'m learning \nPython.') # \n表示换行
print('\\\n\\')	 # \\表示的字符是\
print('\\\t\\')	 # \t表示制表符
print(r'\\\t\\') # 用r''表示''内部的字符串默认不转义


### 用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

print('''I\'m OK!
I\'m learning Python!''')

print(r'''I'm OK!
I'm learning Python!''')


### 布尔型:True,False
print(5>3)	# True:真
print(10>135)	# False:假
print(5>3 or 10>135)	# or:或,条件中有一个为真即全为真True;条件全为假时即为假False
print(5>3 and 10>135)	# and:并,条件中有一个为假即全为假False;条件全为真时即为真True


### 空值:None


### 变量
a = 1 	### 动态语言
print(a)
a='ABC'
print(a)

t_007 = 'T007'
print('t_007 =',t_007)

Answer = True
print(Answer)


### 赋值
a='ABC'	  ### Python解释器干了两件事情:
		### 1.在内存中创建了一个'ABC'的字符串;
		### 2.在内存中创建了一个名为a的变量,并把它指向'ABC'
b=a	 ### 这个操作实际上是把变量b指向变量a所指向的数据			
a='XYZ'	 ### 变量a指向的值改变,对变量b没有影响
print(a,b)


### 常量:不能变的变量

#### 在Python中，通常用全部大写的变量名表示常量
#### 事实上PI仍然是一个变量,Python根本没有任何机制保证PI不会被改变
#### 所以,用全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359


### 除法

#### 1.除法/:计算结果是浮点数,即使是两个整数恰好整除,结果也是浮点数
print(9/3)
print(10/3)

#### 2.除法//:称为地板除,两个整数的除法仍然是整数
print(10//3)

### 取余数:%
print(10%3)



