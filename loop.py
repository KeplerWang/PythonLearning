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

# 高级1.迭代器实现
# 高级2.生成器实现
