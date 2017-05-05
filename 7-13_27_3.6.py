import random
score_you = 0
score_com = 0
choices = ['left', 'center', 'right']
for i in range(5):
    com_choice = random.choice(choices)
    your_choice = input('Choose one side to shoot(left, center or right):')
    print('You kicked ' + your_choice)
    if your_choice == com_choice:
        print('Oops.....')
    else:
        score_you += 1
        print('Goal!')
    print('Your score is %d,and your match\'s is %d' % (score_you, score_com))
    your_choice = input('Choose one side to save(left, center or right):')
    com_choice = random.choice(choices)
    print('You saved ' + your_choice)
    if your_choice == com_choice:
        print('Saved!')
    else:
        score_com += 1
        print('Oops......')
    print('Your score is %d,and your match\'s is %d' % (score_you, score_com))

