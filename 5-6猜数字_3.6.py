# coding:GBK
import random
totalrounds=0   #记录游戏轮数
totaltimes=0    #记录总猜测次数
totalwin=0      #记录猜中次数
chances=10      #每轮10次机会
play='y'        #是否继续游戏
while play=='y' or play=='Y':
    num=random.randint(1,100)
    print('我从1到100中选择了一个数，你猜是哪一个？你有%d次机会' %chances)
    for i in range(1,11):
        guess=eval(input())
        totaltimes+=1
        if guess==num:
            totalwin+=1
            print('Bingo!你猜对了!')
            break
        elif chances-i==0:
            print('你没机会了')
            break
        elif guess>num:
            print('太大了，你还有%d次机会' %(chances-i))
        else:
            print('太小了，你还有%d次机会' %(chances-i))
    totalrounds+=1
    play=input('是否继续游戏？(y/n)')
    while True:
        if play=='y' or play=='Y' or play=='n' or play=='N':
            break
        else:
            play=input('是否继续游戏？(y/n)')
if totalwin==0:
    print('你一次都没猜中')
else:
    print('你进行了%d轮游戏，平均猜%.2f次能够猜中' %(totalrounds,totaltimes/totalwin))

                  


                  


