sum= 0
for i in range(0,1000):
    if i % 3 ==0:
        sum1=i
        sum=sum+sum1
    elif i % 5 ==0:
        sum1=i
        sum=sum+sum1

print(sum)
