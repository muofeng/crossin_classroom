# coding:GBK
import random


def guess(num):
    ans = eval(input('�Ҵ�1-100��ѡ����һ�������²��Ǽ���'))
    if ans > num:
        print(ans, '̫����')
        return False
    elif ans < num:
        print(ans, '̫С��')
        return False
    else:
        print('�¶���')
        return True


def play():
    num = random.randint(1, 100)
    while not guess(num):
        pass

while True:
    choice = input('��ѡ��s��ʼ��e�˳�\n')
    if choice == 's':
        play()
    elif choice == 'e':
        break
    else:
        print("������ѡ��")









