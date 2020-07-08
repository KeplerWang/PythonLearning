# 浅拷贝只是拷贝了最外围的对象本身，内部元素都只是拷贝了一个引用
import copy
a = [1, 2, 3]
a_copy = copy.copy(a)               # 浅拷贝只拷贝了a的最外围对象本身
print(id(a) == id(a_copy))          # False
print(a is a_copy)                  # False
a_copy[2] = 4
print('a: ', a, '\na_copy: ', a_copy)
# output:
# a:  [1, 2, 3]
# a_copy:  [1, 2, 4]                # a[2]的值没改变，a_copy[2]的值改变了

print('-----------------------')

b = [1, 2, [3, 4]]
b_copy = copy.copy(b)               # 浅拷贝只拷贝第一层，第二层list[3, 4]失效
print(id(b) == id(b_copy))          # False
print(id(b[2]) == id(b_copy[2]))    # True
b_copy[2][1] = 5
print('b: ', b, '\nb_copy: ', b_copy)
# output:
# b:  [1, 2, [3, 5]]
# b_copy:  [1, 2, [3, 5]]           # b[2][1] 和 b_copy[2][1] 的值都改变了

print('-----------------------')

# 深拷贝对外围元素和内部元素都拷贝了对象本身，而不是对象的引用
c = [1, 2, 3]
c_copy = copy.deepcopy(c)
print(id(c) == id(c_copy))          # False
print(c is c_copy)                  # False
c_copy[1] = 4
print('c: ', c, '\nc_copy: ', c_copy)
# output:
# c:  [1, 2, 3]
# c_copy:  [1, 4, 3]

print('-----------------------')

d = [1, 2, [3, [4, 5, [6]]]]
d_copy = copy.deepcopy(d)
print(id(d) == id(d_copy))          # False
print(id(d[2]) == id(d_copy[2]))    # False
print(id(d[2][1]) == id(d_copy[2][1]))  # False
print(id(d[2][1][2]) == id(d_copy[2][1][2]))    # False
print(id(d[2][1][2][0]) == id(d_copy[2][1][2][0]))    # True    都是数 6

d_copy[2][1][2][0] = 7
print('d: ', d, '\nd_copy: ', d_copy)
# output:
# d:  [1, 2, [3, [4, 5, [6]]]]
# d_copy:  [1, 2, [3, [4, 5, [7]]]]     # 只改变了 d_copy
