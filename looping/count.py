# wap to allow user to enter the numbers until user enter zero,print count
n=int(input("enter a number:"))
count=0
while n!=0:
    n=int(input("enter a number:"))
    count+=1
print("count=",count)   