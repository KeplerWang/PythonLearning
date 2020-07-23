# 共享内存
# | Type code | C Type             | Python Type       | Minimum size in bytes |
# | --------- | ------------------ | ----------------- | --------------------- |
# | `'b'`     | signed char        | int               | 1                     |
# | `'B'`     | unsigned char      | int               | 1                     |
# | `'u'`     | Py_UNICODE         | Unicode character | 2                     |
# | `'h'`     | signed short       | int               | 2                     |
# | `'H'`     | unsigned short     | int               | 2                     |
# | `'i'`     | signed int         | int               | 2                     |
# | `'I'`     | unsigned int       | int               | 2                     |
# | `'l'`     | signed long        | int               | 4                     |
# | `'L'`     | unsigned long      | int               | 4                     |
# | `'q'`     | signed long long   | int               | 8                     |
# | `'Q'`     | unsigned long long | int               | 8                     |
# | `'f'`     | float              | float             | 4                     |
# | `'d'`     | double             | float             | 8                     |
import multiprocessing as mp

# Shared Value
value1 = mp.Value('i', 0)
value2 = mp.Value('d', 3.14)
# 其中d和i参数用来设置数据类型的，d表示一个双精浮点类型，i表示一个带符号的整型。

# Shared Array
array = mp.Array('i', [1, 2, 3, 4])
# 只能是一维的
# array = mp.Array('i', [[1, 2], [3, 4]]) # 2维list
