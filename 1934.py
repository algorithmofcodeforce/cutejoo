num = int(input())
y=[]
for i in range(num):
    a,b= map(int,input().split())
    x=1
    if a<b:
        for j in range(1,b+1):
            if (a%j==0 and b%j==0):
                x*=j
                a=a//j
                b=b//j
        y.append(a*b*x)
    else:
        for j in range(1,a+1):
            if (a%j==0 and b%j==0):
                x*=j
                a=a//j
                b=b//j
        y.append(a*b*x)
    if i==num-1:
        for k in range(num):
            print(y[k])
