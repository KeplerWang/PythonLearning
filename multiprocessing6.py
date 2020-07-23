# 进程锁
import multiprocessing as mp
import time


def job1(v, num):
    for _ in range(5):
        time.sleep(0.1)  # 暂停0.1秒，让输出效果更明显
        v.value += num  # v.value获取共享变量值
        print(v.value, end=' ')


def multiCore1():
    v = mp.Value('i', 0)  # 定义共享变量
    p1 = mp.Process(target=job1, args=(v, 1))
    p2 = mp.Process(target=job1, args=(v, 3))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()


# 在上面的代码中，我们定义了一个共享变量v，两个进程都可以对它进行操作。
# 在job()中我们想让v每隔0.1秒输出一次累加num的结果，但是在两个进程p1和p2 中设定了不同的累加值。
# 所以接下来让我们来看下这两个进程是否会出现冲突。
if __name__ == '__main__':
    multiCore1()
# 我们可以看到，进程1和进程2在相互抢着使用共享内存v。


# 加锁后
def job2(v, num, l):
    l.acquire()  # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num  # 获取共享内存
        print(v.value, end=' ')
    l.release()  # 释放


def multiCore2():
    l = mp.Lock()  # 定义一个进程锁
    v = mp.Value('i', 0)  # 定义共享内存
    p1 = mp.Process(target=job2, args=(v, 1, l))  # 需要将lock传入
    p2 = mp.Process(target=job2, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    print()
    multiCore2()
