import sys

sys.path.append(r'C:\Users\MICHAEL OGUNSANMI\Desktop\AI & '
                r'CS\Studying Source Codes\Software Intervierw '
                r'Preparation Codes\Algorithms-and-Data-Structures')

from StacksAndQueues.stacksWithArrays import Stack


def isOperator(character):
    return character == "+" \
           or character == "-" \
           or character == "*" \
           or character == "/"


def precedence(character):
    if character == "+" or character == "-":
        return 1
    elif character == "*" or character == "/":
        return 2
    return 0


def infixToPostfixConversion(infixExpression):
    stack = Stack()
    postfix = ""

    for character in infixExpression:
        if not isOperator(character):
            postfix += character
            continue

        if stack.isEmpty():
            stack.push(character)
            continue

        while precedence(character) <= precedence(stack.top()):
            postfix += stack.pop()

        stack.push(character)

    while not stack.isEmpty():
        postfix += stack.pop()

    return postfix


def convertToValue(firstOperand, character, secondOperand):
    if character == "+":
        return firstOperand + secondOperand
    if character == "-":
        return firstOperand - secondOperand
    if character == "*":
        return firstOperand * secondOperand
    if character == "/":
        return firstOperand / secondOperand


def postfixEvaluation(postfixExpression):
    stack = Stack()

    for character in postfixExpression:
        if not isOperator(character):
            stack.push(int(character))
            continue

        secondOperand = stack.pop()
        firstOperand = stack.pop()
        result = convertToValue(firstOperand, character, secondOperand)

        stack.push(result)

    return stack.pop()


print(infixToPostfixConversion("a+b*c-d/e"))  # abc*+de/-
print(infixToPostfixConversion("a+b+c*d"))  # ab+cd*+

print(postfixEvaluation(infixToPostfixConversion("3*5+6/2-4")))  # 14.0
print(postfixEvaluation("234*+82/-"))  # 10
