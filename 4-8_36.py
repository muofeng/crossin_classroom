for i in range(1,10):
    for j in range(1,10):
        if i>j:
            print('%d x %d=%d' %(i,j,i*j),end=' ')
        else:
            print('%d x %d=%d' %(i,j,i*j))
            break

