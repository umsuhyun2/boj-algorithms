import sys
input=sys.stdin.readline

n=int(input())
A=list(map(int,input().split()))
A.sort()
cnt=0
for i in range(n):
    s = 0
    e = n - 1
    while s<e:

        if A[s]+A[e]==A[i]:
            if s!=i and e!=i:
                cnt+=1
                break
            elif s==i:
                s+=1
            else:
                e-=1

        elif A[s]+A[e]<A[i]:
            s+=1
        else:
            e-=1

print(cnt)


