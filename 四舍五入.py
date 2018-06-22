#四舍五入#

print("")

number = float(input("请输入一个数字："))

if number >=0:
    if int(number + 0.5) > number:
        print(int(number + 0.5))
    else:
        print(int(number))
else:
    if int(number - 0.5) < number:
        print(int(number - 0.5))
    else:
        print(int(number))


print("结束")
