## 基于twisted的异步IO框架
- 多任务模型分为同步模型和异步模型，scrapy 使用的是Twisted模型
- Twisted是异步编程模型，任务之间互相独立，用于大量IO密集操作

## 多进程模型
- 多进程、多线程、协程的目的都是尽可能多处理任务
- 产生新的进程可以使用以下方式：
   - os.fork()
   - multiprocessing.Process()
- 多进程的第一个问题：进程的父子关系
