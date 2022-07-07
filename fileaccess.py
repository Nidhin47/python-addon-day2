path="/home/administrator/nidhin/python/day2/sample.txt"
file=open(path).read()
print(file)
z=file.split()
y=[]
for i in z:
    if i not in y:
        y.append(i)
print(y)