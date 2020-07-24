import re

pattern1 = 'cat'
pattern2 = 'bird'
string = 'dog runs to cat'
print(pattern1 in string, pattern2 in string, sep='\n')
# True
# False

print(re.search(pattern1, string))
print(re.search(pattern2, string))
# <re.Match object; span=(12, 15), match='cat'>
# None

# 这里我们还需要注意的是, 建立一个正则的规则, 我们在 pattern 的 “” 前面需要加上一个 r 用来表示这是正则表达式, 而不是普通字符串
pattern3 = r'r[au]n'
# [ab] 可以是a，也可以是b
# [A-Z] 表示的就是所有大写的英文字母
# [0-9a-z] 表示可以是数字也可以是任何小写字母
print(re.search(pattern3, 'dog ran to cat'))
print(re.search(pattern3, 'dog run to cat'))
print(re.search(pattern3, 'dog raun to cat'))
# <re.Match object; span=(4, 7), match='ran'>
# <re.Match object; span=(4, 7), match='run'>
# None

# \d : 任何数字
# \D : 不是数字
# \s : 任何 white space, 如 [\t\n\r\f\v]
# \S : 不是 white space
# \w : 任何大小写字母, 数字和 “” [a-zA-Z0-9]
# \W : 不是 \w
# \b : 空白字符 (只在某个字的开头或结尾)
# \B : 空白字符 (不在某个字的开头或结尾)
# \\ : 匹配 \
# . : 匹配任何字符 (除了 \n)
# ^ : 匹配开头
# $ : 匹配结尾
# ? : 前面的字符可有可无
print(re.search(r'r\dn', 'run r4n'))
# <re.Match object; span=(4, 7), match='r4n'>
print(re.search(r'r\Dn', 'run r4n'))
# <re.Match object; span=(0, 3), match='run'>
print(re.search(r"r\sn", "r\nn r4n"))
# <re.Match object; span=(0, 3), match='r\nn'>
print(re.search(r"r\Sn", "r\nn r4n"))
# <_sre.SRE_Match object; span=(4, 7), match='r4n'>
print(re.search(r"r\wn", "r\nn rn r4n"))
# <_sre.SRE_Match object; span=(4, 7), match='r4n'>
print(re.search(r"r\Wn", "r\nn r4n"))
# <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
print(re.search(r"run\b", "dog runs to cat"))
# None
print(re.search(r"\bruns\b", "dog runs to cat"))
# <re.Match object; span=(4, 8), match='runs'>
print(re.search(r"\B runs \B", "dog   runs  to cat"))
# <_sre.SRE_Match object; span=(8, 14), match=' runs '>
print(re.search(r"runs\\", "runs\\ to me"))
# <_sre.SRE_Match object; span=(0, 5), match='runs\\'>
print(re.search(r"r.n", "r[ns to me"))
# <_sre.SRE_Match object; span=(0, 3), match='r[n'>
print(re.search(r"^dog", "dog runs to cat"))
# <_sre.SRE_Match object; span=(0, 3), match='dog'>
print(re.search(r"cat$", "dog runs to cat"))
# <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(r"Mon(day)?", "Monday"))
# <_sre.SRE_Match object; span=(0, 6), match='Monday'>
print(re.search(r"Mon(day)?", "Mon"))
# <_sre.SRE_Match object; span=(0, 3), match='Mon'>


# 如果一个字符串有很多行, 我们想使用 ^ 形式来匹配行开头的字符, 如果用通常的形式是不成功的.
# 比如下面的 “I” 出现在第二行开头, 但是使用 r"^I" 却匹配不到第二行,
# 这时候, 我们要使用 另外一个参数, 让 re.search() 可以对每一行单独处理.
# 这个参数就是 flags=re.M, 或者这样写也行 flags=re.MULTILINE.
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))
# None
print(re.search(r"^I", string, flags=re.MULTILINE))
# <_sre.SRE_Match object; span=(18, 19), match='I'>

# 分组
# 我们甚至可以为找到的内容分组, 使用 () 能轻松实现这件事.
# 通过分组, 我们能轻松定位所找到的内容.
# 比如在这个 (\d+) 组里, 需要找到的是一些数字,
# 在 (.+) 这个组里, 我们会找到 “Date: “ 后面的所有内容.
# 当使用 match.group() 时, 他会返回所有组里的内容,
# 而如果给 .group(2) 里加一个数, 它就能定位你需要返回哪个组里的信息.
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())
# 021523, Date: Feb/12/2017
print(match.group(1))
# 021523
print(match.group(2))
# Date: Feb/12/2017

# 有时候, 组会很多, 光用数字可能比较难找到自己想要的组,
# 这时候, 如果有一个名字当做索引, 会是一件很容易的事.
# 我们需要在括号的开头写上这样的形式 ?P<名字> 就给这个组定义了一个名字.
# 然后就能用这个名字找到这个组的内容.
match = re.search(r'(?P<id>\d+), Date: (?P<date>.+)', 'ID: 021523, Date: Feb/12/2017')
print(match.group('id'))
print(match.group('date'))

# findall
print(re.findall(r'r[ua]n', 'run ran ren'))
print(re.findall(r'(run|ran)', 'run ran ren'))

# replace
# 通过正则表达式匹配上一些形式的字符串然后再替代掉这些字符串.
# 使用这种匹配 re.sub(), 将会比 python 自带的 string.replace() 要灵活多变.
print(re.sub(r'r[au]ns', 'catches', 'dog runs to cat'))

# split \.表示匹配.
print(re.split(r'[,;\.]', 'a;b,c.d;e'))

# compile
compiled_re = re.compile(r'r[au]n')
print(compiled_re.search('dog ran to cat'))
# <re.Match object; span=(4, 7), match='ran'>
