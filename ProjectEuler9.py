a: int = 1
b: int = 1
while a<1000:
    while b<1000:
        if (a+b+((a**2+b**2)**(1/2))==1000):
            print(a*b*(1000-a-b))
        if a**2 + b**2 == (1000-a-b)**2:
            print(a*b*(1000-a-b))
        b=b+1
    b=0
    a=a+1