# 代替三目运算符
print(1 if 1 > 2 else 2)

# 条件语句
a = 1
if a < 2:
    print("lower")
elif a == 2:
    print("equal")
elif a > 2:
    print("bigger")

# 支持链式比较 0 < age < 20

# 断言 assert
# 要求某些条件得到满足（如核实函数参数满足要求或为初始测试和调试提供帮助）
age = -1
assert 0 < age < 100, 'age > 0!'
