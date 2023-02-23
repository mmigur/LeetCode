list1 = [9,9,9,9,9,9,9]
list2 = [9,9,9,9]

def addTwoSum(list1, list2):
    number1 = ''
    number2 = ''

    for char in list1:
        number1 += str(char)
    for char in list2:
        number2 += str(char)

    result_list = [int(number) for number in str(int(number1[::-1]) + int(number2[::-1]))]
    return result_list[::-1]

print(addTwoSum(list1, list2))