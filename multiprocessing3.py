import multiprocessing as mp
import threading as td
import time

def job(q):
    res = 0
    for i in range(10000000):
        res += i + i ** 2 + i ** 3
    q.put(res)


def multiCore():
    queue = mp.Queue()
    process1 = mp.Process(target=job, args=(queue,))
    process2 = mp.Process(target=job, args=(queue,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    res1 = queue.get()
    res2 = queue.get()
    print('multiCore:', res1 + res2)


def multiThread():
    q = mp.Queue()  # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multiThread:', res1 + res2)


def normal():
    res = 0
    for _ in range(2):
        for i in range(10000000):
            res += i + i ** 2 + i ** 3
    print('normal:', res)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multiThread()
    st2 = time.time()
    print('multiThread time:', st2 - st1)
    multiCore()
    st3 = time.time()
    print('multiCore time:', st3 - st2)

# normal: 4999999666666716666660000000
# normal time: 12.45940613746643
# multiThread: 4999999666666716666660000000
# multiThread time: 13.175164937973022
# multiCore: 4999999666666716666660000000
# multiCore time: 6.596951961517334
