# 判断回文联
a = input('Please enter the string:')
b = len(a)


def judge(ordinery_string, length):
    if length == 1 or 0:  # 字符串长度为1和0时的情况
        print('%s is a palindrome.' % ordinery_string)
    else:
        i = 0
        while length > i:
            if ordinery_string[length - 1] == ordinery_string[i]:  # 判断字符串第i位和倒数第i位是否相同
                length -= 1
                i += 1
                if length - i == 1 or length - i == 0:  # 字符串长度为偶数时差为1,奇数时差为0
                    print('%s is a palindrome.' % ordinery_string)
            else:
                print('Sorry,%s is not a palindrome.' % ordinery_string)
                break


judge(a, b)


def judge(ordinery_string):  # 简易方法
    temp = list(ordinery_string)
    if temp == list(reversed(temp)):
        print('%s is a palindrome' % ordinery_string)
    else:
        print('%s is not a palindrome' % ordinery_string)
    return
