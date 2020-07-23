# 存储进程输出 Queue
# Queue的功能是将每个核或线程的运算结果放在队里中，
# 等到每个线程或核运行完毕后再从队列中取出结果， 继续加载运算。
# 原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果
import multiprocessing as mp


def job1(q):  # 该函数没有返回值
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)


def job2(q):  # 该函数没有返回值
    res = 0
    for i in range(500):
        res += i + i ** 2 + i ** 3
    q.put(res)


if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job1, args=(q,))
    # args 的参数只要一个值的时候，参数后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
    p2 = mp.Process(target=job2, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(q.get(), q.get())

# 如果q是一个list... 输出q是空的
# 因为传入参数q只是传入一个deep_copy，进程内修改q不会影响原q
# 线程情况下则不一样，与Queue没有区别
# 线程共享内存变量 进程内存变量是隔离的
