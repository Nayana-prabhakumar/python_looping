# wap to reverse a number entered by the user


n=int(input("enter number"))
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n//=10
print(rev) 