# wap to print sum of even numbers from 1 to n entered by user

i=1
n=int(input("enter number"))
sum=0
while i<=n:
    if i%2==0:
        sum+=i
    i=i+1
print(sum)        