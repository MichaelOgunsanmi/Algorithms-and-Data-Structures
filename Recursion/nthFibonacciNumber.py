def fibonacciIterative(index):
    if index == 0:
        return 0
    
    if index == 1:
        return 1

    prevValue = 0
    valueBeforePrevValue = 1
    while index >= 1:
        answer = prevValue + valueBeforePrevValue
        valueBeforePrevValue = prevValue
        prevValue = answer       
        index -= 1
    return answer

def fibonacciRecursive(index):
    if index == 0:
        return 0
    
    if index == 1:
        return 1
    
    return fibonacciRecursive(index - 1) + fibonacciRecursive(index - 2)

print('Iterative', fibonacciIterative(40))
print('Recursive', fibonacciRecursive(40))