### 一、类和属性
#### 1、属性（类属性和对象属性）
   - 类属性与对象属性
   - 类属性字段在内存中只保存一份
   - 对象属性在每个对象都保存一份
   
#### 2、方法(三种方法)
   - 普通方法 至少一个self参数，表示该方法的对象
   - 类方法 至少一个cls参数，表示该方法的类
   - 静态方法 由类调用，无参数
   - 三种方法在内存中都归属于类
   
#### 3、属性的处理
   - __getattribute__()
   - __getattr__()
   - 异同
     - 都可以对实例属性进行获取拦截
     - __getattr() 适用于未定义的属性
     - __getattribute__() 对所有属性的访问都会调用该方法
     
#### 4、属性描述符property
   - 描述器：实现特定协议(描述符)的类
   - property 类需要实现_get_、_set_、_delete_方法
   
   
'''
class Teacher:
    def __int__(self,name):
       self.name = name
    def __get__(self):
       return self.name
    def __set__(self,value):
       self.name = value
 pythonteacher = Teacher('yin')
'''

