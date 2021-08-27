for num in range(1, 1000):
    if num % 15 == 0:         # used 15 to combine divisibility by 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)