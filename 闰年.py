#编写一个程序，判断是否是闰年

print("欢迎使用") #欢迎使用

year = int(input("请输入一个年份:"))

while year <= 0:
    print("年份需要大于0,请重新输入")      #如果小于等于0 告知重新输入
    year = int(input("请输入一个年份:"))
if year % 4 == 0:
    print("您输入的年份", year, "是一个闰年")
else:
    print("您输入的年份", year, "不是一个闰年")

print("谢谢使用")
