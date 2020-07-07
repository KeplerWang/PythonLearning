# 自定义函数
def func1(x, y):
    return x - y


print(func1(1, 9))
print(func1(y=1, x=9))


# 函数的默认参数
# 默认参数 不能出现 在 非默认参数 之前
def func2(x, y, z=1):
    return x + y + z


print(func2(1, 9))
print(func2(y=1, x=9))
print(func2(z=2, y=0, x=1))

# 高级3.自调用
# 高级4.可变参数
# 高级5.关键字参数
