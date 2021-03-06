"""
匹配单个字符-元字符<meta char>
	.  \n除外的任意一个字符
	[] 里面出现的任意一个字符
	-  范围连接符
	[^] 非 禁止匹配里面的,取反

多个字符
	{n,m}  要求n <= m 才可以,匹配至少n次,至多m次
	?
	+
	*
分组
	匿名分组 创建  r'正则'  获取 结果对象.group(分组编号) 0表示整体
	有名分组
	目的:部分数据的提取
非贪婪 也称之为 懒惰模式
r 对\进行转义,因为\本身就是一个特殊字符
"""

"""
扩展:
	1.>在正则中如果匹配 字符的本来含义 \字符
		例如想要匹配字符中的.,应该是 \. 就可以了
	2.>.字符
		默认情况下,.字符匹配任意字符\n除外,但是如果想要匹配\n
		则使用re.S == re.DOTALL
		re.match(r'a.b')
	3.>\w 在Py3中,re.U 即re.UNICODE ,可以匹配汉字,而在re.A模式中不能匹配汉字
		A是ASCII码的意思,无法匹配汉字,U是unicode的意思,所有的字符都能被匹配
	4.>取消分组
		(?:等等) 
	5.> r'(?P<name>\w??)'非贪婪,0到1次 \w
	6.> 对象 = re.compile(正则)  提前编译,减少编译次数,因为每次re都要编译
		对象.方法(str)
	7.> 如果需要判断生成器是否已经执行完成,才需要捕获生成器代码抛出的异常.
	

"""