x=raw_input("enter a string:")
y=x[::-1]
if x==y:
    print "the word "+str(x)+" is palindrome"
else:
    print "the word "+str(x)+" is not a palindrome"