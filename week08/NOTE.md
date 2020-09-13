### 一、变量的赋值
#### 1、可变数据类型
   - 列表list
   - 字典 dict
#### 2、不可变数据类型：
   - 整型 int
   - 浮点型 float
   - 字符串型 string
   - 元组 tuple
   
### 二、序列
#### 1、序列分类
   - 容器序列：list,tuple,collection.deque等，能存放不同类型的的数据
   - 扁平序列：str、bytes、bytearray、memoryview（内存视图）等，存放的是相同的数据类型
#### 2、容器序列存在深拷贝、浅拷贝问题
   - 注意：非容器(数字、字符串、元组)类型没有拷贝问题
   - 深拷贝是指重新申请一份内存，将被拷贝的容器数据复制到新申请的内存中
   - 浅拷贝是指将要拷贝的容器地址复制到新的内存中
   
   
### 三、变量
#### 1、变量的作用域
##### 高级语言对变量的使用
   - 变量的声明
   - 定义类型(分配内存空间大小)
   - 初始化(赋值、填充内存)
   - 引用(通过对象名称，调用对象的内存数据结构)
##### Python的区别
   - 在模块、类、函数中才有作用域的概念
   
##### Python作用域遵循LEGB规则
   - L-Local(function):函数内的名称空间
   - E-Enclosing function locals:外部嵌套函数的名字空间
   - G-Global(module)：函数定义所在模块(文件的名字空间)
   - B-Builtin(Python):Python 内置模块的名字空间

### 四、函数
#### 1、Lambda表达式
   - Lambda只是表达式，不是所有的函数逻辑都能封装进去
   - 例子 k = lambda x:x+1   print(k(1))
   - Lambda表达式后面只能有一个表达式
      - 实现简单函数的时候可以使用Lambda表达式替代
      - 使用高阶函数的时候一般使用Lambda表达式替代
 
#### 2、高阶函数
   - 高阶：参数是函数，返回值是函数
   - 常见的高阶函数：map,reduce,filter,apply
   - apply在Python2.3中移除，reduce被放在functools包中
   - 推导式和生成器表达式可以替代map和filter函数
   
#### 3、返回值
   - 返回关键字
      - return
      - yield
   - 返回的对象
      - 可调用对象--闭包(装饰器)
      
 #### 4、装饰器
    - 增强而不改变原有的函数
    -装饰器强调函数的定义态而不是运行态
、、、python

  @decorate
  def target():
     print('dosomthing)
     
   def target():
     print('do something')
     
   target = decorate(target)
 
、、、
   
   
   
   
   
   
   
   
   
   
   
