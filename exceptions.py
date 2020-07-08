# try: except ... as ... :
try:    # 可能产生异常的语句放进try
    file = open('1.txt', 'r+')
except Exception as e:  # 捕获异常 成功则执行 except
    print(e)
    response = input('do you want to create a new file:')
    if response == 'y':
        file = open('1.txt', 'w')
        file.write('hello')
        file.close()
else:   # 如果没有异常 则执行 else
    print(file.readline())
finally:    # 无论有没有异常 都会执行 finally
    print('in finally')
