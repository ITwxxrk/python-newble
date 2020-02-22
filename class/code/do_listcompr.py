# N3_do_listcompr.py
# 列表生成式：List Comprehensions

### 列表生成式可以用一行语句代替循环生成上面的list
### 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
L1 = [x * x for x in range(1,11)]
print(L1)

### for循环后面还可以加上if判断
L2 = [x * x for x in range(1,11) if x % 2 == 0]
print(L2)

### 还可以使用两层循环，可以生成全排列
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)

### 三层和三层以上的循环就很少用到了

### 例子：列出当前目录下的所有文件和目录名
import os 
L4 = [d for d in os.listdir('.')]	## os.listdir可以列出文件和目录
print(L4)