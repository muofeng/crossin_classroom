# coding:GBK
import random
num=random.randint(1,100)
a=input('����һ������:')
while a!=num:
    if a>num:
        print '���ֹ���'
    else:
        print '���ֹ�С'
    a=input('�ٲ�:')
print 'Bingo!'
print '����'
