
# 字符编码

## 在最新的Python3版本中,字符串是以Unicode编码的
## 也就是说,Python的字符串支持多语言
print('这是一个python程序')


### ord():获取字符的整数表示
### chr():把编码转化为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(98))
print(chr(25991))


### 如果知道字符的整数编码,还可以用十六进制这么写str
print('\u4e2d\u6587')



### Python的字符串类型是str,在内存中以Unicode表示,一个字符对应若干个字节
### 如果要在网络上传输,或者保存到磁盘上,需要把str变为以字节为单位的bytes
### Python对bytes类型的数据用带b前缀的单引号或双引号表示

### 区分'ABC'和b'ABC',前者是str,
### 后者虽然内容显示得和前者一样,但bytes的每个字符都只占用一个字节
x = 'ABC'	# str
y = b'ABC'	#bytes


### str通过encode()方法可以编码为指定的bytes
### 纯英文的str可以用ASCII编码为bytes
### 含有中文的str可以用UTF-8编码为bytes
###（含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错）
print(x.encode('ascii'))
print('中文'.encode('utf-8'))


### 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes
### 把bytes变为str，就需要用decode()方法
print(y.decode('ascii'))
#print(b'\xe4\xb8\xad\xe6\x96\x87',decode(utf-8))
#如果bytes中包含无法解码的字节，decode()方法会报错,如上一个语句
#如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8',errors='ignore'))


##len():计算字符串str包含几个字符
print(len('ABC'))
print(len('中文'))

#如果换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

#1个中文字符经过UTF-8编码后通常会占用3个字节
#而1个英文字符只占用1个字节

#   格式化
###	%：	用来格式化字符串
###	%str：字符串
###	%d：整数
###	%f：浮点数
###	%x：十六进制整数
print('Hello,%s' % 'world')
print('Hi,%s,you have S%d.' % ('Michael',1000000))
print('%2d - %02d' % (3,1))
print('%.2f' % 3.1415926)
### 如果你不太确定应该用什么,%s永远起作用,它会把任何数据类型转换为字符串
print('Age:%s. Gender:%s' % (25,True))
print('growth rate : %d %%' % 7)	# 用%%来表示一个%


### 另一种格式化方法：format()
### 它会用传入的参数依次替换字符串内的占位符{0}、{1}……
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明',17.125))


#practice
##小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，
##并用字符串格式化显示出'xx.x%'，只保留小数点后1位
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明成绩提升了%.1f%%.' % r)
