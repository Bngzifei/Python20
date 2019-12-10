"""
抽象类表示接口.

本章讨论的话题是接口:从鸭子类的代表特征动态协议,到使接口更明确,能验证实现是否符合规定的抽象基类(Abstract Base Class)


如果你用过Java,C#或类似的语言,你会觉得鸭子类型的非正式协议很新奇.但是对长时间使用Python或者Ruby的程序员来说,这是接口的常规方式,新知识是抽象基类的严格规定和类型检查.Python2.6才引入抽象基类.


本章先说明Python社区以往对接口的不严谨理解:部分实现接口通常被认为是可接受的.我们将通过几个示例强调鸭子类型的动态本性,从而澄清这一点.


专门讲解抽象基类.首先,本章说明抽象基类的常见用途:实现接口时作为超类使用.然后,说明抽象基类如何检查具体子类是否符合接口定义,以及如何示意注册机制声明一个类实现了某个接口,而不进行子类化操作.最后,说明如何让抽象基类自动"识别"任何符合接口的类---不进行子类化或注册.


我们将实现一个新抽象类,看看它的运作方式.但是,我和Alex Martelli 都不建议你自己编写抽象基类,因为很容易过度设计.

抽象基类与描述符和元类一样,是用于构建框架的工具.因此,只有少数Python开发者编写的抽象基类不会对用户施加不必要的限制,让他们做无用功.

下面我们从Python风格的角度探讨接口.





"""