def Fibonacci():
    cache = {}

    def nthFibonacciNumber(index):
        if index in cache:
            return cache[index]

        if index <= 1:
            return 1

        cache[index] = nthFibonacciNumber(index - 1) + nthFibonacciNumber(index - 2)
        print(cache)
        return cache[index]

    return nthFibonacciNumber


fib = Fibonacci()
print(fib(9))


def bottomUpFibonacci(index):
    answer = [1, 1]

    if index < 2:
        return answer[index]

    for i in range(2, index + 1):
        answer.append(answer[i - 1] + answer[i - 2])

    return answer.pop()


print('bottom up', bottomUpFibonacci(100))
