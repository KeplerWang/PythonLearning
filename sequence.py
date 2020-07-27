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

# 字典 dictionary
# 1.用 {} 包围
# 2.字典中有 key 和 value 两种元素，key 和 value 可以是字符串/数字
# 3.字典是一个无序的容器
# 4.字典的键必须不可变，可以是数字、字符（串）、元组
dic0 = {'apple': 1, 123 : 'hello', 1.23 : 'hi', tuple1 : list1}
print(dic0)
dic1 = {'apple': 1, 'banana': 2, 'pineapple': 3}
print(dic1['apple'])
dic1['banana'] = 22  # 修改
dic1['pear'] = 4     # 增加
print(dic1)
print(dic1.values())    # 以list形式返回dict的value
print(dic1.popitem())   # 随机返回并删除字典中的一对键和值
temp = dic1.items()     # 以列表返回可遍历的(键, 值) 元组数组
for i in temp:
    print(i, type(i))
del(dic1['banana'])  # 删除 key='banana' 的元素
print(dic1)

for key in dic1.keys():     # 通过 key 来遍历
    print(key, dic1[key])


def func():
    print('func()')


# Sequence 组合
dic2 = {1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9],
        'orange': func}
print(dic2)
print(dic2[2])
print(dic2[2][2])
dic2['orange']()    # 这时存的是函数的地址 加 () 后实现调用

# 和 list 比较，dict 有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多
# 而list相反：
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很少