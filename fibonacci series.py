n = int(input("ENTER A NUMBER:"))
a=0
b=1
i=a+b
print(a)
print(b)
while i<=n:
    print(i)
    a=b
    b=i
    i=a+b
