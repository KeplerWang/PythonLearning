

# 高级1.迭代器实现
# 只要类中实现了 __iter__ 和 __next__ 函数，那么对象就可以在 for 语句中使用
class Fib(object):
    def __init__(self, number):
        self.max = number
        self.n, self.a, self.b = 1, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return self.a
        raise StopIteration()


# using Fib object
for Fib_i in Fib(5):
    print(Fib_i)


# 高级2.生成器实现
# 使用 yield 关键字也能实现类似迭代的效果，yield 语句每次 执行时，立即返回结果给上层调用者，而当前的状态仍然保留，以便迭代器下一次循环调用。这样做的 好处是在于节约硬件资源，在需要的时候才会执行，并且每次只执行一次
def fib(maximum):
    fib_a, fib_b = 0, 1
    while maximum:
        fib_a, fib_b = fib_b, fib_a+fib_b
        maximum -= 1
        yield fib_a


# using generator
for fib_i in fib(5):
    print(fib_i)


# 高级3.自调用
# if __name__ == '__main__':
#     #code_here
# 如果执行该脚本的时候，该 if 判断语句将会是 True,那么内部的代码将会执行
# 如果外部调用该脚本，if 判断语句则为 False,内部代码将不会执行

# 高级4.可变参数
# 可变参数在函数定义不能出现在特定参数和默认参数前面，因为可变参数会吞噬掉这些参数
# 可变参数可以为任意个
def GetGrade(name, math=150, *grade):
    grades = 0
    for k in grade:
        grades += k
    print(name + "'s grade is ", grades, "+", math)


GetGrade("Kepler", 149, 100, 100)
GetGrade("Wang", 149)


# 高级5.关键字参数
# 可以传入任意个含参数名的参数，这些参数名在函数定义中并没有出现，这些参数在函数内部自动封装成一个字典(dict).
def portrait(name, **kwargs):
    print("name", name)
    for k, v in kwargs.items():
        print(k, v)


portrait("Kepler", sex="male", single=False, health="fine")
