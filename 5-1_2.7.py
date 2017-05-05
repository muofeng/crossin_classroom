# coding:GBK
import random
num=random.randint(1,100)
a=input('输入一个数字:')
while a!=num:
    if a>num:
        print '数字过大'
    else:
        print '数字过小'
    a=input('再猜:')
print 'Bingo!'
print '结束'
