a,b= map(int,input().split())
x=1
if a<b:
    for j in range(1,b+1):
        if (a%j==0 and b%j==0):
            x*=j
            a=a//j
            b=b//j
else:
    for j in range(1,a+1):
        if (a%j==0 and b%j==0):
            x*=j
            a=a//j
            b=b//j
print(a*b*x)
            
