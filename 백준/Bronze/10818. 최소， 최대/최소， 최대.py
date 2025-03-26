a=int(input())
b=list(map(int,input().split()))
max=b[0]
min=b[0]
for i in b:
    
    if max<i:
        max=i
    if min>i:
        min=i
print(min,max)

        
    
    