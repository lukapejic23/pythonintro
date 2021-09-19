import math

class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
 
    def area(self):
        s = (self.a + self.b + self.c)/2
        area = math.sqrt(s*((s-self.a)*(s-self.b)*(s-self.c)))
        return area
    
 
    def perimeter(self):
        return self.a + self.b + self.c

    def scale(self, scale_factor) :
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid(a,b,c):
     if a+b>=c and b+c>=a and c+a>=b:
        return True
     else:
        return False    

    def is_right(a, b, c):
        if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
            return "True" 
        else:
            return "False"

    