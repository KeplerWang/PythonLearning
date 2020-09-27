# 循环语句 foreach while
for i in range(0, 3):
    print(i)

j = 10
while j > 5:
    print(j)
    j = j - 1   # 没有自增自减

# break & continue
while True:
    a = input('type a number: ')
    if a == '1':
        break  # continue
    else:
        pass   # 跳过
    print('still in while')
print('out of while')

# 迭代时获取索引 enumerate
for index, string in enumerate('Hello!'):
    print('index =', index, 'string =', string)

# 反向迭代和排序后再迭代
print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello World!'))
print(list(reversed('Hello World!')))
print(''.join(reversed('Hello World')))

# 如何判断是break 还是 顺序执行结束
for i in range(10):
    print('i =', i)
    if int(input('type a number:')) == 8:
        print('break out, not come out')
        break
else:
    print('come out, not break out')    # 不是因break而结束时执行

# ? 可以作为 condition
# 1.数字
# condition = 10
# while condition:
#     print(condition)
#     condition -= 1
# 2.None类型
# 3.集合类型 list tuple dictionary set
# a = range(10)
# while a:
#     print(a[-1])
#     a = a[:len(a)-1]

# 集合推导
print([x*x for x in range(10)])
print([x*x for x in range(10) if x % 2 == 0])
print([(x, y) for x in range(3) for y in range(4) if x != y])
# 字典推导
print({i: "{} squared is {}".format(i, i**2) for i in range(10)})

# 高级1.迭代器实现
# 高级2.生成器实现
