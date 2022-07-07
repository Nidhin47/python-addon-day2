path="/home/administrator/nidhin/python/day2/sample.txt"
file=open(path).read()
count=0
n=raw_input("enter an alphabet:")
z=file.split()
for i in z:
    for j in i:
        if j==n:
            count=count+1
print "Number of "+str(n)+"'s"+" in the file is:",count