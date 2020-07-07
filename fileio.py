# 换行符 \n
text = 'This is the first text.\nThis is the second text.\nThis is the third text.'
print(text)

# 制表符 \t
text = '\tThis is my first line.\n\tThis is the second line.\n\tThis is the third line'
print(text)

# 读文件方式 open
file = open('if.py', 'r')
para = file.readline()
print(para)

para = open('test.txt', 'r').readlines()
print(para)  # para 是一个 list
for i in para:
    print(i)

file = open('test.txt', 'a+')
append_text = '\nThis is a new line.'
file.write(append_text)

file.close()
