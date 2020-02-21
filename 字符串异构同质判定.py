# 请编码实现一个命令行工具，判定两个指定的字符串是否异构同质；异构同质的定义为：一个字符串的字符重新排列后，能变成另一个字符串。
#
# 输入描述:
# 以空格字符分隔的两个字符串；输入字符串的合法字符集为[a-zA-Z0-9 ]，大小写敏感，无需考虑异常输入场景。
#
# 输出描述:
# 如果判定两个字符串异构同质，则输出true，否则输出false。
#
# 输入例子1:
# abc acb
#
# 输出例子1:
# true


from collections import Counter
s1, s2 = input().split()
c1 = Counter(s1)
c2 = Counter(s2)
if c1 == c2:
    print('true')
else:
    print('false')
