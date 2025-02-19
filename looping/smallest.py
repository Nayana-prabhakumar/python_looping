# wap to find the smallest digit in a number

n=int(input("enter a number:"))
smallest=9
while n>0:
    last=n%10
    if last<smallest:
        smallest=last
    n=n//10
print("smallest digit=",smallest)        