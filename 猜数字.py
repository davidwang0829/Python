print("") # 欢迎界面
import random 
answer = random.randint(1,100) # 生成随机数
i = 10              #可以（10）次

while i > 0:

    n = int(input("请输入1-100的整数:")) #用户输入数字

    if n == answer:
        print("恭喜你答对了")
        i = i - i
    elif n > answer:
        print("大了，您还有", i-1 , "次机会")
        i = i - 1
    else:
        print("小了，您还有", i-1 , "次机会")     #判断大小
        i = i - 1


print("数字是", answer, "游戏结束")  #游戏结束
    
