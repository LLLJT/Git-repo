a=eval(input("输入a:"))
b=eval(input("输入b:"))
c=eval(input("输入c:"))
d=eval(input("输入c:"))
if(a<b):
    a,b=b,a
if(a<c):
    a,c=c,a
if(a<d):
    a,d=d,a
if(b<c):
    b,c=c,b
if(b<d):
    b,d=d,b
if(c<d):
    c,d=d,c
print(a,b,c,d)