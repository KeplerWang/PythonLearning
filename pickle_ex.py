# pickle是一个 python 中, 压缩/保存/提取 文件的模块.
# 最一般的使用方式非常简单. 比如下面就是压缩并保存一个字典的方式.
# 字典和列表都是能被保存的.
import pickle

# pickle保存
a_dict = {'da': 111, 2: [23, 1, 4], '23': {1: 2, 'd': 'sad'}}
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# pickle提取
with open('pickle_example.pickle', 'rb') as file:
    a_dict1 = pickle.load(file)
# 用with+open文件 结束后自动关闭文件
print(a_dict1)
