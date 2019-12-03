# N1_InputAndPrint.py
# 输入输出

## 输出函数:print()

### 用print()在括号中加上字符串,就可以向屏幕上输出指定的文字

print('hello,world')

### print()函数也可以接受多个字符串,用逗号“,”隔开,就可以连成一串输出
### print()会依次打印每个字符串,遇到逗号“,”会输出一个空格

print('The quick brown fox','jumps over','the lazy dog')

### print()也可以打印整数,或者计算结果
print(300)
print(100 + 300)
print('100 + 300 =' , 100 + 300)



## 输入函数:input()


### 交互式
### 让用户输入字符串,并存放到一个变量里让用户输入字符串,并存放到一个变量里
name = input('please enter your name:') # 输入用户的名字
print(name)
print('hello' , name)
