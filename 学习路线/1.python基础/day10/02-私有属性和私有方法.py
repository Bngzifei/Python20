"""私有属性:

属性私有后,只能在类的定义里面使用,不能在外部使用,只要在属性名字前面加上双下划线__

方法私有后也是只能在类里面使用,外部无法使用.在方法名前面加双下划线__

看需求使用.

自己摸索,总结,领悟.

__init__(self) 里面定义的属性都是实例属性.
只要在方法里面看到形参self,就是实例方法.

"""


class Dog:
	def __init__(self):
		self.__age = None  # 私有属性:空 不想给它赋值没有数据,但是None在内存上面也是有地址的

	def set_age(self, age):
		if age >= 0 and age <= 20:  # 满足需求再把数据赋值给属性
			self.__age = age  # 私有属性:只能在class类的内部进行使用
		else:
			print('数据不满足')

	def get_age(self):  # 只能通过方法去调用私有属性的值.大部分都是只在类里面使用.就是不想在外部使用就用私有属性
		return self.__age  # 必须另外创建新的方法来获取私有属性的值(当在类的外部使用对象操作的时候),在类外部使用的时候通过这个方法来获取私有属性的值.

	def __info(self):  # 私有方法:只是起一个封装的作用.可以都不要,但是为了以后的好处必须尽量使用
		print('hello')
		"""51-100"""

	def drink(self):
		"""1-50"""
		self.__info()  # 对象.方法  的方式.  这里self就是一个对象了.  self.__info()


dog1 = Dog()  # 先创建一个dog1对象
# dog1.age = -10  # 脏数据,垃圾数据.会影响计算结果,影响程序运行的稳定性.尽量避免这样的脏数据.所以在使用这个数据的时候需要进行判断处理.
dog1.set_age(10)  # 外部对象通过普通方法来设置私有属性  对象年龄 的值.
dog1.age = 100  # 定义了一个新的普通属性
dog1.__age = -20  # 还是定义了一个新的普通属性,只是和私有属性同名而已,注意区分.自己编写的时候不要这么写.

dog1.drink()  # 对象.方法  来调用方法(和函数的调用一样)     通过另外一个普通方法来调用私有方法,获取私有方法的返回值.
print(dog1.age)
print(dog1.__age)  # 这只是一个普通属性的值,只是和私有属性重名了.注意区分
print(dog1.get_age())  # 通过另外一个方法来获取私有属性的值

# 如果在写代码的时候看到没有提示了就要注意了是不是有错误


# 也可以通过__init__()方法来调用修改私有属性的值,这时候__init__()方法就和其他的普通方法一样了.
