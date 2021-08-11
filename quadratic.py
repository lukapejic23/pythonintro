import math

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))

d = b**2-4*a*c # discriminant

if d < 0:
    print ("No real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print (x)
else:
    x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    print (x1, x2)