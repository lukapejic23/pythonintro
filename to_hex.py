conversion_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']

def to_hex(x):
    if(x<=0):
        return ''
    remainder = x%16
    return  to_hex(x//16)+conversion_symbols[remainder]
        
#decimal = int(input("Enter a decimal number: "))
#print(to_hex(decimal))
def hex_color(red, green,blue):
    r=to_hex(red)
    g=to_hex(green)
    b=to_hex(blue)
    rgb="#"+r+g+b
    return rgb
test=hex_color(10,32,255)
print (test)
