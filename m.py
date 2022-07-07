def cumulative_product(n):
    s=[]
    c=1
    for i in n:
       c=c*i
       s.append(c)
    return(s)

def second(list):
    val=cumulative_product(list)
    print(val)
second(input("enter a list:"))