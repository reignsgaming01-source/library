def func(s):
    sum=0
    for x in s:
        sum+=int(x)**2
    return sum
s=input()
b=int(s)
aa=func(s)
while aa!=1:
    s=str(aa)
    aa=func(s)
    if len(s)>2:
        break
if aa==1:
    print(b,"is HAPPY")
else:
    print(b,"is not HAPPY")
    
    
