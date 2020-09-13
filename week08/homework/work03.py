# 实现一个@timer装饰器，记录函数运行时间，考虑函数的不定长参数

import time

def timer(func):
    def time_decorate(*args,**kwargs):
        start_tiem = time.time()
        res = func(*args,**kwargs)
        end_time = time.time()
        sum_time = end_time - start_tiem
        print(f"func：{func.__name__} cost：{sum_time}")
        return res
    return time_decorate

@timer
def func1(a,b):
    res = a+b
    print(f'rse:{res}')
    time.sleep(10)

if __name__ == '__main__':
    func1(10,20)