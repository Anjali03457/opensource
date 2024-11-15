a,b,c=list(map(int,input().split()))
if b>c:
    mango=0
else:
    mango= (c-b)//a
print(mango)
