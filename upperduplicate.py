path="/home/administrator/nidhin/python/day2/sample.txt"
file=open(path).read()
a=file.upper()
print(a)
y=a.split()
z=[]
for i in y:
    if i not in z:
        z.append(i)
print(z)