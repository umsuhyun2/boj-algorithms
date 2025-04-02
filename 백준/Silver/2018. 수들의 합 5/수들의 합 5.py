n=int(input())
s=1
e=1
count=1 
sum=1 
while e!=n: 
    if sum==n:
        count+=1
        e+=1
        sum+=e
    elif sum<n:
        e+=1
        sum+=e
    else:
        sum-=s
        s+=1
         
print(count)