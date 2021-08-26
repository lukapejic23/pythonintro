# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,12] # ctrl + / 
def my_reverse(numbers):
    L = len(numbers)
    
    for i in range(int(L/2)):

        n = numbers[i]
        numbers[i] = numbers[L-i-1]
        numbers[L-i-1] = n
    

    print(numbers)
my_reverse([1,2,3,4,5])