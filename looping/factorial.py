# wap to find the factorial entered by the user

n=int(input("enter the number:"))
i=n
fact=1
while i>=1:
    fact*=i
    i-=1
print(fact)    
