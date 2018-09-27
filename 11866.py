n,m=map(int,input().split())
w=m
jose=[]
josep=[]
for i in range(1,n+1):
      jose.append(i)
j=0
for i in range(n):
      while m>len(jose):
            m=m-len(jose)
      josep.append(jose[m-1])
      jose.pop(m-1)
      m+=w-1
k=0
prin="<"
p=0
for i in range(0,len(josep)):
      p=josep[i]
      prin+=str(p)
      k+=1
      if k==len(josep):
            prin+=">"
      else:
            prin+=", "
print(prin)
      
      
