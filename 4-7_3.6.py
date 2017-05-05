nums=[23,45,8,13,50,43,21]
sum=0
for n in nums:
    sum1=sum
    sum+=n
    if sum>100:break
print(sum1)
