def carpim(a,b):
    c = a * b 
    return c

def bol(a,b):
    c = a / b
    return (c)

x=carpim(3,5)
y=bol(10,3)
print(y)

print(x)

def us(a,b):
    c= 1
    for x in range(b):
        c = c*a
    return c

z  = us(5,10)
print(z)
