import threading
import time


# 对比一下两种情况
def thread_job():
    print('thread_job start')
    for i in range(10):
        time.sleep(0.1)  # 延迟 0.1s
    print('thread_job finish')


added_thread = threading.Thread(target=thread_job, name='T1')
added_thread.start()
print('thread_job Done')
# output:
# thread_job start
# thread_job Done
# thread_job finish

# 可以发现：线程任务还未完成便输出 Done

# 如果要遵循顺序，可以在启动线程后对它调用 join
added_thread.start()
added_thread.join()   # 注意差别！！
print('thread_job Done')
# output:
# thread_job start
# thread_job finish
# thread_job Done


# 使用 join 对控制多个线程的执行非常关键
# 举个例子，假设现在再加一个线程T2，T2的任务量较小，会比T1更快完成
def T1_job():
    print('T1 start')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish')


def T2_job():
    print('T2 start')
    print('T2 finish')


thread_1 = threading.Thread(target=T1_job, name='T1')   # 函数带参数时 通过args=( , , )传入
thread_2 = threading.Thread(target=T2_job, name='T2')
thread_1.start()
thread_2.start()
print('all done')
# 一种output:
# T1 start
# T2 start
# T2 finish
# all done
# T1 finish

# 现在T1和T2都没有join，注意这里说”一种”是因为all done的出现完全取决于两个线程的执行速度
# 完全有可能T2 finish出现在all done 之后
# 这种杂乱的执行方式是我们不能忍受的，因此要使用join加以控制

# 我们试试在T1启动后，T2启动前加上thread_1.join():
thread_1.start()
thread_1.join()     # 注意差别！！
thread_2.start()
print("all done")
# output:
# T1 start
# T1 finish
# T2 start
# T2 finish
# all done

# 可以看到，T2会等待T1结束后才开始运行

# 如果我们在T2启动后放上thread_1.join()会怎么样呢？
thread_1.start()
thread_2.start()
thread_1.join()     # 注意差别！！
print("all done")
# output:
# T1 start
# T2 start
# T2 finish
# T1 finish
# all done

# T2在T1之后启动，并且因为T2任务量小会在T1之前完成；
# 而T1也因为加了join，all done在它完成后才显示。

# 也可以添加thread_2.join()进行尝试
thread_1.start()
thread_2.start()
thread_2.join()     # 注意差别！！
print("all done")
# output:
# T1 start
# T2 start
# T2 finish
# all done
# T1 finish

# 但为了规避不必要的麻烦，推荐如下1221的型排布
thread_1.start()
thread_2.start()
thread_2.join()
thread_1.join()
print('all done')
# output:
# T1 start
# T2 start
# T2 finish
# T1 finish
# all done

# thread_1.join()阻塞主线程，让T1结束后再回到主线程，T1 & T2并行执行
