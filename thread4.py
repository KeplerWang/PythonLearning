# python 的多线程 threading 有时候并不是特别理想.
# 最主要的原因是就是, Python 的设计上, 有一个必要的环节, 就是 Global Interpreter Lock (GIL).
# 这个东西让 Python 还是一次性只能处理一个东西.
# 我从这里摘抄了一段对于 GIL 的解释.
# 尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。
# 实际上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。
# GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势
# 比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行。
# 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。
# 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。
# 实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。
import threading
from queue import Queue
import copy
import time


def job(li, q):
    res = sum(li)
    q.put(res)


def multiThreading(li):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(li), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    #   for t in threads:
#       t.join()
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(li):
    total = sum(li)
    print(total)


if __name__ == '__main__':
    li = list(range(1000000))
    s_t = time.time()
    normal(li * 4)  # li*4 将 li 重复4次 如[1, 2, 3]*3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    print('normal: ', time.time() - s_t)
    s_t = time.time()
    multiThreading(li)
    print('multiThreading: ', time.time() - s_t)

# output
# 1999998000000
# normal:  0.07152700424194336
# 1999998000000
# multiThreading:  0.06424903869628906

# 我们的运算结果没错, 所以程序 threading 和 Normal 运行了一样多次的运算.
# 但是我们发现 threading 却没有快多少, 按理来说, 我们预期会要快3-4倍,
# 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪.
