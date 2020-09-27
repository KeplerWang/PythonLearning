from string import Template
from math import pi, e

# 长字符串 能表示横跨多行的字符串 三引号''' '''
print('''This is a very long string. It continues here.
And it's not over yet. "Hello!"
Still here.''')
# 常规字符串也可以横跨多行，只要在行尾加上反斜杠\，反斜杠和换行符将被转义
print("Hello, \
world!")
# 甚至也可以
print \
    ('Hello, world!')
# 原始字符串 不以特殊方式处理反斜杠 用前缀r表示
print(r'C:\program files\hello')
# 但是引号需要通常那样的进行转义 但这意味着用于执行转义的反斜杠也将包含在最终的字符串中
print(r'Let\'s go!')  # Let\'s go!
# 另外 原始字符串也不能以单个反斜杠结尾
# print(r'C:\') SyntaxError: EOL while scanning string literal

# 设置字符串的格式
print('%s, %f, %g, %e, %d, %x' % ('string', 3.1415926, 1.732222222, 10030025, 1024, 63))
# 模板字符串
tmpl = Template('Hello, $who! $what enough for ya?')
print(tmpl.substitute(who='Mars', what='Dusty'))
# format
print('{name} is approximately {value:.2f}.'.format(value=pi, name='Π'))  # 命名字段
print('{2} is approximately {1}.'.format('hi', pi, 'Π'))  # 索引无需顺序排列
# 如果变量与替换字段同名，可以简写，前面加上f
print(f"Euler's constant is roughly {e}.")
name = 'Kepler'
age = 19
print(f'Hello, {name}! You are {age + 1} years old now.')

price_width = 10
item_width = 25
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:<{}}}{{:>{}.2f}}'.format(item_width, price_width)
print(header_fmt.format('Item', 'Price'))
print(fmt.format('apple', 0.4))
print("that's all folks".title())

# 字符串方法
# 1.center 通过在两边添加填充字符（默认为空格）让字符串居中
print('The Middle by Jimmy Eat World'.center(39))
print('The Middle by Jimmy Eat World'.center(39, '-'))
# more: ljust rjust zfill
# 2.find 在字符串中查找子串，找到就返回第一个字符的索引，否则返回-1
print('With a moo-moo here, and a moo-moo there'.find('moo'))
print('With a moo-moo here, and a moo-moo there'.find('moo1'))
print('With a moo-moo here, and a moo-moo there'.find('moo', 8, 12))  # 设置起点[,终点]
# more: rfind index rindex count startswith endswith
# 3.join 与split相反，用于合并序列的元素
seq = ['1', '2', '3', '4', '5']
x = '+'
print(x.join(seq))
# more: split
# 4.lower 返回小写
print('ABCDEFG'.lower(), 'abcdefg'.islower())
# more: islower istitle isupper isupper translate
# more: capitalize casefold swapcase title upper
# 5.replace 将所有指定字符串替换为另一个字符串，并返回替换的结果
print('can you can a can as a canner cans a can?'.replace('can', '+++'))
# 6.split 与join相反，用于将字符串拆分为序列
print('1+2+3+4+5'.split('+'))
print('1 2 3 4   5'.split())  # 默认分隔符为单个/连续多个空白符
# 7.strip 将字符串开头和末尾的空白删除，并返回删除结果
print('             hello,     world!           '.strip())
print('*************hello,     world? ?!***********'.strip('*!'))  # 指定要删除的字符! 和 *
# more: lstrip rstrip
# 8.translate 替换单个字符
# 使用translate前必须创建一个转换表
table = str.maketrans('cs', 'kz')
print(table)    # c--k, s--z Unicode码点之间的映射
print('this is an incredible test'.translate(table))
table = str.maketrans('cs', 'kz', ' t')  # 指定要将哪些字母删除 t 和 空格
print('this is an incredible test'.translate(table))
# more: replace lower
