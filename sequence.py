# 元组 tuple
# 1.用 () 或  来包围
# 2.元组定义后不能修改
# 3.都可以被迭代 用索引定位 索引[-1] 表示最后一个元素
tuple1 = (1, 5, 3, 8, 10, 2)
tuple2 = 2, 10, 6, 16, 20, 4
for content in tuple1:
    print(content)
print('####')
# tuple1[0] = 10  # Error: tuple 不支持更改元素
print(tuple1[-1])
print(tuple1)


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
print(list1)        # insert(1, 16) 在索引 1 处加一个 16

list1.sort()        # 从小到大排序
# list1.sort(reverse=True)    # 从大到小排序
print(list1)        # sort() 将list排序


# 二维列表
multi_dim_list = [[1, 2],
                  [4, 5],
                  [7, 8]]  # 3行2列
print(multi_dim_list[0])  # 一维list
print(multi_dim_list[1][1])

# 字典 dictionary
# 1.用 {} 包围
# 2.字典中有 key 和 value 两种元素，key 和 value 可以是字符串/数字
dic1 = {'apple': 1, 'banana': 2, 'pineapple': 3}
print(dic1['apple'])


