x='''Developer Wes is'''
evensum=0
oddsum=0
y=x.split()
for i in y:
    if len(i)%2==0:
        evensum=evensum+1
    else:
        oddsum=oddsum+1
print "the sum of evennumber words is:",evensum
print "the sum of oddnumber words is:",oddsum
