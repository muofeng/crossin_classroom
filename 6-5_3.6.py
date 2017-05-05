# coding:GBK
import random


def guess(num):
    ans = eval(input('我从1-100中选择了一个数，猜猜是几：'))
    if ans > num:
        print(ans, '太大了')
        return False
    elif ans < num:
        print(ans, '太小了')
        return False
    else:
        print('猜对了')
        return True


def play():
    num = random.randint(1, 100)
    while not guess(num):
        pass

while True:
    choice = input('请选择：s开始，e退出\n')
    if choice == 's':
        play()
    elif choice == 'e':
        break
    else:
        print("请重新选择")









