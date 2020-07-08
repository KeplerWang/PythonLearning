# zip函数接受任意个序列作为参数，合并后返回多个 tuple
a = [1, 2, 3, 4, 5]
b = ('a', 'c', 'd', 'b')
ab = zip(a, b)
print(tuple(zip(a, b)))
print(list(zip(a, b)))
print(dict(zip(a, b)))

# for i in ab:  # or list(ab)
#     print(i)

# lambda 定义一个简单函数，实现简化代码的功能
fun = lambda x, y: x + y    # do not assign a lambda expression, use a def
print(fun(1, 2))


# map 把函数和参数绑定在一起
def func(x, y):
    return x + y


print(list(map(fun, [1], [2])))
print(list(map(fun, [1, 2], [3, 4])))

