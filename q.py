a,b=map(int,input().split())
d=[]
for i in range(a):
    q=list(map(str,input().split()))
    if len(sorted(set(q)))==1:
        pass
    else:
        print(q.index("*"))