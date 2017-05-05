num=10
for i in range(5):
    ans=eval(input('Enter a number:'))
    if ans>num:
            print('It\'s bigger than the right number')
    elif ans<num:
            print('It\'s smaller than the right number')
    else:
            print('Correct')
            break
    if i==4:
            print('You are foolish!')
