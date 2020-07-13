import threading
from queue import Queue


# 函数的参数是一个列表li和一个队列q，函数的功能是，对列表的每个元素进行平方计算，将结果保存在队列中
def job(li, q):
    for i in range(len(li)):
        li[i] = li[i] ** 2
    q.put(li)    # 多线程调用的函数不能用return返回值


# 在多线程函数中定义一个Queue，用来保存返回值，代替return，定义一个多线程列表，初始化一个多维数据列表，用来处理
q = Queue()     # q中存放返回值，代替return的返回值
threads = []    # 定义四个线程
data = [[1, 2, 3],
        [3, 4, 5],
        [4, 4, 4],
        [5, 5, 5]]
for i in range(4):
    t = threading.Thread(target=job, args=(data[i], q))
    t.start()
    threads.append(t)   # 把每个线程append到线程列表中
# 分别join四个线程到主线程
for thread in threads:
    thread.join()
# 定义一个空的列表results，将四个线运行后保存在队列中的结果返回给空列表results
results = []
for _ in range(4):
    results.append(q.get())
print(results)
