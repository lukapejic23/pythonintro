def is_it_prime(n):  #to see if it is a prime number
     
    
    if n <= 1 :
        return False
 
    
    for i in range(2, n):
        if n % i == 0:
            return False
 
    return True
 

def primes_below(n):  #to print the prime numbers less than "n"
    for i in range(2, n + 1):
        if is_it_prime(i):
            print(i, end = " ") # to put a space?
 
if __name__ == "__main__" :
    
    
    
    n = 17

print: primes_below(n)
     