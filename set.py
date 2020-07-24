# set找不同
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
sentence = 'Welcome Back To This Tutorial'
print(set(char_list))
print(set(sentence))
print(set(char_list + list(sentence)))

# 添加元素
unique_char = set(char_list)
unique_char.add('x')
# unique_char.add(['y', 'z'])
# TypeError: unhashable type: 'list'
unique_char.add(1)
unique_char.add('hello')
print(unique_char)

# 删除元素 remove or discard
unique_char.remove(1)
print(unique_char)
unique_char.discard('x')
print(unique_char)
# 全部清除
unique_char.clear()
print(unique_char)

# 筛选
unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))  # 不同于a e i的元素
print(unique_char.intersection({'a', 'e', 'i'}))  # 包含a e i的元素

# ..
char = {x for x in unique_char if x != 'hello'}
print(char)
