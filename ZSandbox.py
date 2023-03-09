# def solution(x, y):
#     hashMap = {}

#     for numerator, denominator in zip(x, y):
#         decimalVal = numerator/denominator
#         hashMap[decimalVal] = hashMap.get(decimalVal, 0) + 1
    
    
#     print(hashMap)

#     return max(hashMap.values())




# solution([1,2,3,4,0], [2,3,6,8,4])


# def solution(S):
#     n = len(S)
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     numOfVowels = 0

#     for char in S:
#         if char in vowels:
#             numOfVowels += 1
    
#     print((S[:int(n/2)]))
#     print((S[int(n/2):]))
#     return abs(n - (2 * numOfVowels)) + solution(S[:int(n/2)]) + solution(S[int(n/2):])




# # base case
# # find the number of consonants and vowels in S, and find the difference. 
# # split S into 2 and add the left difference and the right difference



# print(solution('imbalance'))


# def solution(S, Y, Z):
#     numOfNewLines = 0
#     firstLength = 0
#     hasFound = False
#     for i in range(Y - 1, max(-1, Y - Z - 1), -1):
#         if S[i] == '\n':
#             numOfNewLines += 1
        
#         if numOfNewLines == 1 and not hasFound:
#             firstLength = i
#             hasFound = True

#         if numOfNewLines == 2:
#             break 
    
#     firstPart = S[i:Y]

#     numOfNewLines = 0
#     secondLength = len(S) - 1
#     hasFound = False
#     for i in range(Y + 1, min(len(S), Y + Z + 1)):
#         if S[i] == '\n':
#             numOfNewLines += 1
        
#         if numOfNewLines == 1 and not hasFound:
#             secondLength = i
#             hasFound = True
#             print(i, 'hit')

#         if numOfNewLines == 2:
#             break 
#     secondPart = S[ Y+1: i + 1]
    

#     caratRow = ((Y - (firstLength + 1)) * ' ') + '^' + ((secondLength - Y - 1) * ' ') + '\n'
    
#     return (firstPart + S[Y] + secondPart[:(secondLength - Y)] + caratRow + secondPart[(secondLength - Y):])


# print(solution('123', 1, 0))



# # With the element at Y, Find the line before it and find the line after it
# # this will be your scope. using this scope, find the Z characters either side.  
# # find the length of the line housing position Y. then concatenate the before characters
# # the carat character and the after characters. return this concatenation

