x=eval(input('x:'))
y=eval(input('y:'))
if x<10:
    if y<10:
        print('TT')
    elif y>10:
        print('TF')
    else:
        print('TO')
elif x>10:
    if y<10:
        print('FT')
    elif y>10:
        print('FF')
    else:
        print('FO')
else:
    if y<10:
        print('OT')
    elif y>10:
        print('OF')
    else:
        print('OO')
