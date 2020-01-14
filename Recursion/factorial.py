def findFactorialRecursive(number):
    if number <= 1:
        return 1
    
    return number * findFactorialRecursive(number - 1)


def findFactorialIterative(number):
    answer = 1
    while number > 1:
        answer *= number
        number -= 1
    return answer  


print('Iterative Answer', findFactorialIterative(0))
print('Recursive Answer', findFactorialRecursive(0))