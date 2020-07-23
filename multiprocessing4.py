# !！待完善！！

# 进程池Pool
# 进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题
# 有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。
# Pool和之前的Process的不同点是丢向Pool的函数有返回值，而Process的没有返回值。
import multiprocessing as mp


def job(x):
    return x * x


def multiCore():
    # 通过在Pool中传入processes参数即可自定义需要的核数量，Pool默认大小是CPU的核数
    pool = mp.Pool(processes=3)  # 定义CPU的核数为3
    # 用map()获取结果，在map()中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果
    res = pool.map(job, range(10))
    print(res)

    # 除了map()外，还有可以返回结果的方式
    # apply_async()中只能传递一个参数值，它只会放入一个核进行运算，但传入值时要注意是可迭代的
    # 所以在传入值后要加逗号，同时要用get()方法获取返回值
    res = pool.apply_async(job, (2,))
    print(res.get())

    # 试试在apply_async()中多传入几个值试试
    # res = pool.apply_async(job, (2, 3, 4,))
    # res = pool.apply_async(job, range(10))
    # print(res.get())
    # TypeError: job() takes 1 positional argument but 3/10 were given
    # 即apply_async()只能输入一组参数

    # 在此 我们将apply_async()放入迭代器中，定义一个新的multi_res
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print(multi_res[0].get())   # multi_res是一个list，元素是一个（只有一个元素的）Queue
    print([r.get() for r in multi_res])


if __name__ == '__main__':
    multiCore()
