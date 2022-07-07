x=[1,2,22,33,4,4,5,5]
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)