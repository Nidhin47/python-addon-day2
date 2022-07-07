c=input("enter a list:")
sum1=0
sum2=0
for i in c:
    if i%2==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print "sum of even numbers in list:",sum1
print "sum of odd numbers in list:",sum2
