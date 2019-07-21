# 会用,会写,即可.解释都是官方的 .思想都是面向过程的
# 熟悉基本语法,多写,多用就好

# 面向--->过程 :从过程的角度来考虑问题.是大锅饭的模型,国有化
# 好处:容易理解一步接一步,环环相扣.适合做小型的开发
# 坏处:耦合性强,不利于团队开发.重复代码多.

# 面向--->对象:利于团队开发,降低耦合度.分田到户了,私有化了
# 换了称呼了,方法,属性,对象,实例
# 每个人出来的抽象的东西不一样
# 棋盘(刷新界面,显示棋子),棋手(下棋),计算系统(判断胜负).谁出了问题就找谁
# 降低耦合性,依赖性
# 对象:属性-->变量,方法-->函数  (对象--->过程的对应关系)
# 这些功能函数属于某个对象
# 对象.方法    函数是公有的, 方法是私有的.

# 还是有一定的耦合性,只是降低了耦合性
# 优点:将数据和业务抽象为对象,有利于程序整体结构的分析和设计,使设计思路更加清晰
# 缺点:不好理解

"""
对象:
承载数据,执行操作的一个具体事物.有一些是看的见的有一些是我们抽象出来的(五子棋的计算系统)

对象的组成: 1.保存数据的叫属性,类似面向过程中的变量 2.实现操作,行为,功能的叫方法.类似面向过程的函数.只由这两个组成

类名:大驼峰命名
类:物以类聚,人以群分.存在相同的操作行为.用来描述多个对象共同行为的集合.
通过类来描述对象的属性和方法.类里面来定义对象的属性和方法.
类是一个对象的集合


类和对象的关系:类是创建对象的模板.或者说是 制造手册.类总结了对象的共同特征.用来定义对象的公共行为.

每个对象必须有一个类.有对象之前必须有类.但是细究下去,说不清楚.

比如:飞机图纸就是一个类,根据这个就可以早出许多飞机(对象)

模板 ---- > 类

真正实现行为的是对象.类只是来描述对象的行为方法.


想要有类,先要心中有一个对象.即将看到的物体抽象成一个对象,然后才能有类.



类中既可以有属性,也可以有方法.这个做测试的时候错了,当时就有点疑惑,以后要记住!


"""


# 类和方法只会执行一次

class Dog:
	"""定义狗类"""

	def drink(self):  # 方法会自动添加一个形参self,在类的里面.self:位置参数,必须给一个实参   编程中原则:  谁制造,谁使用
		print(self)  # <__main__.Dog object at 0x0000018ABAE7B208>
		print('喝点江小白')

	# print(self)


# 创建对象  有一个返回值,拿个变量接收一下
dog1 = Dog()  # 实际上是一个全局变量,这里我们将保存一个对象的变量称之为dog1对象
dog1.drink()  # 对象.方法()       Pycharm提示:    v:变量 variable,f:函数 function,m:方法 method c:类 class
print(dog1)  # <__main__.Dog object at 0x0000018ABAE7B208>


"""
# print(self)和print(dog1)的值一样了. 这样就说明self就是dog1
# 调用方法时不需要手动添加实参,解释器会自动添加一个实参给形参(位置参数)


"""

