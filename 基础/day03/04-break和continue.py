"""
break:一旦循环中执行到break,本次循环的后续代码不会再执行,并且跳出循环(就是结束循环了).循环体彻底报废.经常配合while True 和 if使用

continue:一旦循环中执行到continue,本次循环的后续代码不会再执行(只是结束了本次循环),并且直接进行下一次循环判断(就是程序回到了while 后面的条件判断的地方).会一直在while后面的循环条件那里进行判断操作.经常会出现因逻辑错误导致的死循环.本质上是实现剔除符合某个条件的相应功能.例如以下的过7游戏示例.
"""

"""
设计“过7游戏”的程序, 打印出1-100之间除了含7和7的倍数之外的所有数字。

for i in range(1,101):
	if i % 7 != 0:
		print(i)
或者:
i = 0
while i < 100:
	i += 1
	if i % 7 == 0:  # 这么设计的目的是跳过i+1=7,但是打印输出的是i,这样设计就实现了将7和7的倍数剔除的效果
		continue
	else:
		print(i)   # 打印的是7之前的那个数字,或者7的整数倍-1的数字,成功避免7陷入死循环无法跳出来.逻辑上的
"""

"""
import random

i = 0
while i < 5:
	num = random.randint(1,3)
	if i == 2:
		break
	print('第%d次输出' % i)
	i += 1
print('完成')

"""

# i = 0
# while i < 5:
# 	if i == 2:
# 		i += 1  # 使用continue时一定要记得修改计数变量的值,否则会出现死循环去掉i = 2的情况,否则会死循环
# 		continue  # 忽略掉i=2的这一次.否则会死循环
# 	print('第%d次输出' % i)
# 	i += 1
# print('完成')


"""

import random

i = 0
while i < 5:
	num = random.randint(1, 3)
	if num == 2:
		break
	print('第%d次输出' % num)
	i += 1
print('完成')
"""

i = 0
while i < 100:
	i += 1
	if i % 7 == 0:  # 这么设计的目的是跳过i+1=7,但是打印输出的是i,这样设计就实现了将7和7的倍数剔除的效果
		continue  # 这个continue应该是if后面的条件成立的时候,继续进行从while开始的程序,而不是进入后续的程序

	print(i)  # 打印的是7之前的那个数字,或者7的整数倍-1的数字,成功避免7陷入死循环无法跳出来.逻辑上的















