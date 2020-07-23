# 多进程
# 和线程的使用方法类似
import multiprocessing as mp


def job(a, d):
    print('job', a, d)


if __name__ == '__main__':
    p1 = mp.Process(target=job, args=(1, 2))
    p1.start()
    p1.join()
