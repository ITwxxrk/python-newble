# pre_function.py
# function:函数

## 计算圆的面积：
## S=pi*r*r
r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 *r1
s2 = 3.14 * r2 *r2
s3 = 3.14 * r3 *r3
print('s1=%f\ns2=%f\ns3=%f\n' %(s1,s2,s3))


### 当代码出现有规律的重复的时候，你就需要当心了，每次写3.14 * x * x,
### 不仅很麻烦，而且，如果要把3.14改成3.14159265359的时候，得全部替换。
### 有了函数，我们就不再每次写s = 3.14 * x * x，
### 而是写成更有意义的函数调用s = area_of_circle(x)，
### 而函数area_of_circle本身只需要写一次，就可以多次调用。

PI=3.14
def area_f_cricle(x):
	s = PI * x * x
	return s


s1 = area_f_cricle(r1)		# 函数调用
s2 = area_f_cricle(r2)
s3 = area_f_cricle(r3)
print('s1=%f\ns2=%f\ns3=%f\n' %(s1,s2,s3))

