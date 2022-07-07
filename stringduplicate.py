x=raw_input("enter a string:")
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)