# IPv4地址字符串位点('.')分隔的四段数字，每段数字取值范围为0~255，例如202.106.0.20,8.8.4.4。
# 请编写函数将其转换为32比特无符号整数。其中字符串中最左边的一段在最高位侧，最右边的一段在最低位侧。
# 例如上述两个IP地址转换完后分别是0xCA6A0014和0x08080404。
# 输入描述：输入数据每行为一个IPv4地址，
# 例如：
#     202.106.0.20
#     8.8.4.4
# 输出描述：
#  输出为解析后得到的整数的8位16进制表述，例如：
#      CA6A0014
#      08080404
# 注意不输出0x前缀，不够8位数用0补齐。对非法的输入，输出一个X


class Solution(object):
    def IPtoInt(self, num):
        a_list = num.split('.', 4)
        for i in a_list:
            if int(i) < 0 or int(i) > 255:
                return 'X'

        a_str = ''
        for i in a_list:
            a_tem = bin(int(i))[2:]
            if len(a_tem) != 8:
                # 在前面加 0
                a_str += '0' * (8 - len(a_tem)) + a_tem
            else:
                a_str += a_tem
        print(a_str)
        a = hex(int(a_str, 2))[2:]
        if len(a) != 8:
            a = '0' + a
        return a


s = Solution()
print(s.IPtoInt(num='202.106.0.20'))
print(s.IPtoInt(num='8.8.4.4'))


