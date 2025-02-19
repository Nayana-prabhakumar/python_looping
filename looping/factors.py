n=int(input("enter the number:"))
i=1
factors=[]
while i<n:
    if n%i==0:
        factors+=[i]
    i=i+1
print(factors)        