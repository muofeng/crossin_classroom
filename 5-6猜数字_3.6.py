# coding:GBK
import random
totalrounds=0   #��¼��Ϸ����
totaltimes=0    #��¼�ܲ²����
totalwin=0      #��¼���д���
chances=10      #ÿ��10�λ���
play='y'        #�Ƿ������Ϸ
while play=='y' or play=='Y':
    num=random.randint(1,100)
    print('�Ҵ�1��100��ѡ����һ�������������һ��������%d�λ���' %chances)
    for i in range(1,11):
        guess=eval(input())
        totaltimes+=1
        if guess==num:
            totalwin+=1
            print('Bingo!��¶���!')
            break
        elif chances-i==0:
            print('��û������')
            break
        elif guess>num:
            print('̫���ˣ��㻹��%d�λ���' %(chances-i))
        else:
            print('̫С�ˣ��㻹��%d�λ���' %(chances-i))
    totalrounds+=1
    play=input('�Ƿ������Ϸ��(y/n)')
    while True:
        if play=='y' or play=='Y' or play=='n' or play=='N':
            break
        else:
            play=input('�Ƿ������Ϸ��(y/n)')
if totalwin==0:
    print('��һ�ζ�û����')
else:
    print('�������%d����Ϸ��ƽ����%.2f���ܹ�����' %(totalrounds,totaltimes/totalwin))

                  


                  


