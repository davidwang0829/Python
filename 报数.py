#编写一个程序，输入整数后从1开始报数到该整数

print("开始报数")

number = int(input("请输入一个数字:")) #输入数字
while number<=0 or number > 100:
    number = int(input("请输入1-100的数字:")) #提示重新输入数字

i = 1

while number >= i:
    print(i)
    i = i + 1


print("报数完毕")
