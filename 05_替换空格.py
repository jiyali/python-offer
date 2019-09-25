# 题目：请实现一个函数，将一个字符串中的每个空格替换成“%20”。
#       例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
# 第一种方法：
# Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。


def replace1(string):
    if type(string) != str:
        return False
    return string.replace(' ', '%20')


print(replace1(string='we are happy'))


# 第二种方法：使用append一次遍历即可替换，时间复杂度O(n)


def replace2(string):
    if type(string) != str:
        return False
    string = list(string)
    stringReplace = []
    for i in string:
        if i == ' ':
            stringReplace.append('%')
            stringReplace.append('2')
            stringReplace.append('0')
        else:
            stringReplace.append(i)
    return "".join(stringReplace)


print(replace2(string='we are happy'))


# 第三种：创建新的字符串进行替换


def replace3(string):
    tmpstr = ''
    for i in string:
        if i == ' ':
            tmpstr += '%20'
        else:
            tmpstr += i
    return tmpstr


print(replace3(string='we are happy'))

# 第四种：使用两个指针，从后往前替换空格


def replace4(string):
    if type(string) != str:
        return False
    if string is None or len(string) == 0:
        return False
    spaceNum = 0
    for i in string:
        if i == ' ':
            spaceNum += 1

    newStrLen = len(string) + spaceNum * 2
    newStr = newStrLen * [None]
    indexOfOriginal, indexOfNew = len(string) - 1, newStrLen - 1
    while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
        if string[indexOfOriginal] == ' ':
            newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOriginal -= 1
        else:
            newStr[indexOfNew] = string[indexOfOriginal]
            indexOfNew -= 1
            indexOfOriginal -= 1
    return "".join(newStr)


print(replace4(string='we are happy'))