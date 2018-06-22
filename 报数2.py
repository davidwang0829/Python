#编写一个程序，输入整数后显示数字位数相同的* 并逐渐减少到一个*

print("开始报数")

number = int(input("请输入一个数字:")) #输入数字
while number<=0 or number > 20:
    number = int(input("请输入1-20的数字:")) #提示重新输入数字

i = 1
while number >= i:
    print("*"* number)
    number -= 1

print("报数完毕")
