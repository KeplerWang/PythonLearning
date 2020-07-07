# input 输入
input1 = input('input1: ')
print(input1)

input2 = input('input2: ')
# print('bigger' if input2 > 20 else 'not bigger') # Error : 默认 input2 是一个 str ，不能与 int 进行比较
print('bigger' if int(input2) > 20 else 'not bigger')  # 使用类型转换

