weight=eval(input('Enter your weight(kg):'))
height=eval(input('Enter your height(m):'))
bmi=weight/height**2
if bmi<18.5:
    print('You are too thin')
elif bmi>=24:
    print('You are too fat')
else:
    print('Your weight is normal')
