"""
@ Title:
@ Author: Cathy
@ Time: 2024/4/12 19:35
"""
import random


def number_guessing():
    while True:
        print("*******************************")
        print("*******    1.play  ************")
        print("*******    0.exit  ************")
        print("*******************************")
        ret = int(input("请选择1开始或者0退出游戏："))
        random_num = random.randint(1, 100)
        if ret == 1:
            print("*********  开始游戏  ********")
            while True:
                input_num = int(input("请猜数字："))
                if input_num < random_num:
                    print("猜小了")
                elif input_num > random_num:
                    print("猜大了")
                else:
                    print("恭喜，猜对了！")
                    break
        elif ret == 0:
            print("退出游戏")
            break


number_guessing()
