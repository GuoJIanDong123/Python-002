## 异常捕获与处理
### 异常的捕获示例
- StopIteration 异常示例：
```Python
genumber = (i for i in range(0,2))
print(next(genumber))
print(next(genumber))
try:
    print(next(genumber))
except StopIteration:
    print('最后一个元素')
```
### 异常处理机制的原理
- 异常也是一个类
- 异常捕获的过程：
   - 异常类把错误消息打包到一个对象
   - 然后该对象会自动查找到调用栈
   - 直到运行系统找到明确声明如何处理这些类异常的位置
- 所有异常继承自BaseException
- TraceBack显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的
- 捕获异常可以使用try...except语法
- try...except支持多重异常处理
- 常见的异常类型主要有：
   - LookupError 下的IndexError 和KeyError
   - IOError
   - NameError
   - TypeError
   - AttributeError
   - ZeroDivisionError
### 自定义异常
```Python
class UserInputError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self,ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo
 ```
 ### 魔法方法
 ```Python
 class Open:
  # 首先调用这个方法
    def __enter__(self):
        print('open')
   # 最后调用这个方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("close")

    def __call__(self):
    # with 调用这个方法
        pass
with Open() as f:
    pass
 ```
## Pmysql数据库处理

- 创建connection
- 获取cursor
- CURD（查询并获取数据）
- 关闭cursor
- 关闭connection

## 反爬虫：模拟浏览器的头部信息

### 浏览器的基本行为
- 带http头信息：如User-Agent,Referer等
- 带cookies（包含用户名，密码验证信息）

### 下载中间件
- process_request(request,spider)
   - request对象经过下载中间件会被调用，优先级高先调用
- process_reponse（request,response,spider）
   - response对象经过下载中间件会被调用，优先级高后调用
- process_exception(request,exception,spider)
   - process_response()和process_request()抛出异常时会被调用
- from_crawl(cls,crawler)
   - 使用crawl来创建中间器对象，并(必须)返回一个中间件对象

