def pluOne(digits):
    number_str = ''

    for char in digits:
        number_str += str(char)
    
    number_int = int(number_str) + 1

    return [int(digit) for digit in str(number_int)]

print(pluOne([1,2,3]))