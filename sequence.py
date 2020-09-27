# 元组 tuple
# 1.用 () 或  来包围
# 2.元组定义后不能修改
# 3.都可以被迭代 用索引定位 索引[-1] 表示最后一个元素
tuple1 = (1, 5, 3, 8, 10, 2)
tuple2 = 2, 10, 6, 16, 20, 4
tuple3 = (123,) # 一个tuple
tuple4 = (123)  # 一个int 123
tuple5 = tuple()
print(tuple5)
print(tuple3, tuple4, sep='--')
for content in tuple1:
    print(content)
print('####')
# tuple1[0] = 10  # Error: tuple 不支持更改元素
del tuple3  # 可以一下删除tuple
print(tuple1[-1])
print(tuple1)
print(tuple1 + tuple2)  # 两个序列连接
print(tuple1 * 3)       # 序列重复3次
print(tuple(['hi', 1, 3.33]))   # list转tuple


# 列表 list
# 1.用 [] 来包围
# 2.列表定义后可以修改
# 3.列表是一种有序序列，有一系列自带操作
# 4.都可以被迭代 用索引定位 索引[-1] 表示最后一个元素
list1 = [3, 15, 9, 24, 30, 6, 3]
for index in range(len(list1)):
    print(list1[index])
print('####')

print(list1[-1])
print(list1.index(3))   # 查找元素 3 第一次出现的索引
print(list1.count(3))   # 统计元素 3 出现的次数

list1[0] = 30
print(list1)

list1.append(40)
print(list1[-1])    # append() 将元素加在最后

list1.insert(1, 16)
print(list1)        # insert(1, 16) 在索引 1 处插入一个 16

list1.sort()        # 从小到大排序
# list1.sort(reverse=True)    # 从大到小排序
print(list1)        # sort() 将list排序

list1.pop()         # 删除最后一个元素
list1.pop(2)        # 删除 index=2 的元素
del(list1[1])       # 删除 index=1 的元素
list1.remove(3)     # 删除元素3
print(list1)
print(list(tuple1)) # tuple转list

# 二维列表
multi_dim_list = [[1, 2],
                  [4, 5],
                  [7, 8]]  # 3行2列
print(multi_dim_list[0])  # 一维list
print(multi_dim_list[1][1])

# 序列解包
values = 1, 2, 3, 4, 5
print(values)
x, y, z, i, j = values
print(x, y, z, i, j)
x, y, z, *rest = values
print(x, y, z, rest)
x, y, *rest, z = values
print(x, y, z, rest)

