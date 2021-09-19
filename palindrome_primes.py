from math import sqrt, pow
sz = 100000
is_prime = [True for i in range(sz + 1)]  #list comperhension


def next():
    is_prime[0] = is_prime[1] = False
 
    for i in range(2, int(sqrt(sz)) + 1, 1):
        if (is_prime[i]):
            for j in range(i * i, sz, i):
                is_prime[j] = False
 

def findprimesdigit(d):
     
    left = int(pow(10, d - 1))
    right = int(pow(10, d) - 1)
    palindrome_prime=[]
    
    for i in range(left, right + 1, 1):
    
        if (is_prime[i]): 
            palindrome_prime.append(i)

    is_palindrome=[ x for x in palindrome_prime if str(x) == (str(x))[::-1]]
 
    print(is_palindrome)

     #       print(1, end = " ")
         

if __name__ == '__main__':
     
    # Generate primes with n digits
    next()
    d = 5
    findprimesdigit(d)
     
#print(is_prime)#