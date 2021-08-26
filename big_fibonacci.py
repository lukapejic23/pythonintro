def big_fibonacci():

    previous_num, result = 0, 1
    desiredlength = int(input("enter the number of digits : "))

    while len(str(result)) < desiredlength:
        previous_num, result = result, previous_num + result

    return result

print(big_fibonacci())