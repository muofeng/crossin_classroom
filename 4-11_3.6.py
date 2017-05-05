sum=0
for x in range(1,5):
    for y in range(1,5):
        if y!=x:
            for z in range(1,5):
                if z!=x and z!=y:
                    sum+=1
                    print('%d%d%d' %(x,y,z))
print('sum=%d' %sum)


            
