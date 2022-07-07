c=input("enter a list:")
count1=0
count2=0
for i in c:
    if i%2==0:
        count1=count1+1
    else:
        count2=count2+1
print("count of even numbers in list:",count1)
print("count of odd numbers in list:",count2)
