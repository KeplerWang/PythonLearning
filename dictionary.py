# 字典 dictionary
# 1.用 {} 包围
# 2.字典中有 key 和 value 两种元素，key 和 value 可以是字符串/数字
# 3.字典是一个无序的容器
# 4.字典的键必须不可变，可以是数字、字符（串）、元组
from sequence import list1, tuple1

dic0 = {'apple': 1, 123: 'hello', 1.23: 'hi', tuple1: list1}
print(dic0)
dic1 = {'apple': 1, 'banana': 2, 'pineapple': 3}
print(dic1['apple'])
dic1['banana'] = 22  # 修改
dic1['pear'] = 4  # 增加
print(dic1)
print(dic1.values())  # 以list形式返回dict的value
print(dic1.popitem())  # 随机返回并删除字典中的一对键和值
temp = dic1.items()  # 以列表返回可遍历的(键, 值) 元组数组
for i in temp:
    print(i, type(i))
del (dic1['banana'])  # 删除 key='banana' 的元素
print(dic1)

for key in dic1.keys():  # 通过 key 来遍历
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
dic2['orange']()  # 这时存的是函数的地址 加 () 后实现调用

# 和 list 比较，dict 有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢
# 需要占用大量的内存，内存浪费多
# 而list相反：
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很少

# 将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341'}
print("Alice's phone number is {Alice}".format_map(phonebook))

# 字典方法
# 1.clear 删除所有字典项
# 2.copy 返回一个新字典，浅拷贝
# 3.fromkeys 创建一个新字典，包含指定的键，且每个键对应的值都是None(默认)
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], 'unknown'))
# 4.get 使用get访问不存在的键时，不会引发异常，而是默认返回None
print(phonebook.get('Alice'), phonebook.get('Dave', 'N/A'))
# print(phonebook['Dave'])    # KeyError: 'Dave'
# 5.items 返回一个包含所有字典项的字典视图，每个元素为(key, value)的形式
p_items = phonebook.items()
print(p_items)
phonebook['Karl'] = '1345'
print(p_items)  # 始终是底层字典的反映，实时的
print(list(p_items))
# 6.keys 返回一个包含所有键的字典视图
print(phonebook.keys())
# 7.pop 获取与指定键相关的值，并删除
print(phonebook.pop('Karl'), '-----', phonebook)
# 8.popitem 类似pop 但随机弹出一个
# 9.setdefault 有点像get，当不包含指定键时，将其加入字典中
print(phonebook.setdefault('Alice', 'N/A'))
print(phonebook.setdefault('Karl', '0000'))
print(phonebook)
# 10.update 用一个字典中的项更新另一个字典
y = {'Karl': '1234'}
phonebook.update(y)
print(phonebook)
# 11.values 返回值组成的字典视图
