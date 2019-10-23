# Python ChainMap用法

"""
ChainMap 是一个方便的工具类，它使用链的方式将多个 dict“链”在一起，从而允许程序可直接获取任意一个 dict 所包含的 key 对应的 value。

简单来说，ChainMap 相当于把多个 dict 合并成一个大的 dict，但实际上底层并未真正合并这些 dict，因此程序无须调用多个 update() 方法将多个 dict 进行合并。所以说 ChainMap 是一种合并，但实际用起来又具有较好的效果。

需要说明的是，由于 ChainMap 只是将多个 dict 链在一起，并未真正合并它们，因此在多个 dict 中完全可能具有重复的 key，在这种情况下，排在“链”前面的 dict 中的 key 具有更高的优先级。

例如，下面程序示范了 ChainMap 的用法：
"""

from collections import ChainMap

# 定义三个字典对象
a = {"kotlin":90,"python":86}
b = {"go":93,"python":92}
c = {"swift":89,"go":87}

# 将3个dict 对象链在一起,就像变成了一个大的dict
cm = ChainMap(a,b,c)
print(cm)


# 获取kotlin对应的value
print(cm["kotlin"])
print(cm["python"])
print(cm["python"])
print(cm["go"])
"""
上面程序 a、b、c 三个 dict 链在一起，
组成一个 ChainMap，这个链的顺序就是 a、b、c，因此 a 的优先级最高，b 的优先级次之，c 的优先级最低。运行上面程序，可以看到如下输出结果：
"""


"""
掌握了 ChainMap 的用法之后，接下来介绍的示例程序借鉴了 Python 库文档中的一个例子，该例子将局部范围的定义、全局范围的定义、Python 内置定义链成一个 ChainMap，当程序通过该 ChainMap 获取变量时，将会按照局部定义、全局定义、内置定义的顺序执行搜索。
"""

from collections import ChainMap

import builtins


my_name = "孙悟空"
def test():
    my_name = "yeeku"
    # len = "大圣"

    # 将locals,globals,builtins的变量链接成一个ChainMap
    pylookup = ChainMap(locals(),globals(),vars(builtins))
    # 访问my_name对应的value,优先使用局部范围的定义
    print(pylookup["my_name"])

    # 访问len对应的value,由于局部范围,全局范围都找不到,因此访问内置定义的len函数
    print(pylookup["len"])  # <built-in function len>

test()



"""
下面程序示范了优先使用运行程序的指定参数,然后是系统环境变量,最后才使用系统默认值的实现

"""

# 程序文件名为ChainMap_test.py
from collections import ChainMap
import os,argparse

# 定义默认参数
defaults = {"color":"蓝色","user":"yeeku"}

# 创建程序参数解析器
parser = argparse.ArgumentParser()

# 为参数解析器添加-u (--user) 和-c (--color)参数
parser.add_argument("-u","--user")
parser.add_argument("-c","--color")
# 解析运行程序的参数
namespace = parser.parse_args()
# 将程序参数转换成dict
command_line_args = {k:v for k,v in vars(namespace).items() if v}
# 将command_line_args(解析程序参数而来),os.environ(环境变量),defaults链接成ChainMap
combined = ChainMap(command_line_args,os.environ,defaults)
# 获取color对应的value
print(combined["color"])
print(combined["user"])
print(combined["PYTHONPATH"])

