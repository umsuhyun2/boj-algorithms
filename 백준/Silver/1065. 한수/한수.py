n=int(input())
cnt=0
for i in range(1,n+1):
    if i<100:
        cnt+=1
    elif i<1000:
        a=list(str(i))
        if (int(a[2])-int(a[1]))==(int(a[1])-int(a[0])):
            cnt+=1
print(cnt)