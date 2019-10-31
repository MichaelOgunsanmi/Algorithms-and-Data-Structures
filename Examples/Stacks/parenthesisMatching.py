import sys

sys.path.append(r'C:\Users\MICHAEL OGUNSANMI\Desktop\AI & '
                r'CS\Studying Source Codes\Software Intervierw '
                r'Preparation Codes\Algorithms-and-Data-Structures')
from StacksAndQueues.stacksWithArrays import Stack


def matchBrackets(inputString):
    stack = Stack()
    leftBrackets = {"(", "[", "{", "<"}
    rightBrackets = {")", "]", "}", ">"}

    for character in inputString:
        if character in leftBrackets:
            stack.push(character)

        if character in rightBrackets:
            if stack.isEmpty():
                return False
            currentTop = stack.pop()
            if currentTop != oppositeBracket(character):
                return False

    return stack.isEmpty()


def oppositeBracket(leftBracket):
    return "(" if leftBracket == ")" \
        else "[" if leftBracket == "]" \
        else "{" if leftBracket == "}" \
        else "<" if leftBracket == ">" \
        else None


print(matchBrackets("2{(3+4)}{{<<>>}}"))
