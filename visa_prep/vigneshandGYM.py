p,q,r=list(map(int, input().split()))
if p+q<=r:
    print("2")
elif p>r:
    print("0")
else:
    print("1")
