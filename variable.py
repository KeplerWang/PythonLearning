# 局部变量
def fun1():
    b = 10  # 局部变量
    print(b)


# print(b)  # Error 'b'未定义

# 全局变量
a = None  # 全局变量


def fun2():
    global a  # 使用全局变量 a
    a = 20


print(a)
fun2()
print(a)
# 若在执行fun2()前未定义全局变量a，在执行后a会被定义
